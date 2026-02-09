'''
Docstring for exercises.retail_plots
### Teaching Tips for Students:

1. **Wide vs. Long Format**: Emphasize the `melt()` function. Most plotting libraries (like Seaborn) prefer "Long" (tidy) data, but data is often provided in "Wide" format (one column per month).
2. **Handling Missing Data**: Point out that real-world data uses symbols like 'S' for suppression or 'NA'. Using `pd.to_numeric(..., errors='coerce')` is a vital trick for converting these to values Python can plot.
3. **NAICS Codes**: Briefly explain that these codes represent specific industries (e.g., 441 is Auto, 445 is Grocery). This adds "Domain Knowledge" to their technical skills.
4. **Baseline Awareness**: In growth charts, the  line is the most important reference point. Always encourage students to add a `plt.axhline(0)`.

'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('state_retail_yy.csv')

# Display basic info and first few rows
print(df.info())
print(df.head())


# Load the data
file_path = 'state_retail_yy.csv'
df = pd.read_csv(file_path)

# ---------------------------------------------------------
# PRE-PROCESSING (Common for all exercises)
# ---------------------------------------------------------
# The data contains 'S' for suppressed values. We need to convert 
# monthly columns to numeric and handle 'S' as NaN.
month_cols = [col for col in df.columns if col.startswith('yy')]
for col in month_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# ---------------------------------------------------------
# EXERCISE 1: The Impact of 2020 on Motor Vehicles
# Task: Filter the data for the USA (stateabbr == 'USA') and 
# 'Motor Vehicle and Parts Dealers' (naics == 441). 
# Create a line plot showing the growth trend from 2019 to 2025.
# ---------------------------------------------------------

print("Running Exercise 1...")

# SOLUTION
usa_auto = df[(df['stateabbr'] == 'USA') & (df['naics'] == '441')]
# Reshape from wide to long format
usa_auto_long = usa_auto.melt(id_vars=['stateabbr', 'naics'], 
                              value_vars=month_cols, 
                              var_name='Month', value_name='Growth')
# Convert Month string to datetime for better plotting
usa_auto_long['Date'] = pd.to_datetime(usa_auto_long['Month'].str.replace('yy', ''), format='%Y%m')

plt.figure(figsize=(12, 6))
plt.plot(usa_auto_long['Date'], usa_auto_long['Growth'], marker='o', linestyle='-', color='b')
plt.axhline(0, color='red', linewidth=1, linestyle='--') # Baseline
plt.title('USA Motor Vehicle & Parts Dealers: YoY Growth (2019-2025)')
plt.xlabel('Year')
plt.ylabel('YoY % Change')
plt.grid(True, alpha=0.3)
plt.savefig('exercise1_timeseries.png')
print("Saved: exercise1_timeseries.png")


# ---------------------------------------------------------
# EXERCISE 2: Comparing State Performance
# Task: Select three states (e.g., 'CA', 'TX', 'NY') and 
# compare their 'Food and Beverage' (naics == 445) retail growth 
# during the year 2021.
# ---------------------------------------------------------

print("Running Exercise 2...")

# SOLUTION
selected_states = ['CA', 'TX', 'NY']
target_months = [col for col in month_cols if '2021' in col]

states_df = df[(df['stateabbr'].isin(selected_states)) & (df['naics'] == '445')]
states_long = states_df.melt(id_vars='stateabbr', value_vars=target_months, 
                             var_name='Month', value_name='Growth')

plt.figure(figsize=(10, 6))
sns.barplot(data=states_long, x='Month', y='Growth', hue='stateabbr')
plt.title('Comparison of Food & Beverage Growth (2021)')
plt.xticks(rotation=45)
plt.ylabel('YoY % Change')
plt.legend(title='State')
plt.tight_layout()
plt.savefig('exercise2_comparison.png')
print("Saved: exercise2_comparison.png")


# ---------------------------------------------------------
# EXERCISE 3: Sector Growth Heatmap
# Task: Create a heatmap for the USA (stateabbr == 'USA') 
# showing the YoY growth of ALL naics sectors for the year 2022.
# ---------------------------------------------------------

print("Running Exercise 3...")

# SOLUTION
usa_2022 = df[df['stateabbr'] == 'USA']
months_2022 = [col for col in month_cols if '2022' in col]

# Prepare data for heatmap: Rows=NAICS, Columns=Months
heatmap_data = usa_2022.set_index('naics')[months_2022]

plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_data, annot=True, cmap='RdYlGn', center=0, fmt=".1f")
plt.title('USA Retail Sector Performance Heatmap (2022)')
plt.xlabel('Month')
plt.ylabel('NAICS Code')
plt.savefig('exercise3_heatmap.png')
print("Saved: exercise3_heatmap.png")


# ---------------------------------------------------------
# EXERCISE 4: Distribution of Growth (Boxplot)
# Task: Create a boxplot that shows the distribution of 
# growth rates across all 50 states for 'General Merchandise' 
# (naics == 452) for each month in 2023.
# ---------------------------------------------------------

print("Running Exercise 4...")

# SOLUTION
# Filter for General Merchandise and exclude the 'USA' aggregate
gen_merch = df[(df['naics'] == '452') & (df['stateabbr'] != 'USA')]
months_2023 = [col for col in month_cols if '2023' in col]

gen_merch_2023 = gen_merch.melt(id_vars='stateabbr', value_vars=months_2023, 
                                var_name='Month', value_name='Growth')

plt.figure(figsize=(12, 6))
sns.boxplot(data=gen_merch_2023, x='Month', y='Growth', color='lightblue')
plt.title('Distribution of General Merchandise Growth Across States (2023)')
plt.xticks(rotation=45)
plt.axhline(0, color='red', linestyle='--')
plt.ylabel('YoY % Change')
plt.savefig('exercise4_boxplot.png')
print("Saved: exercise4_boxplot.png")

print("\nAll exercises completed!")

