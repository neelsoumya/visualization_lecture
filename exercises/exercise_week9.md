# 🎮💡🛠️ Exercise (social media harm) data storytelling

# Assignment: Visualizing the Harms of Social Media

## Overview

Social media platforms have become central to modern communication, politics, and culture. However, they have also been associated with a range of potential harms, including misinformation, political polarization, mental health effects, and economic disruption.

In this assignment, you will analyze a **synthetic dataset on social media harms across countries** and use data visualization techniques to investigate patterns in the data. Based on your analysis, you will write a **policy brief recommending whether a country should regulate, restrict, or ban social media platforms**.

The goal of the assignment is not only to produce good visualizations, but also to **interpret data critically and communicate policy implications clearly**.

---

# Dataset

You are provided with a **synthetic dataset** containing indicators related to social media use and potential harms in different countries.

The dataset includes variables such as:

* Social media usage (penetration and time spent)
* Misinformation index
* Youth mental health decline indicators
* Political polarization measures
* Content moderation strength
* Censorship levels
* Regulatory strength
* Economic dependency on social media platforms
* Composite harm scores

The dataset is **synthetic**, meaning it was generated artificially for the purpose of analysis and teaching. Treat it as if it were real data, but remember that conclusions are illustrative rather than factual.

---

# Assignment Tasks

## 1. Exploratory Data Analysis

Perform an initial exploration of the dataset.

You should:

* Examine the distribution of key variables
* Identify possible relationships between variables
* Identify outliers or unusual countries

Produce **at least two visualizations** showing patterns in the data.

Examples include:

* Scatter plots
* Correlation heatmaps
* Bar charts
* Bubble charts
* Histograms

---

## 2. Visualizing Social Media Harms

Create **at least three visualizations** that illustrate different types of social media harms.

Examples of research questions you might explore include:

* Is higher social media usage associated with greater youth mental health decline?
* Does misinformation correlate with political polarization?
* Do countries with weak regulation show higher harm scores?
* How do harm profiles differ between political regimes?

Your visualizations should:

* Clearly label axes and variables
* Use appropriate scales
* Include informative titles
* Be easy to interpret

---

## 3. Comparative Country Analysis

Select **one country from the dataset** and conduct a deeper analysis.

You should:

* Compare your chosen country to at least **three other countries**
* Identify which harms are most significant
* Explain how your country differs from others

Use visualizations to support your argument.

---

## 4. Policy Recommendation

Write a **short policy brief (800–1200 words)** recommending one of the following actions for your chosen country:

* No restriction (monitoring only)
* Moderate regulation
* Targeted restrictions
* Partial platform bans
* Full ban of social media platforms

Your policy brief should include:

### Executive Summary

A short paragraph summarizing your recommendation.

### Evidence

Use **visualizations and data analysis** to justify your position.

### Policy Options

Discuss at least two possible policy approaches.

### Recommendation

Explain which policy you recommend and why.

### Limitations

Discuss limitations of the dataset and your analysis.

---

# Deliverables

Submit the following:

1. **3–5 visualizations**
2. **Policy brief (800–1200 words)**
3. **Code used for analysis** (Python or R)


## Code to generate synthetic data

Code to generate synthetic data is here

