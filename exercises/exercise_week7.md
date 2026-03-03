# 🎮🛠️ Exercise on interactive visualizations and visual storytelling (Superintelligence)  

- We show how to create interactive visualizations

- How to bridge the gap between abstract technical concepts and data-driven storytelling? Below is a structured exercise designed for a Python-based data visualization class.

- Reading [Michale Nielsen superintelligence risk](https://michaelnotebook.com/whichfuture/index.html)

- [Blog post on superintelligence](https://neelsoumya.github.io/policy/agi_harms_benefits.html)

---

## Exercise: The Velocity Gap – A Narrative Data Storytelling Challenge

### **Objective**

In this exercise, you will use Python to model a speculative future. You will generate synthetic data representing the growth of AI benefits versus AI harms, constrained by "Institutional Inertia." Your goal is to create a compelling visualization and a 300-word narrative that explains the "Velocity Gap" to a non-technical audience.

---

### Interactive Python simulator

Open the following code in a [Google Colab notebook](https://colab.research.google.com/drive/1Eo7oF2T7fBJrbfQ2P1M2XCJhqQu-8RwL?usp=sharing)

or in a standalone python script.

This uses `ipywidgets`.

```bash
python -m venv venv_viz
source activate venv_viz
pip install matplotlib numpy ipywidgets plotly
```

```python
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
from ipywidgets import interact, widgets

def plot_velocity_gap(harm_growth, benefit_ceiling, inst_speed, policy_lag):
    time = np.linspace(0, 25, 250)
    
    # Models
    y_harm = 0.5 * np.exp(harm_growth * time)
    midpoint = 10 + policy_lag
    y_benefit = benefit_ceiling / (1 + np.exp(-inst_speed * (time - midpoint)))
    
    # Calculate Risk Score (Area between curves)
    risk_score = np.trapz(np.maximum(0, y_harm - y_benefit), time)
    
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(time, y_harm, color='red', lw=2, label='Harmful AI Potential')
    plt.plot(time, y_benefit, color='blue', lw=2, label='Realized AI Benefits')
    
    # Fill the gap
    plt.fill_between(time, y_benefit, y_harm, where=(y_harm > y_benefit), 
                     color='red', alpha=0.1, label='The Velocity Gap')
    
    # Formatting
    plt.title(f"AI Velocity Gap | Cumulative Risk: {risk_score:.2f}", fontsize=14)
    plt.xlabel("Years from AGI Emergence")
    plt.ylabel("Impact Magnitude")
    plt.ylim(0, min(max(y_harm)*1.1, 300))
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    
    plt.show()

# Interactive Sliders
interact(
    plot_velocity_gap,
    harm_growth = widgets.FloatSlider(value=0.25, min=0.1, max=0.4, step=0.01),
    benefit_ceiling = widgets.IntSlider(value=50, min=10, max=100, step=5),
    inst_speed = widgets.FloatSlider(value=0.4, min=0.1, max=1.0, step=0.05),
    policy_lag = widgets.IntSlider(value=0, min=-5, max=10, step=1)
);
```

### **Part 1: The Synthetic Data Generator**

Use the following Python script to generate your dataset. This script simulates two trajectories:

1. **"Harmful AI Potential"**: Exponential growth driven by rapid, unregulated code deployment.
2. **"Realized AI Benefits"**: Logistic (S-curve) growth, representing the friction of policy, safety trials, and human consensus.

```python
import pandas as pd
import numpy as np

def generate_ai_narrative_data(years=20, seed=42):
    np.random.seed(seed)
    time = np.linspace(0, years, 100)
    
    # Scenario A: Exponential Harm (unregulated)
    # Grows at 30% annually
    harm_trajectory = 0.5 * np.exp(0.25 * time) + np.random.normal(0, 1, 100).cumsum() * 0.2
    
    # Scenario B: Sluggish Benefits (Institutional Friction)
    # Logistic growth: starts strong, but hits the 'Consensus Ceiling'
    L = 15 # Maximum realized benefit
    k = 0.4 # Growth rate
    x0 = 10 # Midpoint of adoption
    benefit_trajectory = L / (1 + np.exp(-k * (time - x0))) + np.random.normal(0, 0.2, 100)
    
    df = pd.DataFrame({
        'Year': 2024 + time,
        'Harmful_Potential': np.maximum(0, harm_trajectory),
        'Realized_Benefits': np.maximum(0, benefit_trajectory)
    })
    return df

# Students: Start your analysis here
df = generate_ai_narrative_data()
print(df.head())

```

---

### **Part 2: The Scenarios**

Choose one of the following "Institutional Environments" to model. Adjust the parameters in the code (or manually perturb the data) to reflect your chosen story:

* **Scenario 1: "The Great Stagnation"** – Policy becomes so gridlocked that the `Realized_Benefits` curve plateaus early (at $L=5$), while `Harmful_Potential` accelerates.
* **Scenario 2: "The Alignment Sprint"** – A global treaty is signed in year 10. The `Harmful_Potential` curve should show a sudden "kink" or drop, while `Realized_Benefits` continues its slow climb.
* **Scenario 3: "The Double-Edged Sword"** – Both curves are identical for 10 years, then diverge sharply as an ASI (Artificial Superintelligence) is reached.

---

### **Part 3: The Narrative Visual Task**

Your submission must include a single, publication-quality plot created with `Matplotlib`, `Seaborn`, or `Plotly` that adheres to the following storytelling principles:

1. **Visual Hierarchy:** Use color to distinguish between "Benefit" (calm, stable) and "Harm" (urgent, alarming).
2. **Annotation as Narrative:** Do not just plot lines. Add at least three text annotations to the plot that mark "The Consensus Crisis," "The Policy Lag," or "The Velocity Gap."
3. **The "So What?" Factor:** Use a title that is a *statement*, not a description. (e.g., *"Why Policy Inertia Makes AI Risks Grow Faster Than its Rewards"* instead of *"AI Growth Plot"*).

---

### **Part 4: The Written Story (300 Words)**

Write a short "news from the future" article (dated 2040) based on your plot.

* How did the "Velocity Gap" manifest?
* What specific institution (e.g., the FDA, UN, or Patent Office) was the bottleneck?
* What was the consequence of the harm curve outpacing the benefit curve?

---

### **Evaluation Rubric**

| Criteria | Excellent (5/5) | Developing (3/5) |
| --- | --- | --- |
| **Technical Execution** | Clean, bug-free Python code; effective use of libraries. | Code runs but has redundant steps or poor formatting. |
| **Data Storytelling** | Annotations and colors guide the eye to the "Velocity Gap." | Plot is technically correct but lacks context or narrative. |
| **Insight & Narrative** | The story explains *why* the curves diverge based on Michael Nielsen’s theories. | The story is generic and doesn't connect to the data. |
| **Aesthetics** | Professional styling (no default settings), clear labels, and high contrast. | Default Matplotlib colors; overlapping text or unreadable labels. |


## Interactive notebook

This is a complete Python structure designed to be copied directly into a **Jupyter Notebook** or **Google Colab**. It uses `Plotly` to create an interactive experience where students can hover over data points to see the "Institutional Bottlenecks" and "Unregulated Risks" at specific moments in time.

---

# **Notebook: The AI Velocity Gap Interactive Story**

### **Overview**

This notebook explores the "Velocity Gap" — the divergence between the exponential growth of AI risks and the linear/logistic growth of AI benefits. You will generate synthetic data, visualize it interactively, and annotate the "friction points" where human institutions struggle to keep pace.

---

## **Step 1: Setup and Data Generation**

We will generate a dataset spanning from 2024 to 2044.

* **Harmful Potential:** Modeled as an exponential curve.
* **Realized Benefits:** Modeled as a Logistic (S-curve) to simulate initial excitement followed by a "Consensus Plateau."

```python
import pandas as pd
import numpy as np
import plotly.graph_objects as go

def generate_velocity_data(years=20):
    np.random.seed(42)
    time = np.linspace(0, years, 200)
    
    # 1. Exponential Harm (Speed of Code)
    harm = 0.8 * np.exp(0.22 * time) + np.random.normal(0, 0.5, 200).cumsum() * 0.1
    
    # 2. Logistic Benefits (Institutional Speed)
    # L = max benefit, k = growth rate, x0 = midpoint
    L, k, x0 = 18, 0.35, 10
    benefits = L / (1 + np.exp(-k * (time - x0))) + np.random.normal(0, 0.1, 200)
    
    df = pd.DataFrame({
        'Year': 2024 + time,
        'Harmful_Potential': np.maximum(0, harm),
        'Realized_Benefits': np.maximum(0, benefits),
        'Gap': np.maximum(0, harm - benefits)
    })
    
    # Adding 'Event' labels for interactivity
    df['Event'] = ""
    df.loc[30, 'Event'] = "First Major AI-Driven Bank Run"
    df.loc[100, 'Event'] = "UN Global Consensus Summit (Deadlocked)"
    df.loc[150, 'Event'] = "Institutional Stagnation Peak"
    
    return df

df = generate_velocity_data()
df.head()

```

---

## **Step 2: Create the Interactive Plot**

In this step, we use `graph_objects` to create a dual-layered story. Hover over the lines to see the widening "Velocity Gap."

```python
# Create the figure
fig = go.Figure()

# Add the Harmful Potential Trace
fig.add_trace(go.Scatter(
    x=df['Year'], y=df['Harmful_Potential'],
    mode='lines',
    name='Harmful AI Potential',
    line=dict(color='#ef4444', width=4),
    hovertemplate='<b>Year %{x:.1f}</b><br>Harm Level: %{y:.2f}<extra></extra>'
))

# Add the Realized Benefits Trace
fig.add_trace(go.Scatter(
    x=df['Year'], y=df['Realized_Benefits'],
    mode='lines',
    name='Realized AI Benefits (Institutional)',
    line=dict(color='#3b82f6', width=4),
    fill='tonexty', # Fills the "Gap" between the two lines
    fillcolor='rgba(239, 68, 68, 0.1)', 
    hovertemplate='<b>Year %{x:.1f}</b><br>Benefit Level: %{y:.2f}<extra></extra>'
))

# Add markers for specific "Historical Events"
events = df[df['Event'] != ""]
fig.add_trace(go.Scatter(
    x=events['Year'], y=events['Harmful_Potential'],
    mode='markers+text',
    name='Critical Milestones',
    text=events['Event'],
    textposition="top left",
    marker=dict(color='black', size=10, symbol='x')
))

# Update Layout for Storytelling
fig.update_layout(
    title={
        'text': "<b>The Velocity Gap: Why AI Risk Outpaces Policy</b><br><span style='font-size:14px; color:gray'>Exponential technical harms vs. Logistic institutional benefits</span>",
        'y':0.95, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'
    },
    xaxis_title="Timeline (Years)",
    yaxis_title="Impact Magnitude",
    hovermode="x unified",
    template="plotly_white",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    shapes=[
        # Highlight the "Divergence Point"
        dict(type="rect", xref="x", yref="paper",
             x0=2034, y0=0, x1=2044, y1=1,
             fillcolor="LightSalmon", opacity=0.1, layer="below", line_width=0),
    ]
)

# Add a narrative annotation
fig.add_annotation(
    x=2038, y=35,
    text="<b>The Velocity Gap</b><br>Risk grows permissionless;<br>Benefits require consensus.",
    showarrow=True, arrowhead=2,
    ax=40, ay=-40,
    bordercolor="#c7c7c7", borderwidth=2, borderpad=4, bgcolor="#ffffff", opacity=0.8
)

fig.show()

```

---

## **Step 3: Critical Analysis (Discussion Questions)**

1. **The Divergence Point:** Around the year 2034, the red line surpasses the blue line. Based on Michael Nielsen's essay, what specific "social technologies" could we invent to move the blue line upward?
2. **The Shape of the Curve:** Why is a **Logistic Curve (S-curve)** a more realistic model for AI benefits than a straight line? (Hint: Think about FDA approvals or international treaties).
3. **The Shaded Area:** The shaded red area represents the "Unmanaged Risk." If you were a policymaker, what is the maximum "Gap" you would allow before pausing AI development?

---

### **Student Task: Narrative Extension**

**Modify the code above to simulate a "Policy Breakthrough" Scenario.**

* Change the `benefit_trajectory` parameters so that the curve doesn't plateau at 18, but continues to grow linearly after year 10.
* Add a new annotation to the plot marking where "Global Consensus" was reached.
* **Export your plot as an HTML file** and write a 200-word summary explaining how your new data changes the future outcome.

---

### **How to use this in class:**

1. **Live Coding:** Run the data generation block first and ask students to guess what the plot will look like.
2. **Parameter Tweak:** Have students change the `k` (growth rate) in the logistic function to see how "faster bureaucracy" changes the outcome.
3. **Visualization Critique:** Discuss why we used a "fill" between the lines (to visually represent the *cost* of the gap).


## Activity

- Now read this [blog on how we are all connected to Ramanujan](https://github.com/neelsoumya/science_blog_fun/blob/main/ramanujan_breath.md)

- Implement the core formula `probabilty = e^(x * a / b)`

where

`x` = number of molecules breathed by us

`a` = number of molecules breathed by Ramanujan during his lifetime

`b` = Number of molecules in the Earth's atmosphere

- Design an interactive simulation that varies `x`, `a` and `b` and looks at how it changes the probability that we breathe a molecule inhaled by Ramanujan.
