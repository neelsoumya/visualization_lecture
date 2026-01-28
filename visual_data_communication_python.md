<!-- File: 01_python_basics.md -->

<!--
# 01_python_basics.md
-->

# Python Basics and Data Handling

## Functions and objects

In programming, **functions** perform specific operations, taking inputs (arguments) and returning values.

For example, in Python you can call built-in functions like `math.sqrt(9)` or `round(10.232, 1)`, which return numerical results.

To store values we assign them to **variables** (Python’s equivalent of R “objects”). For instance:

```python
age = 21
print(age)        # Outputs: 21
double_age = age * 2
```

This mirrors R’s assignment (`age <- 21`) but uses `=` in Python. Python supports various data types (numbers, strings, booleans) similar to R. Strings must be in quotes (`"text"`), and booleans are `True` / `False`. Like R’s `NA`, Python uses `None` for missing values (handled carefully in computations).

---

## Basic data structures

Common Python data structures: lists, dictionaries, and `pandas.DataFrame` for tabular data (similar to R’s `data.frame` / tibble). A `DataFrame` lets you work with columns and rows.

Example — read a CSV of Darwin’s finch measurements:

```python
import pandas as pd

finches = pd.read_csv("data/finches.csv")
print(finches.head())
```

A DataFrame will have columns like `species`, `weight`, etc. Inspect the first few rows with `finches.head()`. Pandas automatically infers data types (numeric, string, etc.), similar to R’s tibble output.

---

## Subsetting data

Select columns using bracket notation:

```python
subset = finches[['group', 'wing']]
print(subset.head())
```

Filter rows using boolean indexing. Example — keep only species `G. fortis`:

```python
fortis = finches[finches['species'] == "G. fortis"]
print(fortis.shape)   # e.g., (89, 12)
```

Filter by numeric condition:

```python
heavy = finches[finches['weight'] > 18]
```

Chaining (filter then select) with `.loc`:

```python
result = finches.loc[finches.weight > 18, ['species','weight']]
```

This corresponds to R’s pipe-based workflows (e.g. `finches %>% filter(weight > 18) %>% select(species, weight)`).

---

## Exercises

- **Exercise:** Read `finches.csv` with pandas. Print the first 5 rows.
- **Exercise:** In the DataFrame, create a new column `weight_kg = weight / 1000`. Verify it by displaying the columns and first few rows.

---

---

<!-- File: 02_data_wrangling.md -->
# 02_data_wrangling.md

# Document 2 — Data Wrangling with Pandas

## Adding and rearranging columns

Add or transform columns:

```python
finches['weight_kg'] = finches['weight'] / 1000
```

Reorder columns (example: move `weight_kg` so it sits right after `weight`):

```python
cols = list(finches.columns)
cols.insert(cols.index('weight')+1, cols.pop(cols.index('weight_kg')))
finches = finches[cols]
```

This mimics R’s `mutate()` and `relocate()` patterns.

---

## Grouping and summarising (split–apply–combine)

Count observations per species:

```python
counts = finches.groupby('species').size().reset_index(name='count')
print(counts)
```

Summary statistics (mean/median/min/max) per species:

```python
summary = finches.groupby('species')['weight'].agg(['mean','median','min','max']).reset_index()
summary.columns = ['species','avg_weight','median_weight','min_weight','max_weight']
print(summary)
```

---

## Reshaping data (wide vs long)

Count by `species` and `group`:

```python
counts = finches.groupby(['species','group']).size().reset_index(name='n')
print(counts.head(6))
```

Pivot to wide format:

```python
finches_wide = counts.pivot(index='species', columns='group', values='n').reset_index()
print(finches_wide)
```

---

## Exporting data

Save transformed results:

```python
finches_wide.to_csv("data/finches_wide.csv", index=False)
```

---

## Exercises

- **Exercise:** Using the `finches` DataFrame, group by `species` and compute the average and standard deviation of `wing`.
- **Exercise:** Reshape that result so each species has its own row and the standard deviation per species appears in a column.

---

---

<!-- File: 03_basic_visualization.md -->
# 03_basic_visualization.md

# Document 3 — Basic Data Visualization with Python

