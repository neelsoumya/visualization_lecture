# visualization + exploratory data analysis while using the COMPAS recidivism dataset to highlight bias and introduce basic fairness metrics


# Learning goals (what students should take away)

1. How to do quick EDA and visual storytelling with real-world tabular data.
2. How to visualize and quantify group differences (race, sex) in a classifier’s outputs.
3. What simple fairness metrics (FPR, FNR, calibration, predictive parity) mean and how they can be computed/visualized.
4. Awareness of the limits of visualizations: they can reveal patterns but not settle ethical or legal questions.

---

# 1 — Lecture plan (50–75 mins)

1. (5 min) Motivation + context: algorithmic risk scores in criminal justice (short ethical framing).
2. (10 min) Quick EDA demo: load COMPAS table, inspect columns, missingness, basic distributions.
3. (15 min) Visual comparisons: score distribution by race / sex; bar plots of positive predictions; confusion-matrix-based group metrics.
4. (10 min) Fairness metrics: define and show how to compute FPR/FNR, calibration, ROC/PR by group.
5. (10–20 min) Hands-on coding exercise (students work in pairs): reproduce a plot and compute group FPR/FNR — short discussion afterwards.

---

# 2 — Instructor notes & talking points

* **Context** (short): The dataset used in many fairness studies is a public extract of risk-assessment scores used by courts; investigators noted disparities between groups when using common error-rate metrics. Use this to emphasize *how different fairness definitions produce different conclusions* about whether a model is “biased.” (See Sources.) ([ProPublica][1])
* **One caution**: visual differences do not automatically imply unlawful discrimination — there are many confounders (different base rates, covariate differences, label noise). Use visuals to motivate deeper thinking, not to close the argument. ([Harvard Data Science Review][2])
* **Pedagogy tip**: Ask students to first predict (by hand) whether each visualization will show a difference, then show the plot — the prediction step encourages reflection and reduces passive viewing.
* **Ethics**: Remind students this is sensitive material — anonymized research data, but the subject matter affects real people.

---

# 3 — Slide / demo checklist (short)

* Title slide (topic + learning goals)
* Short bullets: what COMPAS is + dataset provenance (one-line)
* Demo 1: head(), describe(), missingness heatmap
* Demo 2: histogram / KDE of COMPAS score by race
* Demo 3: confusion matrices (thresholded) and bar chart of FPR/FNR by group
* Demo 4: calibration plot (predicted risk deciles vs observed recidivism)
* Homework/Challenge slide

---

# 4 — Practical Python exercises & code

**Prereqs:** `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`.
Instruction: Download the COMPAS CSV (save as `compas.csv`) from the ProPublica compas analysis repo (see Sources) and place it in the working directory.

---

## Utility: load + quick EDA

```python
# File: compas_eda.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

DATA_PATH = "compas.csv"  # save the downloaded CSV at this path

# 1. Load
df = pd.read_csv(DATA_PATH)

# 2. Quick inspect
print(df.shape)
display(df.head())
display(df.describe(include='all'))

# 3. Relevant example columns (may differ slightly by CSV version)
# Typical names: 'race', 'sex', 'age', 'age_cat', 'c_charge_degree',
# 'priors_count', 'decile_score' (1-10), 'two_year_recid' (0/1), 'is_recid'

# 4. Missingness heatmap
plt.figure(figsize=(10,4))
sns.heatmap(df.isnull(), cbar=False)
plt.title("Missingness (True = missing)")
plt.show()
```

---

## Exercise A — Distribution of COMPAS scores by race (visual)

Task: plot histograms and KDEs of the COMPAS decile score across two race groups (e.g., Black vs White).

```python
# Exercise A
plt.figure(figsize=(9,5))
sns.histplot(data=df[df['race'].isin(['African-American','Caucasian'])],
             x='decile_score', hue='race', bins=10, kde=False, stat='density', alpha=0.6)
plt.title("Distribution of COMPAS decile score by race")
plt.xlabel("decile_score (1=low ... 10=high)")
plt.show()

# KDE alternative
plt.figure(figsize=(9,5))
sns.kdeplot(data=df[df['race'].isin(['African-American','Caucasian'])],
            x='decile_score', hue='race', fill=True)
plt.title("KDE of COMPAS decile score by race")
plt.show()
```

**Discussion prompts:** Do the score distributions differ? Which group shows more mass at higher scores?

---

## Exercise B — Threshold, confusion matrix, and group FPR/FNR

We’ll threshold decile score: classify as `pred = (decile_score >= 5)` (this is the threshold ProPublica used to split low vs medium/high in examples).

```python
# Exercise B: compute group metrics
from sklearn.metrics import confusion_matrix

THRESH = 5
df = df.copy()
df['pred_high'] = (df['decile_score'] >= THRESH).astype(int)
# outcome: whether re-arrested within two years (column name may be 'two_year_recid' or 'is_recid')
OUTCOME = 'two_year_recid'  # adjust if your CSV uses a different name

groups = df['race'].unique()
results = []
for g in groups:
    sub = df[df['race'] == g]
    if sub.empty: 
        continue
    tn, fp, fn, tp = confusion_matrix(sub[OUTCOME], sub['pred_high'], labels=[0,1]).ravel()
    # careful: confusion_matrix order: [[tn, fp],[fn, tp]]
    fpr = fp / (fp + tn) if (fp + tn) > 0 else np.nan
    fnr = fn / (fn + tp) if (fn + tp) > 0 else np.nan
    tpr = tp / (tp + fn) if (tp + fn) > 0 else np.nan
    precision = tp / (tp + fp) if (tp + fp) > 0 else np.nan
    results.append({'race': g, 'n': len(sub), 'TP': tp, 'FP': fp, 'TN': tn, 'FN': fn,
                    'FPR': fpr, 'FNR': fnr, 'TPR': tpr, 'Precision': precision})

res_df = pd.DataFrame(results).sort_values('n', ascending=False)
display(res_df)
```

