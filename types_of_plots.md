# Types of plots

- [Types of plots](https://www.atlassian.com/data/charts/how-to-choose-data-visualization)

# Visualization Cheatsheet — Chart Types

A concise reference for undergraduate students summarizing common chart types, when to use them, what they show, and quick best-practice tips.

---

# Overview

Visualizations help turn data into insight. Choosing the right chart depends on: the question you want to answer (task), the types of variables you have (quantitative vs categorical vs temporal vs geographic), and your audience. Common roles for visualizations include:

* Showing change over time
* Showing part–to–whole composition
* Showing distributions
* Comparing values between groups
* Observing relationships between variables
* Mapping geographic data

---

# Quick reference table

| Chart type             |                          Primary use | Data type / encoding                  | When to prefer it                                              |
| ---------------------- | -----------------------------------: | ------------------------------------- | -------------------------------------------------------------- |
| Line chart             |                     Change over time | Time (x) → numeric (y)                | Continuous trends, multiple series                             |
| Bar chart              |                   Compare categories | Categorical → numeric                 | Ranked comparisons, discrete categories                        |
| Grouped / stacked bar  |  Compare subgroups or parts of whole | Categorical × categorical             | Compare groups or show composition across categories           |
| Histogram              | Distribution of one numeric variable | Numeric → bins                        | Explore shape, skew, outliers                                  |
| Density plot           |                Smoothed distribution | Numeric                               | When you want a smooth estimate                                |
| Box plot               |               Summarize distribution | Numeric by group                      | Compare medians, spread, outliers                              |
| Violin plot            |      Distribution + density by group | Numeric by group                      | Show distribution shape per group                              |
| Scatter plot           |   Relationship between two variables | Numeric × numeric                     | Correlation, clusters, outliers                                |
| Bubble chart           |          Scatter with third variable | Numeric × numeric + size/color        | Add magnitude to scatter points                                |
| Heatmap                |                Matrix or 2-D density | Two categorical / binned numeric axes | Show intensity across a grid                                   |
| Choropleth / Cartogram |                  Geographic patterns | Region → numeric                      | Map-based comparisons                                          |
| Area chart             |              Part-to-whole over time | Time with stacking                    | Emphasize totals and composition (use carefully)               |
| Pie / Donut            |                 Simple part-to-whole | Categorical proportions               | Only for few categories and when exact comparison not required |
| Treemap / Marimekko    |          Hierarchical or composition | Hierarchy → area                      | Many subparts, space-limited views                             |
| Candlestick / OHLC     |                Financial time series | Time → open/high/low/close            | Price movements in trading data                                |
| Funnel chart           |                   Process conversion | Ordered stages                        | Conversion/drop-off visualization (marketing, UX)              |
| Parallel coordinates   |              Multivariate comparison | Many numeric attributes               | Observe patterns across many variables                         |
| Dumbbell / Slope chart |                Two-point comparisons | Category → two numeric points         | Show change between two timepoints or conditions               |
| Bullet chart           |                 Compare to benchmark | Numeric with target                   | Compact KPI vs target display                                  |

---

# Short descriptions & classroom tips

## Line chart

* **What:** Points connected by lines (time on x-axis).
* **Use when:** Visualizing trends, seasonality, and multiple series.
* **Tip:** Keep series to a readable number (≤ 6). Use small multiples when there are many series.

## Bar chart (including grouped & stacked)

* **What:** Rectangles whose heights encode value.
* **Use when:** Comparing values across categories. Grouped bars compare subgroups; stacked bars show part–to–whole.
* **Tip:** Avoid stacked bars when precise comparison of subparts is needed; use grouped bars or small multiples.

## Histogram & Density plot

* **What:** Histogram bins numeric data; density smooths it.
* **Use when:** Inspecting distribution shape, skew, modality.
* **Tip:** Show both histogram and density overlay in teaching exercises; discuss bin width effects.

## Box plot & Violin plot

* **What:** Box shows median, IQR, whiskers; violin shows density shape.
* **Use when:** Comparing distributions across groups.
* **Tip:** Use box plots for concise comparison and violins when distribution shape matters.

## Scatter & Bubble charts

* **What:** Plot points for pairs of values; bubble adds size (third var).
* **Use when:** Exploring correlations, clusters, heteroskedasticity.
* **Tip:** Avoid bubbles when size comparisons are critical (perceptual issues); consider log scales for skewed axes.

## Heatmap

* **What:** Grid colored by value.
* **Use when:** Showing two-dimensional intensity (e.g., correlation matrices, 2-D histograms).
* **Tip:** Cluster rows/columns to reveal structure.

## Choropleth & Cartogram

* **What:** Map regions colored (choropleth) or resized (cartogram) to encode values.
* **Use when:** Spatial comparisons (population, rates).
* **Tip:** Normalize by population for rates; beware of small-area visual bias.

## Area & Stacked area

* **What:** Line chart with filled area under the curve; stacking shows composition.
* **Use when:** Emphasize totals and contributions over time.
* **Tip:** Stacked areas can hide trends for smaller series—use carefully.

## Pie & Donut charts

* **What:** Circle divided into slices.
* **Use when:** Very small number of categories and audience prefers simple proportion visuals.
* **Tip:** Prefer bar charts for precise comparisons; avoid many slices.

## Treemap & Marimekko

* **What:** Nested rectangles sized by value.
* **Use when:** Represent hierarchical composition or many categories in limited space.
* **Tip:** Order and labels matter—interactive hover helps.

## Specialized charts (Candlestick, Funnel, Bullet, Parallel coordinates)

* **What:** Domain-specific; good to introduce as examples of targeted visualization.
* **Use when:** Financial time series (candlesticks), conversion flows (funnels), benchmark comparisons (bullet), and multivariate patterns (parallel coords).

---

# Best-practice checklist (short)

* Use the simplest chart that answers the question.
* Label axes and include units. Provide a clear title and a short caption.
* Use perceptually effective encodings (position > length > angle > area > color hue).
* Limit categories and series shown at once; use small multiples for scale.
* Consider accessibility: colorblind-safe palettes, high contrast, descriptive alt text.
* Annotate important values or outliers; use direct labeling when possible.
* Avoid 3D effects unless they add genuine information.

---

# Suggested classroom exercises

1. **Pick the right chart:** Give the same dataset and three analysis questions; students pick and justify a chart for each question.
2. **Tufte reflection:** Ask students to rework a messy dashboard to follow Tufte’s principles (minimize ink, maximize data-ink ratio).
3. **Perception lab:** Compare bar vs pie vs donut for the same proportions and test which students estimate most accurately.
4. **Small multiples:** Students create small-multiple line charts to compare dozens of time series.

---

# Further reading / resources

* Edward Tufte — *The Visual Display of Quantitative Information*


- [Next: Seaborn overview](seaborn.md)

