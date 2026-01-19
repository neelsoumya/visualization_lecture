# Seaborn


**Learning objectives**

* Understand Seaborn's design principles and how it differs from matplotlib.
* Know the major plot *types* and the common Seaborn functions for each.
* Distinguish figure-level and axes-level APIs (e.g., `displot` vs `histplot`).
* Be able to create informative plots with built-in datasets and style controls.
* Learn basic composition: `FacetGrid`, `PairGrid`, combining Seaborn + Matplotlib.
* Gain three hands-on mini-exercises to apply learned techniques.

---

## Quick outline (timed)

1. Introduction & design philosophy — 5 min
2. Seaborn basics: data formats, theme/style — 10 min
3. Plot categories and representative functions — 25 min

   * Relational (scatter/line)
   * Categorical
   * Distribution
   * Regression & statistical
   * Matrix / multivariate
4. Grids & figure-level plots (`FacetGrid`, `PairGrid`) — 8 min
5. Practical tips, pitfalls, combining with Matplotlib — 7 min
6. Exercises & resources — 5 min

---

# 1. Introduction & design principles (5 min)

* **Seaborn** is a high-level API built on top of matplotlib, designed for *statistical* data visualization.
* Works best with **tidy (long-form)** data (one observation per row, columns are variables).
* Offers default themes, color palettes, and convenient statistical aggregations.
* Two main API styles:

  * **Figure-level** functions (create entire figure + facets) — `displot`, `relplot`, `catplot`, `pairplot`, `lmplot`.
  * **Axes-level** functions (plot on an existing `Axes`) — `scatterplot`, `histplot`, `boxplot`, `violinplot`, `heatmap`, etc.

---

# 2. Seaborn basics: data formats, theme, imports (10 min)

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.__version__  # ensure recent version (0.11+ has many features)

# load example datasets
tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")
penguins = sns.load_dataset("penguins")
```

**Data forms**

* `long` (tidy): each row = observation. e.g. `tips` (total_bill, tip, sex, smoker, day, time)
* `wide`: multiple related measurement columns (e.g., columns for each time point). Some seaborn functions accept wide-form directly.

**Themes & context**

```python
sns.set_theme(style="whitegrid", context="notebook")
# style: whitegrid, darkgrid, white, ticks, dark
# context: paper, notebook, talk, poster

# control rc parameters
sns.set(rc={"figure.figsize": (8, 5)})
```

**Color palettes**

```python
sns.color_palette("deep")
sns.color_palette("crest", as_cmap=True)

# categorical vs sequential vs diverging
sns.palplot(sns.color_palette("tab10"))
```

---

# 3. Plot categories & representative functions (25 min)

> We'll list functions by purpose with short code examples.

## A. Relational plots — show relationships between variables

**Axes-level**: `scatterplot`, `lineplot`.

```python
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time", style="smoker")

sns.lineplot(data=some_time_series_df, x="date", y="value", hue="category")
```

**Figure-level**: `relplot(kind="scatter" / "line")` — convenience wrapper that returns `FacetGrid`.

```python
sns.relplot(data=tips, x="total_bill", y="tip", col="day", hue="sex", kind="scatter")
```

**Notes**: `scatterplot` accepts `size`, `hue`, `style` for multidimensional encoding. Use `alpha` and `s` for density/marker size.

## B. Categorical plots — comparing categories

* `stripplot`, `swarmplot` (jittered points)
* `boxplot`, `violinplot` (distribution summaries)
* `barplot` (aggregate with CI), `countplot` (counts)
* `pointplot` (point estimates with CI)

```python
sns.boxplot(data=tips, x="day", y="total_bill")
sns.violinplot(data=tips, x="day", y="total_bill", hue="sex", split=True)

sns.barplot(data=tips, x="day", y="total_bill", estimator=sum)
sns.countplot(data=tips, x="day")
```

**Figure-level**: `catplot(kind=...)` — good for faceting.

```python
sns.catplot(data=tips, x="day", y="tip", kind="violin", hue="sex", col="time")
```

**When to use**: use `boxplot` for robust summaries, `violinplot` for showing full distribution, `strip/swarm` for raw points.

## C. Distribution plots — one or two variables

* `histplot`, `kdeplot`, `ecdfplot`, `displot` (figure-level combining hist/kde)

```python
sns.histplot(data=iris, x="sepal_length", kde=True)
sns.kdeplot(data=iris, x="sepal_length", hue="species", fill=True)

sns.displot(data=iris, x="sepal_length", col="species", kde=True)
```

**Notes**: `displot` returns a `FacetGrid` so you can facet easily.

## D. Regression & statistical models

* `regplot` (axes-level), `lmplot` (figure-level + faceting)

```python
sns.regplot(data=tips, x="total_bill", y="tip", scatter_kws={"s": 10})

sns.lmplot(data=tips, x="total_bill", y="tip", hue="smoker", col="day")
```

**Options**: lowess smoothing, polynomial `order`, `ci` for confidence intervals.

## E. Multivariate / matrix plots

* `heatmap` (matrices/correlations)
* `clustermap` (hierarchical clustering heatmap)

```python
corr = iris.corr()
sns.heatmap(corr, annot=True, fmt='.2f', square=True)