```python
# Fixed run: generate the dataset and save CSV.
import numpy as np
import pandas as pd

np.random.seed(42)

countries = [
    "United States", "United Kingdom", "India", "China", "Brazil", "Nigeria", "Russia", "Germany",
    "Australia", "Japan", "Sweden", "Mexico", "South Africa", "Turkey", "Egypt", "Saudi Arabia",
    "Indonesia", "Argentina", "Poland", "Vietnam"
]

regime_map = {
    "United States": "democracy",
    "United Kingdom": "democracy",
    "India": "democracy",
    "China": "authoritarian",
    "Brazil": "democracy",
    "Nigeria": "hybrid",
    "Russia": "authoritarian",
    "Germany": "democracy",
    "Australia": "democracy",
    "Japan": "democracy",
    "Sweden": "democracy",
    "Mexico": "hybrid",
    "South Africa": "hybrid",
    "Turkey": "hybrid",
    "Egypt": "authoritarian",
    "Saudi Arabia": "authoritarian",
    "Indonesia": "democracy",
    "Argentina": "democracy",
    "Poland": "democracy",
    "Vietnam": "authoritarian"
}

n = len(countries)

population_m = np.random.uniform(5, 330, size=n).round(1)
internet_penetration = np.clip(np.random.normal(70, 15, n), 20, 98).round(1)
social_media_penetration = np.clip(internet_penetration * np.random.uniform(0.6, 0.95, n), 10, 98).round(1)
avg_daily_time = np.clip(np.random.normal(95, 35, n), 10, 400).round(1)

misinformation_index = np.clip(np.random.beta(2,5,n)*100 + (np.array([1 if regime_map[c]!="democracy" else 0 for c in countries])*10) + np.random.normal(0,6,n), 0, 100).round(1)
content_moderation_score = np.clip(np.random.normal(60, 18, n) - (np.array([1 if regime_map[c]=="authoritarian" else 0 for c in countries])*12), 5, 98).round(1)
censorship_level = np.clip(np.random.normal(25, 20, n) + (np.array([1 if regime_map[c]=="authoritarian" else 0 for c in countries])*45), 0, 100).round(1)
regulatory_strength = np.clip(np.random.beta(2,3,n) - (np.array([0.2 if regime_map[c]=="authoritarian" else 0 for c in countries])) + np.random.normal(0,0.05,n), 0, 1).round(2)
reported_harm_incidents_per_100k = np.clip((misinformation_index/100)*np.random.uniform(40,200,n) + (avg_daily_time/120)*np.random.uniform(5,50,n) + np.random.normal(0,10,n), 0, None).round(1)
youth_mental_health_decline_pct = np.clip((avg_daily_time/240)*np.random.uniform(5,35,n) + (misinformation_index/100)*np.random.uniform(2,15,n) + np.random.normal(0,2,n), 0, 50).round(2)
political_polarization_index = np.clip(np.random.normal(45,18,n) + (misinformation_index*0.15) - (content_moderation_score*0.1), 0, 100).round(1)
economic_dependency_pct = np.clip(np.random.normal(0.8,0.6,n) + (social_media_penetration/100)*np.random.uniform(0.1,1.5,n), 0, 8).round(2)

public_health_harm_score = np.clip(0.6*youth_mental_health_decline_pct + 0.2*(misinformation_index) + 0.2*(reported_harm_incidents_per_100k/10), 0, 100).round(1)
political_harm_score = np.clip(0.5*political_polarization_index + 0.4*misinformation_index + 0.1*censorship_level, 0, 100).round(1)
economic_harm_score = np.clip(0.5*economic_dependency_pct*10 + 0.3*(reported_harm_incidents_per_100k/20) + 0.2*(100-content_moderation_score)/10, 0, 100).round(1)

ban_risk_score_arr = np.clip(0.35*public_health_harm_score + 0.35*political_harm_score + 0.2*reported_harm_incidents_per_100k/10 + 0.1*(100* (1-regulatory_strength)), 0, 100).round(1)

df = pd.DataFrame({
    "country": countries,
    "population_m": population_m,
    "regime": [regime_map[c] for c in countries],
    "internet_penetration_pct": internet_penetration,
    "social_media_penetration_pct": social_media_penetration,
    "avg_daily_time_min": avg_daily_time,
    "misinformation_index_0_100": misinformation_index,
    "content_moderation_score_0_100": content_moderation_score,
    "censorship_level_0_100": censorship_level,
    "regulatory_strength_0_1": regulatory_strength,
    "reported_harm_incidents_per_100k": reported_harm_incidents_per_100k,
    "youth_mental_health_decline_pct": youth_mental_health_decline_pct,
    "political_polarization_index_0_100": political_polarization_index,
    "economic_dependency_pct_of_gdp": economic_dependency_pct,
    "public_health_harm_score_0_100": public_health_harm_score,
    "political_harm_score_0_100": political_harm_score,
    "economic_harm_score_0_100": economic_harm_score,
    "ban_risk_score_0_100": ban_risk_score_arr
})

```

- Solution is here