> Use `matplotlib` + `seaborn` for static plots; `plotly` for interactive variants when desired.

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data (assumes the finches DataFrame is available)
finches = pd.read_csv("data/finches.csv")
```

---

## Scatter plots

Explore relationships between two numeric variables (example: beak depth vs beak length):

```python
sns.scatterplot(data=finches, x='bdepth', y='blength')
plt.title("Finch beak length vs depth")
plt.show()
```

Color by categorical variable (e.g. `species`):

```python
sns.scatterplot(data=finches, x='bdepth', y='blength', hue='species', alpha=0.7)
```

- 💡 _Hint_ Use `alpha` to reduce overplotting.

---

## Line plots

Good for ordered/time data:

```python
# Example assumes a 'year' column exists
sns.lineplot(data=finches, x='year', y='weight', hue='species')
plt.title("Finch weight over years")
plt.show()
```

---

## Box plots (and overlaid points)

Visualise distributions by category:

```python
sns.boxplot(data=finches, x='species', y='weight')
sns.stripplot(data=finches, x='species', y='weight', color='blue', jitter=0.1, alpha=0.6)
plt.show()
```

---

## Histograms

Frequency distribution of a single variable:

```python
sns.histplot(data=finches, x='bdepth', bins=10)
plt.show()
```

---

## Exercises

- **Exercise:** Create a box plot of `weight` by `group` (e.g., `"early_blunt"`, `"late_pointed"`, etc.) for `G. scandens` only. Overlay the individual data points in a different color.
- **Exercise:** Plot a histogram of `bdepth` for finches recorded after 1983. Try different numbers of bins and comment on how the histogram shape changes.

---

---

<!-- File: 04_correlations_multivariate.md -->
# 04_correlations_multivariate.md

# Document 4 — Exploring Correlations and Multivariate Plots

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load gapminder-like data
gap = pd.read_csv("data/gapminder_clean.csv")
```

---

## Scatter with colour & size (bubble plots)

Example: life expectancy vs income per person:

```python
sns.scatterplot(data=gap, x='income_per_person', y='life_expectancy', hue='world_region')
plt.title("Life expectancy vs Income per person")
plt.show()
```

- Map population to point size (normalize first):

```python
sizes = (gap['population'] - gap['population'].min()) / (gap['population'].max() - gap['population'].min())
sns.scatterplot(data=gap, x='income_per_person', y='life_expectancy', hue='world_region', size=sizes, sizes=(20,200), alpha=0.7)
plt.show()
```

---

## Correlation matrix heatmap

```python
numeric_cols = gap.select_dtypes(include='number').drop(columns=['year'])
corr_matrix = numeric_cols.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title("Correlation matrix (Pearson)")
plt.show()
```

---

## Extreme values and boxplots

Find top and bottom 5 countries by income and compare:

```python
top5 = gap.nlargest(5, 'income_per_person')
bot5 = gap.nsmallest(5, 'income_per_person')
combined = pd.concat([top5.assign(Group='Top 5'), bot5.assign(Group='Bottom 5')])
sns.boxplot(data=combined, x='Group', y='income_per_person')
plt.title("Income per person: Top 5 vs Bottom 5 countries")
plt.show()
```

---

## Exercises

- **Exercise:** In the gapminder data, plot `life_expectancy` vs `income_per_person` with `hue='main_religion'`. Do you see any patterns? *(Hint: try a log scale on the x-axis: `plt.xscale('log')`.)*
- **Exercise:** Compute the 5 countries with highest and lowest `income_per_person`. Create a bar chart or box chart comparing their life expectancy distributions.

---

---

<!-- File: 05_ranking_design.md -->
# 05_ranking_design.md

# Document 5 — Ranking, Ordering, and Design in Plots

```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

gap = pd.read_csv("data/gapminder_clean.csv")
```

---

## Ordering categories

Order regions by descending average income:

```python
mean_income = gap.groupby('world_region')['income_per_person'].mean().sort_values()
ordered_regions = mean_income.index.tolist()
gap['world_region'] = pd.Categorical(gap['world_region'], categories=ordered_regions, ordered=True)

sns.barplot(data=gap, x='world_region', y='income_per_person', estimator=np.mean)
plt.xticks(rotation=45)
plt.title("Average income per region (ordered)")
plt.show()
```

---

## Stem (lollipop) plots

```python
MEA = gap[gap.world_region == "middle_east_north_africa"].sort_values(by='income_per_person')
plt.figure(figsize=(8,6))
plt.hlines(y=MEA['country'], xmin=0, xmax=MEA['income_per_person'], color='gray', alpha=0.7)
plt.plot(MEA['income_per_person'], MEA['country'], "o")
plt.title("Income per person: Middle East & N. Africa")
plt.xlabel("Income per person")
plt.show()
```

---

## Design principles — “Grey is great”

Use _grey_ to de-emphasise background data and highlight focal elements. Strategies:

- Plot background lines/points in grey with higher transparency (`alpha`).
- Overlay the primary series in a bold color.
- Reduce or remove non-essential gridlines and heavy borders.
- Use clear legends and concise annotations.
- Avoid chartjunk — keep the visual message clear.

---

## Exercises

- **Exercise:** Using `gapminder_clean.csv`, reorder the x-axis of a bar plot of `income_per_person` by region from highest to lowest. Then produce a bar plot of `children_per_woman` for countries in Europe, ordered descending by value.
- **Exercise:** Create a lollipop chart for the countries in “Europe & Central Asia”, showing `children_per_woman` with countries ordered by that value.

---

# References

- Concepts adapted from: Visual Data Communication (Cambio Training)[https://cambiotraining.github.io/visual-data-communication/]

- [Next: Edward Tufte's principles of visualization](lecture_tufte.md)
