# Edward Tufte's recommendations for data visualization

Edward Tufte is a renowned expert in the field of data visualization and information design. His work emphasizes clarity, precision, and efficiency in presenting data. Here are some of his key recommendations for effective data visualization:
1. **Maximize Data-Ink Ratio**: Tufte advocates for minimizing non-essential ink in visualizations. This means removing any elements that do not convey important information, such as excessive gridlines, borders, or decorative graphics.
2. **Avoid Chartjunk**: He warns against "chartjunk," which refers to unnecessary or distracting elements in a chart that do not improve understanding. This includes things like 3D effects, excessive colors, and ornamental graphics.
3. **Use Small Multiples**: Tufte suggests using small multiples (a series of similar graphs or charts) to compare different datasets or variables. This allows viewers to easily see patterns and differences across multiple dimensions.
4. **Show Data Variation**: Instead of just showing averages or totals, Tufte encourages visualizations that display the full range of data variation. This can be done through techniques like scatter plots, box plots, or histograms.
5. **Integrate Text and Graphics**: Tufte emphasizes the importance of integrating text and graphics seamlessly. Annotations, labels, and explanations should be placed close to the relevant data points to enhance understanding.
6. **Use Clear and Simple Design**: Tufte advocates for a clean and simple design that prioritizes clarity. This includes using legible fonts, appropriate color schemes, and avoiding clutter.
7. **Focus on the Data Story**: Every visualization should tell a clear story about the data. Tufte encourages designers to think about the message they want to convey and to design their visualizations accordingly.
8. **Consider the Audience**: Understanding the audience's needs and level of expertise is crucial. Tufte advises tailoring visualizations to ensure they are accessible and meaningful to the intended viewers.


# Assignment based on Tufte's Principles

Using a dataset of your choice, create a data visualization that adheres to Edward Tufte's principles. Your visualization should:
1. Maximize the data-ink ratio by removing any non-essential elements.
2. Avoid chartjunk and focus on clarity.
3. Use small multiples if applicable to compare different aspects of the data.

# Another assignment based on Tufte's Principles

Choose a complex dataset and create a series of visualizations that:
1. Show data variation clearly, using appropriate chart types.
2. Integrate text and graphics effectively to enhance understanding.
3. Focus on telling a clear data story, tailored to your intended audience.


# Python Code Example (Tufte Style Visualization)

## Installation

- setup a virtual environment

```bash
python -m venv venv_viz
source venv_viz/bin/activate
```

- install the required packages 

```bash
pip install -r requirements.txt
```

## Code
- If you want to run the notebooks in Colab, you can also use the _Open in Colab_ badge below:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com)


- [Colab Notebook Link](https://github.com/neelsoumya/visualization_lecture/blob/main/tufte_python.ipynb)


```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Sample dataset
data = pd.DataFrame({
    'Category': np.repeat(['A', 'B', 'C'], 100),
    'Value': np.concatenate([np.random.normal(loc, 1, 100) for loc in [5, 10, 15]])
})

# Set Tufte style
sns.set_context("talk")
sns.set_style("white")

# Create a boxplot to show data variation
plt.figure(figsize=(8, 6))
sns.boxplot(x='Category', y='Value', data=data, hue='Category', palette='pastel', legend=False)
plt.title('Boxplot Showing Data Variation by Category', fontsize=16)
plt.xlabel('Category', fontsize=14)
plt.ylabel('Value', fontsize=14)
plt.grid(False)  # Remove gridlines for clarity
plt.show()
```

- This code creates a boxplot that adheres to Tufte's principles by maximizing the data-ink ratio, avoiding chartjunk, and clearly showing data variation.



# Time series data visualization example

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate sample time series data
dates = pd.date_range(start='2023-01-01', periods=100, freq='D')
np.random.seed(42) # for reproducibility
data_ts = pd.DataFrame({
    'Date': dates,
    'Value': np.cumsum(np.random.randn(100) * 5) + 100
})

# Set Tufte style context (already set, but good to include for standalone)
sns.set_context("talk")
sns.set_style("white")

plt.figure(figsize=(10, 6))

# Plot the time series data with minimal elements
plt.plot(data_ts['Date'], data_ts['Value'], color='darkblue', linewidth=1.5)

# Add a subtle horizontal line at the start value for context, if desired
# plt.axhline(y=data_ts['Value'].iloc[0], color='gray', linestyle='--', linewidth=0.7)

plt.title('Daily Trend of Value Over Time', fontsize=16, loc='left')
plt.xlabel('Date', fontsize=14)
plt.ylabel('Value', fontsize=14)

# Set y-axis to start from 0
plt.ylim(ymin=0)

# Remove top and right spines
sns.despine(left=True, bottom=True)

# Only show relevant x-axis and y-axis ticks/labels
# Keep the bottom spine for the date axis
plt.tick_params(axis='x', length=0)
plt.tick_params(axis='y', length=0)

# Add a grid, but make it very light and only on the y-axis for readability of values
plt.grid(axis='y', linestyle=':', alpha=0.5)

# Improve layout
plt.tight_layout()
plt.show()
```

# Advanced Tufte Visualizations

## Slopegraphs
Slopegraphs are excellent for comparing changes in rank or value between two time points for a list of items.

```python
import pandas as pd
import matplotlib.pyplot as plt

# Data
df_slope = pd.DataFrame({
    'Country': ['A', 'B', 'C', 'D', 'E'],
    '1990': [10, 30, 20, 50, 40],
    '2010': [15, 25, 40, 45, 60]
})

fig, ax = plt.subplots(figsize=(6, 8))
for i in range(len(df_slope)):
    ax.plot([1990, 2010], [df_slope.loc[i, '1990'], df_slope.loc[i, '2010']], color='black', marker='o', linewidth=1)
    ax.text(1990 - 2, df_slope.loc[i, '1990'], f"{df_slope.loc[i, 'Country']} {df_slope.loc[i, '1990']}", ha='right', va='center')
    ax.text(2010 + 2, df_slope.loc[i, '2010'], f"{df_slope.loc[i, '2010']} {df_slope.loc[i, 'Country']}", ha='left', va='center')

# Remove spines and axes
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.set_xticks([1990, 2010])
ax.set_yticks([])

ax.set_title("Slopegraph: Changes from 1990 to 2010", loc='left')
plt.show()
```

## Sparklines
Sparklines are word-sized graphics embedded in text, providing a high-resolution view of data without chartjunk.

See `verify_tufte.py` for an example.

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
data_spark = np.cumsum(np.random.randn(50))
fig, ax = plt.subplots(figsize=(4, 0.5))
ax.plot(data_spark, color='blue', linewidth=1)
ax.plot(len(data_spark)-1, data_spark[-1], marker='o', color='red', markersize=3)
ax.axis('off')
plt.show()
```

# Assignments

## Assignment 3: The Redesign Challenge
Find a visualization (from news media or a report) that violates Tufte's principles (low data-ink, chartjunk).
1. Critique it using Tufte's vocabulary.
2. Write Python code to redesign it into a cleaner, more effective visualization (e.g., a slopegraph or small multiple).
3. Calculate the Lie Factor if applicable.

## Assignment 4: Lie Factor Calculation
Calculate the Lie Factor for a misleading chart:
$$ \text{Lie Factor} = \frac{\text{Size of effect shown in graphic}}{\text{Size of effect in data}} $$