```python
# Analysis "solution" for the classroom exercise.
# Loads the synthetic CSV and produces:
# 1) Descriptive statistics
# 2) Correlation matrix (displayed)
# 3) Scatter plots with linear fit for two pairs of interest
# 4) Counts of suggested_policy_action by regime (table)
# 5) K-means clustering (k=3) on harm scores and cluster centers
# 6) Top 5 countries by ban_risk_score
# Saves a small report CSV and plots to /mnt/data for download.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
#from caas_jupyter_tools import display_dataframe_to_user

# Load dataset
#path = "/mnt/data/synthetic_social_media_harms.csv"
#df = pd.read_csv(path)



# 1) Descriptive statistics (selected columns)
desc_cols = [
    "internet_penetration_pct","social_media_penetration_pct","avg_daily_time_min",
    "misinformation_index_0_100","reported_harm_incidents_per_100k","youth_mental_health_decline_pct",
    "political_polarization_index_0_100","public_health_harm_score_0_100","political_harm_score_0_100",
    "economic_harm_score_0_100","ban_risk_score_0_100"
]
desc = df[desc_cols].describe().round(2)
#display_dataframe_to_user("Descriptive statistics (selected columns)", desc.reset_index())

# 2) Correlation matrix
corr = df[desc_cols].corr().round(2)
#display_dataframe_to_user("Correlation matrix (selected harm & exposure variables)", corr.reset_index())

# 3) Scatter: avg_daily_time_min vs youth_mental_health_decline_pct with linear fit
x = df["avg_daily_time_min"].values
y = df["youth_mental_health_decline_pct"].values
coef = np.polyfit(x, y, 1)
poly1d = np.poly1d(coef)

plt.figure(figsize=(7,5))
plt.scatter(x, y)
plt.plot(np.sort(x), poly1d(np.sort(x)))
plt.xlabel("avg_daily_time_min")
plt.ylabel("youth_mental_health_decline_pct")
plt.title("Scatter: avg daily social media time vs youth mental-health decline")
plt.tight_layout()
#plt.savefig("/mnt/data/plot_time_vs_mental_health.png")
plt.show()

# Linear fit stats (R^2)
y_pred = poly1d(x)
ss_res = np.sum((y - y_pred)**2)
ss_tot = np.sum((y - np.mean(y))**2)
r2_time = 1 - ss_res/ss_tot

# 4) Scatter: misinformation_index vs political_polarization_index with fit
x2 = df["misinformation_index_0_100"].values
y2 = df["political_polarization_index_0_100"].values
coef2 = np.polyfit(x2, y2, 1)
poly2 = np.poly1d(coef2)
y2_pred = poly2(x2)
ss_res2 = np.sum((y2 - y2_pred)**2)
ss_tot2 = np.sum((y2 - np.mean(y2))**2)
r2_misinfo = 1 - ss_res2/ss_tot2

plt.figure(figsize=(7,5))
plt.scatter(x2, y2)
plt.plot(np.sort(x2), poly2(np.sort(x2)))
plt.xlabel("misinformation_index_0_100")
plt.ylabel("political_polarization_index_0_100")
plt.title("Scatter: misinformation vs political polarization")
plt.tight_layout()
#plt.savefig("/mnt/data/plot_misinfo_vs_polarization.png")
plt.show()

# 5) Counts of suggested_policy_action by regime
counts = df.groupby(["regime","suggested_policy_action"]).size().unstack(fill_value=0)
#display_dataframe_to_user("Suggested policy action counts by regime", counts.reset_index())

# 6) K-means clustering on harm scores (public, political, economic)
harm_features = df[["public_health_harm_score_0_100","political_harm_score_0_100","economic_harm_score_0_100"]].copy()
scaler = StandardScaler()
harm_scaled = scaler.fit_transform(harm_features)

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
clusters = kmeans.fit_predict(harm_scaled)
df["harm_cluster"] = clusters
cluster_centers = scaler.inverse_transform(kmeans.cluster_centers_).round(2)
cluster_centers_df = pd.DataFrame(cluster_centers, columns=harm_features.columns)
cluster_centers_df["cluster"] = cluster_centers_df.index
#display_dataframe_to_user("K-means cluster centers (k=3) on harm scores (original scale)", cluster_centers_df)

# Show cluster membership table (country -> cluster)
cluster_table = df[["country","regime","ban_risk_score_0_100","suggested_policy_action","harm_cluster"]].sort_values("ban_risk_score_0_100", ascending=False)
#display_dataframe_to_user("Countries with cluster membership and key metrics", cluster_table.reset_index(drop=True))

# 7) Top 5 countries by ban_risk_score
top5 = df.nlargest(5, "ban_risk_score_0_100")[["country","ban_risk_score_0_100","regime","suggested_policy_action"]]
#display_dataframe_to_user("Top 5 countries by ban risk score", top5.reset_index(drop=True))

# Save CSV report
report_csv = "/mnt/data/synthetic_solution_report.csv"
#df.to_csv(report_csv, index=False)

# Print summary stats for assistant text
summary = {
    "r2_time_vs_mental_health": round(r2_time,3),
    "coef_time_vs_mental_health": coef.round(3).tolist(),
    "r2_misinfo_vs_polarization": round(r2_misinfo,3),
    "coef_misinfo_vs_polarization": coef2.round(3).tolist(),
    "cluster_centers": cluster_centers_df.to_dict(orient="records"),
    "top5_list": top5.to_dict(orient="records"),
    "report_csv": report_csv,
    "plot_time_vs_mental_health": "/mnt/data/plot_time_vs_mental_health.png",
    "plot_misinfo_vs_polarization": "/mnt/data/plot_misinfo_vs_polarization.png"
}

summary

```