sns.clustermap(iris.select_dtypes('number'), metric='euclidean', method='average')
```

**Notes**: Good for showing variable correlation structures or distance matrices.

## F. Pairwise relationships

* `pairplot` (quick pairs), `PairGrid` (customizable)
* `jointplot`, `JointGrid` for bivariate + marginal distributions

```python
sns.pairplot(iris, hue="species", corner=True)

sns.jointplot(data=iris, x="sepal_length", y="sepal_width", kind="hex")
```

**When to use**: exploratory data analysis to inspect pairwise relationships and marginal distributions.

---

# 4. Grids & figure-level plots: Faceting (8 min)

* `FacetGrid` is the core: map plotting functions across facets (rows, cols, hue).

```python
g = sns.FacetGrid(tips, col="time", row="smoker", margin_titles=True)
g.map(sns.scatterplot, "total_bill", "tip")
```

* `relplot`, `catplot`, `displot`, `lmplot`, `pairplot` are built-in figure-level functions that create and use a `FacetGrid` internally.

**Tips**: Use `sharex`/`sharey` to control axis sharing; use `col_wrap` to wrap many facets into rows.

---

# 5. Practical tips & common pitfalls (7 min)

**Figure-level vs Axes-level**

* If you need a single Axes in an existing figure (e.g., subplot layout with `plt.subplots()`), use axes-level functions and pass `ax=` or operate on `ax`.
* Use figure-level when you want seaborn to control the figure and produce faceted plots.

**Long vs Wide data**

* Prefer tidy (long) data. If your data is wide, use `pd.melt()` to reshape.

**Combining with Matplotlib**

```python
fig, ax = plt.subplots()
sns.boxplot(data=tips, x="day", y="total_bill", ax=ax)
ax.set_title("Total bill by day")
```

**Controlling aesthetics**

* `sns.set_theme()` is recommended.
* Use `palette` argument for color control.
* Use `legend`/`ax.legend()` to relocate or format legends.

**Performance**

* For large datasets, use `alpha`, `s`, or hex/bin plots: `sns.histplot(..., bins=100, pthresh=0.05, cmap='mako')` or `kind='hex'` in `jointplot`.

**Statistical interpretation**

* Know what `estimator` and `ci` mean in `barplot`/`pointplot` — defaults are `mean` and bootstrapped 95% CI.

---

# 6. Mini exercises (5 min explanation, student time can follow outside this lecture)

**Exercise 1 (Exploration, 15–30 min)**

* Use `penguins` or `tips` data.
* Produce a `pairplot` colored by species/sex.
* Identify interesting pairwise correlations and summarise them in 5 bullets.

**Exercise 2 (Figure composition)**

* Create a figure with 2x2 subplots. Top-left: `heatmap` of correlations for numeric variables. Top-right: `boxplot` by category. Bottom row: `scatterplot` with regression line.
* Export as PNG and add titles and axis labels.

**Exercise 3 (Communication)**

* Given `tips`, make a single publication-quality figure that shows how `tip` varies by `day` and `time`, and includes raw points (jitter), a violin or box for distribution, and a summary stat (mean) as points.

---

# 7. Useful functions & quick reference (cheat sheet)

**Relational**: `scatterplot`, `lineplot`, `relplot`

**Categorical**: `catplot`, `boxplot`, `violinplot`, `barplot`, `countplot`, `stripplot`, `swarmplot`, `pointplot`

**Distribution**: `histplot`, `kdeplot`, `ecdfplot`, `displot`

**Regression**: `regplot`, `lmplot`

**Pairwise / Joint**: `pairplot`, `PairGrid`, `jointplot`, `JointGrid`

**Matrix**: `heatmap`, `clustermap`

**Utilities**: `load_dataset`, `set_theme`, `color_palette`, `palplot`, `despine`

---

# 8. Further reading & resources (links you can include in repo)

* Official documentation & gallery (seaborn.pydata.org) — gallery is excellent for examples.
* Seaborn API reference pages (look up each function above).
* Practical tutorials: Jake VanderPlas' chapters on visualization; statistical visualization sections in Python data science books.

---

# 9. Appendix: Example code snippets (copy/paste friendly)

```python
# Quick exploratory EDA
import seaborn as sns
sns.set_theme(style='whitegrid')

# 1. Pairplot
sns.pairplot(sns.load_dataset('iris'), hue='species')

# 2. Faceted scatter
sns.relplot(data=sns.load_dataset('tips'), x='total_bill', y='tip', col='day', hue='sex')

# 3. Combined categorical plot
ax = sns.violinplot(data=tips, x='day', y='total_bill', inner=None)
sns.stripplot(data=tips, x='day', y='total_bill', color='k', size=3, jitter=True, ax=ax)

# 4. Heatmap of correlations
import numpy as np
corr = sns.load_dataset('penguins').select_dtypes('number').corr()
sns.heatmap(corr, annot=True, cmap='vlag')
```

[Next: Colour theory](colour_theory.md)