**Visualization of FPR/FNR:**

```python
res_df = res_df.set_index('race')
res_df[['FPR','FNR']].plot.bar(figsize=(9,5))
plt.title(f'FPR and FNR by race (threshold = {THRESH})')
plt.ylabel('Rate')
plt.show()
```

**Talking points:** If one group has substantially higher FPR, that group experiences more false alarms (predicted high risk but did not recidivate). Conversely, higher FNR means more missed positives.

---

## Exercise C — Calibration plot (predicted risk vs observed recidivism)

Use decile score as "predicted risk" (1–10). Group into buckets and plot observed recidivism rate per bucket.

```python
# Exercise C: calibration by decile
df['pred_score_norm'] = (df['decile_score'] - df['decile_score'].min()) / \
                        (df['decile_score'].max() - df['decile_score'].min())

# Create decile bins (1..10 already maps, but we'll aggregate)
df['decile'] = df['decile_score']  # if already 1..10
calib = df.groupby('decile').agg(
    mean_pred=('decile_score', 'mean'),
    obs_rate=(OUTCOME, 'mean'),
    n=(OUTCOME, 'count')
).reset_index()

plt.figure(figsize=(7,5))
plt.plot(calib['mean_pred'], calib['obs_rate'], marker='o', linestyle='-')
plt.plot([1,10],[df[OUTCOME].mean(), df[OUTCOME].mean()], '--', label='overall recid rate')
plt.xlabel('mean decile score in bin')
plt.ylabel('observed recidivism rate')
plt.title('Calibration: predicted decile vs observed recidivism')
plt.legend()
plt.show()
```

**Extension:** compute calibration curves separately for two groups (e.g., Black and White) to see whether predicted risk maps to observed probability similarly.

---

## Exercise D — Simple fairness comparison: remove race and retrain

Task: build a logistic regression predicting `two_year_recid` using a few features (age, priors_count, charge degree), *excluding* race, then compare group error rates.

```python
# Exercise D: simple model (train/test split)
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# select features - omit race
features = ['age', 'priors_count']  # adjust as available in your CSV
df_model = df.dropna(subset=features + [OUTCOME])
X = df_model[features]
y = df_model[OUTCOME]

X_train, X_test, y_train, y_test, g_train, g_test = train_test_split(
    X, y, df_model['race'], test_size=0.3, random_state=42, stratify=df_model['race']
)

clf = LogisticRegression(max_iter=1000).fit(X_train, y_train)
y_pred = clf.predict(X_test)

print("Overall accuracy:", accuracy_score(y_test, y_pred))

# compute FPR/FNR per group on test set
test_df = X_test.copy()
test_df['race'] = g_test.values
test_df['y_true'] = y_test.values
test_df['y_pred'] = y_pred

def group_metrics(df, group_col='race'):
    rows = []
    for g, sub in df.groupby(group_col):
        tn, fp, fn, tp = confusion_matrix(sub['y_true'], sub['y_pred'], labels=[0,1]).ravel()
        fpr = fp / (fp + tn) if (fp + tn) > 0 else np.nan
        fnr = fn / (fn + tp) if (fn + tp) > 0 else np.nan
        rows.append({'group': g, 'n': len(sub), 'FPR': fpr, 'FNR': fnr})
    return pd.DataFrame(rows)

display(group_metrics(test_df))
```

**Homework extension:** try including race as a feature and see how metrics change.

---

# 5 — Short classroom exercises (compact)

1. (5–10 min) Interpret the decile histograms: what story do they tell?
2. (10–15 min) Compute FPR/FNR for Black vs White; propose one visualization that best communicates the harm of a high FPR.
3. (Homework) Build calibration curves separated by race and explain whether the score is calibrated across groups.

---

# 6 — Example answers / instructor notes for the exercises

* Expect to see higher mass of higher decile scores for African-American defendants in many extracts of the dataset; this leads to different error rates when a single threshold is used. (Use the FPR/FNR table to demonstrate.) ([ProPublica][1])
* Be ready to point out dataset artifacts: how labels (`two_year_recid`) are defined, sample selection (Broward County), and measurement error. These matter when interpreting fairness. ([GitHub][3])

---

# 7 — Further reading & data sources

* ProPublica — ProPublica’s analysis and the original dataset release (Broward County two-year scores). ([ProPublica][1])
* Northpointe — Northpointe (the vendor who produces COMPAS) published a technical rebuttal/analysis of the ProPublica findings. Useful for discussing alternative framings. ([go.volarisgroup.com][4])
* Broward County Sheriff's Office — the public records source used to compile the released scores. ([GitHub][3])
* Rudin et al., MIT/HDSR — a critical discussion on fairness definitions and a reminder that seemingly “fair” metrics can be sensitive to base rates and modeling choices. ([Harvard Data Science Review][2])

---

# 8 — Final teaching tips

* Use the plots to *raise questions* rather than to make definitive claims. Encourage students to ask: *Who decides which metric matters? What are the downstream harms?*
* Encourage reproducibility: have students submit a short notebook reproducing one figure + one table of group metrics.
* Emphasize limitations: dataset provenance, labeling noise, sampling biases.

