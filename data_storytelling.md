# Data storytelling and communication

This module focuses on the principles and practices of effective data storytelling and communication, with an emphasis on multivariate visualisation, ethical considerations, and practical coding skills.

- [Nice slides](https://github.com/neelsoumya/visualization_lecture/blob/main/slides/Mastering_Data_Storytelling.pptx)


- [Slides](https://github.com/neelsoumya/visualization_lecture/blob/main/slides/data_storytelling_slides.pptx)



### 1. Principles of data storytelling
* **Reading:** *Data Storytelling: The Essential Data Science Skill Everyone Needs* by Brent D
* **Link:** [https://www.forbes.com/sites/brentdykes/2019/04/29/data-storytelling-the-essential-data-science-skill-everyone-needs/](https://www.forbes.com/sites/brentdykes/2019/04/29/data-storytelling-the-essential-data-science-skill-everyone-needs/)
* **Activities:** Analyze a dataset and create a narrative that highlights key insights using visualisations.

### 2. Multivariate visualisation techniques
* **Lecture + reading:** *Fundamentals of Data Visualization* by Claus O. Wille
* **Link:** [https://clauswilke.com/dataviz/](https://clauswilke.com/dataviz/)
* **Activities:** Create multivariate plots (e.g., scatterplot matrices, parallel coordinates) using R or Python.

### 3. Ethical considerations in data visualization
* **Reading:** *The Ethics of Data Visualization* by Alberto Cairo

* [National Geographic article VERY GOOD](https://www.nationalgeographic.com/adventure/article/151016-data-points-alberto-cairo-interview)

* **Link:** [https://www.ted.com/talks/alberto_cairo_the_ethics_of_data_visualization](https://www.ted.com/talks/alberto_cairo_the_ethics_of_data_visualization)
* **Activities:** Critique visualisations for ethical issues and misleading representations.

### 4. Practical coding skills for data storytelling
* **Tutorials:** R (ggplot2, plotly) or Python (matplotlib, seaborn)
* **Activities:** Hands-on coding sessions to create interactive visualisations and dashboards for storytelling.


## More resources

Data storytelling is the bridge between raw data analysis 📊 and meaningful action. While **exploratory** data analysis is about finding the signal in the noise, **explanatory** storytelling is about presenting that signal to stakeholders in a way that is clear, persuasive, and memorable.

Think of your data as the "facts" of a case. Without a narrative 📖, those facts are just a list. Storytelling provides the "argument" that tells the stakeholders why those facts matter to their specific business goals.


1. **The Narrative Structure**: Learning how to frame a data presentation using classic storytelling techniques like the "Context-Complication-Resolution" 📉 framework.
2. **Visual Hierarchy and De-cluttering**: Using Python libraries like **Matplotlib** and **Seaborn** to remove "chart junk" and direct the stakeholder's eye to the most important data points.
3. **The "So What?" Factor**: Developing exercises that teach students how to translate technical metrics (like p-values or R-squared) into business impacts (like revenue or customer churn).


## Narrative structure

Narrative structure transforms a series of charts into a compelling argument. Instead of just showing data, we use a story arc to lead stakeholders through a journey of discovery. A classic framework for this is the **Context-Complication-Resolution** model.

* **Context 🌍**: Establishing the baseline. For example, "Our app has 10,000 monthly active users and has grown steadily for a year."
* **Complication ⚠️**: The pivot point or "inciting incident" found in the data. "However, in the last two months, retention for new users has dropped by 20%."
* **Resolution ✅**: The data-driven path forward. "Our analysis shows that a specific onboarding friction point is the cause; fixing it could recover $50k in monthly revenue."

Let's decide where to go next to build these resources for your students:

1. **The Storytelling Arc Frameworks**: We can dive into specific models like **Freytag's Pyramid** or the **Action-Result** framework and how to map specific data findings to each narrative stage.
2. **Coding the Narrative**: We can explore how to use Python tools like **Jupyter Notebooks** or **Streamlit** to structure a report so the text and code work together to tell a story rather than just displaying output.
3. **The "Find the Hero" Exercise**: We can design a hands-on Python exercise where students take a raw dataset (like sales or churn data) and must identify the "Villain" (the problem) and the "Hero" (the proposed solution) using visualizations.

## 🎮🛠️ Exercise

This exercise is designed to shift students from "making charts" to "building a case." By framing data points as characters, they learn to highlight the tension (the problem) and the resolution (the recommendation).

### Exercise Title: "The Churn Chronicles: Defeating the Silent Killer"

In this scenario, students act as Lead Data Analysts for **Stream-It**, a fictional video streaming service. Recent reports show a dip in revenue, and it’s their job to find the "Villain" causing the loss and the "Hero" that will save the quarter.

---

### 1. The Setup (Student Instructions)

Your stakeholders are the Marketing and Product teams. They don't want a 50-page technical report; they want to know:

1. **Where are we losing money?** (The Villain)
2. **How do we stop it?** (The Hero)

#### The Dataset

Python code to generate a synthetic dataset with a hidden narrative:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate synthetic data
np.random.seed(42)
n_users = 1000
data = {
    'User_ID': range(n_users),
    'Subscription_Type': np.random.choice(['Basic', 'Premium', 'Family'], n_users),
    'Monthly_Charges': np.random.uniform(10, 30, n_users),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], n_users),
    'Churned': np.random.choice([0, 1], n_users, p=[0.7, 0.3]),
    'Customer_Support_Calls': np.random.poisson(2, n_users),
    'App_Engagement_Score': np.random.normal(50, 15, n_users)
}

df = pd.DataFrame(data)

# Inject the 'Villain': Higher churn for Basic users with high support calls
df.loc[(df['Subscription_Type'] == 'Basic') & (df['Customer_Support_Calls'] > 3), 'Churned'] = 1

# Inject the 'Hero': Users with high App_Engagement_Score almost never churn
df.loc[df['App_Engagement_Score'] > 70, 'Churned'] = 0

print(df.head())
```

---

### 2. The Task: Three Visual Chapters

Students must create three specific visualizations that tell the story:

#### Chapter 1: The Inciting Incident (The Villain)

**Goal:** Use a bar chart or heatmap to show that churn isn't happening everywhere—it’s concentrated.

* **Student Task:** Create a visualization comparing Churn Rates across `Subscription_Type` and `Customer_Support_Calls`.
* **The Finding:** "Basic" users with more than 3 support calls are abandoning ship at an alarming rate. This is the **Villain**.

#### Chapter 2: The Stakes

**Goal:** Translate the data into business impact.

* **Student Task:** Calculate and visualize the potential **lost revenue** (Monthly_Charges * Churned).
* **The Finding:** "If we don't address the support issues for Basic users, we stand to lose $X,000 per month."

#### Chapter 3: The Hero’s Arrival

**Goal:** Find a segment that is succeeding and turn that insight into a recommendation.

* **Student Task:** Analyze the relationship between `App_Engagement_Score` and `Churned`.
* **The Finding:** Users with high app engagement stay loyal regardless of their subscription tier. The **Hero** is a new "Engagement Campaign" to get Basic users into the mobile app earlier.

---

### 3. Evaluation Criteria

Students should be graded not just on the code, but on their **annotations**.

* **Bad Annotation:** "Chart showing churn by engagement."
* **Storytelling Annotation:** "The Safety Net: Users with engagement scores above 70 are 90% more likely to renew."

---

### 4. Discussion Questions for the Class

* **The Perspective Shift:** How did your visualization change when you started thinking of "Basic users with high calls" as a Villain rather than just a data point?
* **Stakeholder Empathy:** If you were the Head of Marketing, which chart would make you want to sign off on a budget increase?


## Exercise Solution

This model solution focuses on **Explanatory Data Viz**. Instead of just showing the data, we are going to use "Active Titles" and annotations to guide the stakeholder’s eye.

Below is the Python code using **Seaborn** and **Matplotlib**. You can share this with your students as the "Goal" they should strive for.

---

### 🎮🛠️ The Data Preparation

First, we ensure the environment is set up and the "Villain" and "Hero" are baked into the data.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set the storytelling theme
sns.set_theme(style="white")
plt.rcParams['font.family'] = 'sans-serif'

# 1. Setup (Data Generation)
np.random.seed(42)
n_users = 1000
data = {
    'Subscription_Type': np.random.choice(['Basic', 'Premium', 'Family'], n_users),
    'Monthly_Charges': np.random.uniform(10, 30, n_users),
    'Customer_Support_Calls': np.random.poisson(2, n_users),
    'App_Engagement_Score': np.random.normal(50, 15, n_users),
    'Churned': np.random.choice([0, 1], n_users, p=[0.7, 0.3])
}
df = pd.DataFrame(data)

# Inject the 'Villain': High churn for Basic users with >3 support calls
df.loc[(df['Subscription_Type'] == 'Basic') & (df['Customer_Support_Calls'] > 3), 'Churned'] = 1
# Inject the 'Hero': High engagement prevents churn
df.loc[df['App_Engagement_Score'] > 75, 'Churned'] = 0

```

---

### Chapter 1: Identifying the Villain

**The Story:** We aren't losing everyone; we are specifically failing our Basic tier users who need help.

```python
# Create a pivot table for the heatmap
heatmap_data = df.groupby(['Subscription_Type', 'Customer_Support_Calls'])['Churned'].mean().unstack()

plt.figure(figsize=(10, 5))
sns.heatmap(heatmap_data, annot=True, cmap='Reds', fmt=".1f", cbar=False)

# Storytelling elements
plt.title("THE VILLAIN: Support Friction is Killing the 'Basic' Tier", fontsize=16, loc='left', pad=20)
plt.xlabel("Number of Customer Support Calls")
plt.ylabel("Subscription Plan")
plt.annotate('CRITICAL ZONE:\nBasic users with 4+ calls\nhave a 100% churn rate.', 
             xy=(5, 0.5), xytext=(7, 0.5),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()

```

---

### Chapter 2: Calculating the Stakes

**The Story:** This isn't just a "metric"—it is a direct hit to our monthly revenue.

```python
# Calculate lost revenue
lost_revenue = df[df['Churned'] == 1].groupby('Subscription_Type')['Monthly_Charges'].sum()

plt.figure(figsize=(8, 6))
ax = sns.barplot(x=lost_revenue.index, y=lost_revenue.values, palette=['#ff9999', '#cccccc', '#cccccc'])

# Storytelling elements
plt.title("THE STAKES: We are losing $1,800+ Monthly in 'Basic' alone", fontsize=16, loc='left', pad=20)
plt.ylabel("Potential Monthly Revenue Lost ($)")
plt.xlabel("Subscription Tier")
sns.despine()

# Add data labels
for p in ax.patches:
    ax.annotate(f'${p.get_height():.0f}', (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha = 'center', va = 'center', xytext = (0, 9), textcoords = 'offset points', fontweight='bold')
plt.show()

```

---

### Chapter 3: The Hero’s Arrival

**The Story:** High app engagement is our "shield." If we can move users into the app, the "Villain" (support friction) loses its power.

```python
plt.figure(figsize=(10, 6))
sns.kdeplot(data=df[df['Churned'] == 0], x='App_Engagement_Score', fill=True, label='Retained', color='teal')
sns.kdeplot(data=df[df['Churned'] == 1], x='App_Engagement_Score', fill=True, label='Churned', color='red')

# Storytelling elements
plt.title("THE HERO: High App Engagement is a Churn Vaccine", fontsize=16, loc='left', pad=20)
plt.axvline(75, color='green', linestyle='--')
plt.text(76, 0.02, "THE HERO ZONE:\nScores >75 = Zero Churn", color='green', fontweight='bold')
plt.legend()
sns.despine()
plt.show()

```

---

### Key Teaching Points for the Solution

1. **Decluttering**: Notice how we removed the top and right spines (`sns.despine()`) and removed the color bar from the heatmap to keep the focus on the data.
2. **Color with Intent**: We used **Red** for the Villain/Loss and **Teal/Green** for the Hero/Retention. This uses the stakeholder's existing mental models (Red = Bad, Green = Good).
3. **The "So What?"**: The titles aren't just labels like "Churn Rate by Tier." They are **conclusions**. A stakeholder could read only the titles and still understand the whole business case.


## Storyboarding

[Video by Scott Klemmer on storyboards](https://youtu.be/z4glsttyxw8?si=-oaFUFP8wTZRiz--)

- 🤔 comic strip: show flow, how does user figure in this?

- _star people_: how to draw people

- Sequence: what steps are involved?

- Helps get stakeholders on the same page.

- Here is an example of a storyboard

![story](images/storyboard.png)

- 🎮 [paper prototypes video and activity](https://youtu.be/z4glsttyxw8?si=yQvl2Hze_-pwovlN&t=417)

- Paper prototypes, transparencies and sticky notes

- Digital mockups

- High fidelity mockups (controlled experiments)


## 🎮 Exercise

Storyboarding for data visualization is like writing a script 📽️ before filming a movie. It helps us map out the **Sequence**—the logical flow of insights—so stakeholders don't get lost between charts. It moves the focus from "how do I code this?" to "what am I trying to say?"

In Python, we can simulate this "sketching" phase by having students create a **Story Skeleton**. Instead of rendering complex charts immediately, they define the "Panels" of their story using a data structure. This ensures the narrative holds up before they spend hours on formatting.

Here are three ways we could structure a Python-based storyboarding exercise:

1. **The Metadata Map 🗺️**: Students write a Python script that defines a `StoryFrame` class. They must "instantiate" 4-5 frames of their story, specifying the **Sequence**, the **Persona** (the "Star Person" 👤 viewing the data), and the **Key Takeaway**.
2. **The Skeleton Plotter 🦴**: Students use Matplotlib to create "Blank" plots. Instead of data, they use `plt.text()` to describe what the chart *will* show and where the annotations will go. This mimics the **Paper Prototype** 📝 approach.
3. **The Narrative Audit 📋**: Students take an existing set of charts and write a Python "wrapper" or function that prints out the transition logic between them (e.g., "Because we see [X] in Frame 1, we must investigate [Y] in Frame 2").


1. **The Metadata Map** (Focus on planning and personas)
2. **The Skeleton Plotter** (Focus on visual layout and placeholders)
3. **The Narrative Audit** (Focus on flow and transitions)

A **Narrative Audit** focuses on the "connective tissue" between your data visualizations. In storyboarding, this ensures that the transition from one chart to the next feels like a logical progression rather than a random jump.

Think of it like a comic strip 🎞️: if Panel A shows a character at home and Panel B shows them on Mars, the reader needs a "transition" panel (the rocket ship 🚀) to understand how they got there. In data, this means explaining why a specific insight in Chart 1 leads us to investigate the metric in Chart 2.

### Exercise: The "Logic Leap" Audit

In this exercise, students are given a Python script that generates three correct but disconnected charts. Their job is to perform an "audit" and write the narrative bridge that connects them.

---

### 1. The Setup (The Disconnected Code)

Provide students with this "broken" narrative. The charts are technically fine, but the story is missing.

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Sample Data: Website Traffic and Sales
data = pd.DataFrame({
    'Day': range(1, 8),
    'Visitors': [1000, 1100, 1050, 1200, 1500, 1600, 1550],
    'Bounce_Rate': [40, 42, 41, 39, 65, 68, 70],
    'Conversion_Rate': [5, 5, 4.8, 5.2, 2.1, 1.8, 1.5]
})

def plot_narrative_gap():
    # Chart 1: Traffic is growing
    plt.figure(figsize=(5, 3))
    sns.lineplot(data=data, x='Day', y='Visitors', marker='o')
    plt.title("Total Website Visitors")
    plt.show()

    # Chart 2: Bounce rate spiked
    plt.figure(figsize=(5, 3))
    sns.lineplot(data=data, x='Day', y='Bounce_Rate', color='red')
    plt.title("Bounce Rate Percentage")
    plt.show()

    # Chart 3: Conversion dropped
    plt.figure(figsize=(5, 3))
    sns.barplot(data=data, x='Day', y='Conversion_Rate')
    plt.title("Sales Conversion Rate")
    plt.show()

plot_narrative_gap()

```

---

### 2. The Student Task: The Transition Script

Students must create a Python dictionary called `narrative_audit`. For each transition, they must identify:

1. **The Observation**: What did we just see?
2. **The Question**: What does this make us wonder?
3. **The Transition**: How does the next chart answer that question?

#### Example Structure for Students:

```python
narrative_audit = {
    "Transition_1_to_2": {
        "Observation": "Traffic is hitting record highs in the second half of the week.",
        "The Question": "Is this high-volume traffic actually high-quality traffic?",
        "Bridge": "To find out, we need to look at the **Bounce Rate** to see if people are sticking around."
    },
    "Transition_2_to_3": {
        "Observation": "Bounce rates nearly doubled as traffic increased.",
        "The Question": "How did this inability to retain users impact our bottom line?",
        "Bridge": "We will now examine **Conversion Rates** to quantify the cost of this technical friction."
    }
}

```

---

### 3. Grading the "Flow"

Instead of checking if the code runs, you are checking for **Causality**.

* **Weak Flow**: "Here is traffic. Next, here is bounce rate."
* **Strong Flow**: "While traffic is up, the bounce rate suggests we are attracting the wrong audience, which leads to the drop in conversions we see here."

How do you think your students would react to critiquing "broken" stories like this versus building their own from scratch? Would they find it easier to spot logic gaps in someone else's work first?


## A bad diagram (how not to communicate)

![Complex diagram](images/complex_diagram.png)

- 🥳 2 experts might figure it out, but the rest of the 8 billion people? 

- As shown in the figure below, overly complex visuals can fail to communicate outside a small expert audience.


# 🎮💡🛠️ Exercise (social media harm)

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

## AI prototyping tools

- Lovable

- Replit

- Cursor

- Google AI studio

- Base44


## Reading Materials

- [The User Experience](http://www.jjg.net/elements/pdf/elements_ch02.pdf
): A detailed look at the components of user experience design.


- [Next: Succinct plots](succinct_plots.md)
