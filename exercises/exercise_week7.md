# 🎮🛠️ Exercise on interactive visualizations and visual storytelling (Superintelligence) using `ipywidgets` and `streamlit` 


## Streamlit

- [streamlit](https://streamlit.io/playground?example=charts)

- [Interactive streamlit GDP dashboard](https://github.com/neelsoumya/gdp-dashboard)

- [Deploy on _streamlit.io_](https://streamlit.io/cloud)

- Click on [_New app_](https://share.streamlit.io/new)

- [Here](https://gdp-dashboard-t19rvs9nq2m.streamlit.app/) is a deployed app

- Push your code to github and deploy

- [Course on deeplearning.ai on streamlit](https://learn.deeplearning.ai/courses/fast-prototyping-of-genai-apps-with-streamlit/lesson/79cfr0/setting-up-your-environment)

- Setup a repository in _github_

- Or run in Google _Colab_

- Run _streamlit_ using

```bash
streamlit run script.py
```

- Here is an example script

```python
import streamlit as st
import pandas as pd
import numpy as np

st.write("Streamlit supports a wide range of data visualizations")

all_users = ["Alice", "Bob", "Charly"]
with st.container(border=True):
    users = st.multiselect("Users", all_users, default=all_users)
    rolling_average = st.toggle("Rolling average")

np.random.seed(19)
data = pd.DataFrame(np.random.randn(20, len(users)), columns=users)

if rolling_average:
    data = data.rolling(7).mean().dropna()

tab1, tab2 = st.tabs(["Chart", "Dataframe"])
tab1.line_chart(data, height=250)
tab2.dataframe(data, height=250, use_container_width=True)

```

- [ngrok signup](https://dashboard.ngrok.com/signup)

- [create an auth token](https://dashboard.ngrok.com/authtokens/new)

- [Google Colab notebook](https://github.com/neelsoumya/visualization_lecture/blob/main/streamlit.ipynb)

- To save your `ngrok` authtoken securely in Google Colab, you should use Colab's **Secrets** feature. This allows you to store sensitive information like API keys or tokens without embedding them directly in your code, which is important for security and when sharing notebooks.

1.  **Open the Secrets Panel:** In the left sidebar of your Colab notebook, click on the **"🔑 Secrets"** icon (it looks like a key).
2.  **Add a new secret:** Click the **"+ Add new secret"** button.
3.  **Name the secret:** For your `ngrok` authtoken, you could name it `YOUR_AUTHTOKEN` (or any other descriptive name you prefer, but remember it for later).
4.  **Enter the secret value:** Paste your `ngrok` authtoken into the "Value" field.
5.  **Save:** Click "Save secret".

Once saved, you can access this secret in your Python code using `from google.colab import userdata` and then `userdata.get('YOUR_AUTHTOKEN')` (replacing `'YOUR_AUTHTOKEN'` with the name you gave your secret).


### 📚 📝 Deployment for `streamlit`

- [Streamlit](https://share.streamlit.io/new)

- [Github](https://github.com/) Create new account on github

- Create new app and connect to [github](https://github.com/)

- Create new repository on github

- Upload your code to github (code below)

```python
import streamlit as st
import pandas as pd
import numpy as np
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium

st.title("Outbreak Investigator")
st.write("Adjust the settings in the sidebar, then try to identify the source of the outbreak from the map.")

# --- SIDEBAR CONTROLS ---
st.sidebar.header("Settings")
total_cases = st.sidebar.slider("Total cases", 100, 1000, 500)
cluster_pct = st.sidebar.slider("% of cases near the source", 10, 90, 70)
show_source = st.sidebar.checkbox("Reveal the true source")

# --- GENERATE SYNTHETIC DATA ---
market_lat, market_lon = 30.6195, 114.2577

cluster_count = int(total_cases * cluster_pct / 100)
noise_count = total_cases - cluster_count

np.random.seed(420)
cluster_lats = np.random.normal(market_lat, 0.005, cluster_count)
cluster_lons = np.random.normal(market_lon, 0.005, cluster_count)
noise_lats = np.random.uniform(30.50, 30.70, noise_count)
noise_lons = np.random.uniform(114.20, 114.40, noise_count)

cases = pd.DataFrame({
    'lat': np.concatenate([cluster_lats, noise_lats]),
    'lon': np.concatenate([cluster_lons, noise_lons]),
})

pois = pd.DataFrame({
    'name': ['Wuhan International Plaza', 'Huanan Seafood Market', 'Hankou Railway Station', 'Wuhan CDC'],
    'lat':  [30.584,   30.6195, 30.618, 30.612],
    'lon':  [114.271,  114.2577, 114.250, 114.265],
    'is_source': [False, True, False, False],
})

# --- SHOW STATS ---
st.write(f"**Total cases:** {total_cases} — **Clustered:** {cluster_count} — **Scattered:** {noise_count}")

# --- BUILD MAP ---
m = folium.Map(location=[30.61, 114.28], zoom_start=13, tiles='cartodbpositron')

HeatMap(cases[['lat', 'lon']].values.tolist(), radius=12, blur=15).add_to(m)

for _, poi in pois.iterrows():
    if poi['is_source'] and show_source:
        color = 'red'
        label = f"TRUE SOURCE: {poi['name']}"
    else:
        color = 'black'
        label = poi['name']

    folium.Marker(
        location=[poi['lat'], poi['lon']],
        popup=label,
        tooltip=label,
        icon=folium.Icon(color=color, icon='question-sign'),
    ).add_to(m)

st_folium(m, width=900, height=550)
```

- `requirements.txt` is here

```bash
streamlit>=1.35.0
streamlit-folium>=0.20.0
folium>=0.17.0
pandas>=2.0.0
numpy>=1.26.0
```

- Test code on [github codespaces](https://github.com/codespaces/new)

- [Connect to code on github](https://github.com/neelsoumya/wuhan_covid_scavenger_hunt_streamlit_teaching)

- [Deployed app](https://wuhan-scavenger-hunt-interactive.streamlit.app/)


- can also deploy on [Huggingface spaces](https://huggingface.co/spaces)

- For example, see the deployed app [here](https://huggingface.co/spaces/neelsoumya/streamlit_spatial)

- The code is shown in the next section

- Also deployed through [github](https://github.com/neelsoumya/streamlit_spatial/) and [streamlit](https://geospatial-visualization-soumya.streamlit.app/)


### Geospatial visualization using `streamlit`

- deployed app [here](https://huggingface.co/spaces/neelsoumya/streamlit_spatial)

- 🎮 code is shown below

```python
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

st.write("Streamlit has lots of fans in the geo community. 🌍 It supports maps from PyDeck, Folium, Kepler.gl, and others.")

chart_data = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
   columns=['lat', 'lon'])

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=37.76,
        longitude=-122.4,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=chart_data,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=chart_data,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))
```

## `ipywidgets` 

- We show how to create interactive visualizations

- How to bridge the gap between abstract technical concepts and data-driven storytelling? Below is a structured exercise designed for a Python-based data visualization class.

- Reading [Michale Nielsen superintelligence risk](https://michaelnotebook.com/whichfuture/index.html)

- [Blog post on superintelligence](https://neelsoumya.github.io/policy/agi_harms_benefits.html)

- Paper and resources co-created with students. Link forthcoming.

- [Game for paperclip optimization problem in AGI](https://www.decisionproblem.com/paperclips/index2.html)

Interested in learning more? See the [Cambridge AI Safety Hub](https://caish.org/)

---

## Exercise: The Velocity Gap – A Narrative Data Storytelling Challenge

### **Objective**

In this exercise, you will use Python to model a speculative future. You will generate synthetic data representing the growth of AI benefits versus AI harms, constrained by "Institutional Inertia." Your goal is to create a compelling visualization and a 300-word narrative that explains the "Velocity Gap" to a non-technical audience.

## 🎮💡 Activity

- Add one slide [here](https://docs.google.com/presentation/d/1YcxPIsxUEOoZrJjxtOYX2FYH08MPYccyIJZcqkkjXR4/edit?usp=sharing)

- Create a narrative around AGI and superintelligence using the code below.


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


## 🎮💡 Activity

- Now read this [blog on how we are all connected to Ramanujan](https://github.com/neelsoumya/science_blog_fun/blob/main/ramanujan_breath.md)

- Implement the core formula `probabilty = e^(x * a / b)`

where

`x` = number of molecules breathed by us

`a` = number of molecules breathed by Ramanujan during his lifetime

`b` = Number of molecules in the Earth's atmosphere

- Design an interactive simulation that varies `x`, `a` and `b` and looks at how it changes the probability that we breathe a molecule inhaled by Ramanujan.

- 🤔❓How can you innovatively visualize a probability?


Play around with this interactive [Google Colab notebook](https://colab.research.google.com/drive/1TsCXpshIREbIG36MtTpOYdoo3szw0A1X?usp=sharing)


# Interactive math exercise

- ChatGPT has a feature to allow you to [interactively learn math exercises](https://openai.com/index/new-ways-to-learn-math-and-science-in-chatgpt/)

- Design an interactive notebook in Python using the `ipywidgets` package to understand the Pythagoras theorem

- Solution is shown below

```python
# Interactive Pythagoras Notebook (ipywidgets)
# -------------------------------------------------
# Run this file in a Jupyter environment (JupyterLab / Jupyter Notebook)
# Requires: numpy, matplotlib, ipywidgets, IPython. Optional: sympy
#
# Features:
# - Interactive sliders for legs a and b
# - Live plotting of the right triangle and squares on each side
# - Numeric and symbolic checks that a^2 + b^2 = c^2
# - Short exercises and an auto-generated quiz with answer checking

import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from ipywidgets import FloatSlider, IntSlider, Checkbox, Button, Output, HBox, VBox, Label, Layout, interactive_output, Dropdown, BoundedFloatText, FloatText
from IPython.display import display, Markdown, HTML

# ---------- Helper geometry utilities ----------

def hypotenuse(a, b):
    return math.hypot(a, b)


def centroid_triangle(p1, p2, p3):
    return ((p1[0]+p2[0]+p3[0])/3.0, (p1[1]+p2[1]+p3[1])/3.0)


def square_coords(p1, p2, outward_point):
    """
    Given segment p1->p2, return coordinates of the square built on that segment.
    outward_point is a point inside the triangle (so we can choose the square direction away from the triangle).
    """
    p1 = np.array(p1, dtype=float)
    p2 = np.array(p2, dtype=float)
    v = p2 - p1
    L = np.linalg.norm(v)
    if L == 0:
        return [p1.tolist()]
    # perpendicular vector of same length
    perp = np.array([-v[1], v[0]])
    perp = perp / np.linalg.norm(perp) * L
    midpoint = (p1 + p2) / 2.0
    # choose perp direction so it points away from triangle centroid
    dir_test = outward_point - midpoint
    if np.dot(perp, dir_test) > 0:
        perp = -perp
    q1 = p1 + perp
    q2 = p2 + perp
    # square coords (p1 -> p2 -> q2 -> q1)
    return [tuple(p1.tolist()), tuple(p2.tolist()), tuple(q2.tolist()), tuple(q1.tolist())]


# ---------- Plotting function ----------

def plot_triangle_and_squares(a, b, show_squares=True, annotate=True, figsize=(6,6)):
    """Plot a right triangle with legs a (x-axis) and b (y-axis) and the squares on each side."""
    # points
    A = (0.0, 0.0)       # right angle at origin
    B = (a, 0.0)         # point on x-axis
    C = (0.0, b)         # point on y-axis
    c = hypotenuse(a, b)

    # prepare figure
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_aspect('equal', adjustable='box')

    # triangle
    tri = Polygon([A, B, C], closed=True)
    ax.add_patch(Polygon([A, B, C], closed=True, fill=True, alpha=0.15, edgecolor='black'))

    patches = []
    colors = []

    centroid = np.array(centroid_triangle(A,B,C))

    if show_squares:
        # square on AB (length a)
        sq_ab = square_coords(A, B, outward_point=centroid)
        patches.append(Polygon(sq_ab, closed=True))
        colors.append(0.6)

        # square on AC (length b)
        sq_ac = square_coords(A, C, outward_point=centroid)
        patches.append(Polygon(sq_ac, closed=True))
        colors.append(0.4)

        # square on BC (hypotenuse length c)
        sq_bc = square_coords(B, C, outward_point=centroid)
        patches.append(Polygon(sq_bc, closed=True))
        colors.append(0.2)

        p = PatchCollection(patches, alpha=0.18, edgecolor='black')
        ax.add_collection(p)

    # plot points and edges
    xs = [A[0], B[0], C[0], A[0]]
    ys = [A[1], B[1], C[1], A[1]]
    ax.plot(xs, ys, '-k')
    ax.scatter([A[0],B[0],C[0]],[A[1],B[1],C[1]], zorder=20)
    ax.text(A[0], A[1], ' A (right angle)', fontsize=9, va='top', ha='left')
    ax.text(B[0], B[1], f' B ({a:.2f},0)', fontsize=9, va='bottom', ha='center')
    ax.text(C[0], C[1], f' C (0,{b:.2f})', fontsize=9, va='center', ha='right')

    # annotation for lengths
    mid_ab = ((A[0]+B[0])/2.0, (A[1]+B[1])/2.0)
    mid_ac = ((A[0]+C[0])/2.0, (A[1]+C[1])/2.0)
    mid_bc = ((B[0]+C[0])/2.0, (B[1]+C[1])/2.0)
    ax.text(mid_ab[0], mid_ab[1]-0.05*max(a,b,1), f'a = {a:.2f}', ha='center')
    ax.text(mid_ac[0]-0.05*max(a,b,1), mid_ac[1], f'b = {b:.2f}', va='center', rotation=90)
    ax.text(mid_bc[0]+0.02*max(a,b,1), mid_bc[1]+0.02*max(a,b,1), f'c = {c:.2f}')

    # axes limits
    pad = max(a,b)*0.6 + 0.5
    ax.set_xlim(-pad, max(a,b)+pad)
    ax.set_ylim(-pad, max(a,b)+pad)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Right triangle with legs a and b; squares on each side')
    ax.grid(True, alpha=0.3)

    if annotate:
        # Area texts: squares areas
        ax.text(0.02, 0.98, f'a^2 = {a**2:.3f}\nb^2 = {b**2:.3f}\nc^2 = {c**2:.3f}\na^2 + b^2 = {(a**2+b**2):.3f}', transform=ax.transAxes,
                fontsize=10, va='top', bbox=dict(boxstyle='round', alpha=0.12))

    plt.show()


# ---------- Interactive widgets and layout ----------

# Widget definitions
a_slider = FloatSlider(value=3.0, min=0.1, max=12.0, step=0.1, description='a (leg):', continuous_update=True, layout=Layout(width='380px'))
b_slider = FloatSlider(value=4.0, min=0.1, max=12.0, step=0.1, description='b (leg):', continuous_update=True, layout=Layout(width='380px'))
show_squares_chk = Checkbox(value=True, description='Show squares')
annotate_chk = Checkbox(value=True, description='Show numeric annotation')

out_plot = Output()


def _update_plot(a, b, show_squares, annotate):
    out_plot.clear_output(wait=True)
    with out_plot:
        if a <= 0 or b <= 0:
            display(Markdown('**Please choose positive values for a and b.**'))
            return
        plot_triangle_and_squares(a, b, show_squares=show_squares, annotate=annotate)

# wire interactive output
widgets_to_link = {'a': a_slider, 'b': b_slider, 'show_squares': show_squares_chk, 'annotate': annotate_chk}
interactive_plot = interactive_output(_update_plot, widgets_to_link)

# Top instructions
instructions = Label(
    value="""
    # Pythagoras theorem — interactive exploration

    Move the sliders for **a** and **b** (the legs of a right triangle).
    - The notebook draws the triangle and the squares built on each of the three sides.
    - Compare the area of the square on the hypotenuse (c^2) with the sum of the areas of the squares on the legs (a^2 + b^2).

    Use the \"+Quiz\" section below to test your understanding with short exercises.
    """
)

controls = VBox([HBox([a_slider, b_slider]), HBox([show_squares_chk, annotate_chk])])

# Display UI
ui = VBox([instructions, controls, out_plot])

# initial render
_update_plot(a_slider.value, b_slider.value, show_squares_chk.value, annotate_chk.value)

# display interactive UI (so users can re-render by changing widgets)
display(ui)

# connect event handlers so that moving sliders updates the plot interactively
for w in [a_slider, b_slider, show_squares_chk, annotate_chk]:
    w.observe(lambda change: _update_plot(a_slider.value, b_slider.value, show_squares_chk.value, annotate_chk.value), names='value')


# ---------- Symbolic check (optional) ----------
try:
    import sympy as sp
    has_sympy = True
except Exception:
    has_sympy = False

if has_sympy:
    display(Markdown('**Symbolic demonstration (using SymPy)**'))
    a, b = sp.symbols('a b', positive=True)
    c = sp.sqrt(a**2 + b**2)
    expr = sp.simplify(c**2 - (a**2 + b**2))
    display(Markdown(f'`simplify(c**2 - (a**2 + b^2))` = `{expr}` (identically 0)'))
else:
    display(Markdown('*SymPy not detected — symbolic verification skipped (optional).*'))


# ---------- Small exercises & quiz ----------

quiz_out = Output()

# Widgets for exercise: compute hypotenuse
exercise_a = FloatText(value=3.0, description='a:')
exercise_b = FloatText(value=4.0, description='b:')
answer_input = FloatText(value=0.0, description='c (your answer):')
check_btn = Button(description='Check answer', button_style='primary')


def _check_answer(btn=None):
    quiz_out.clear_output()
    a = float(exercise_a.value)
    b = float(exercise_b.value)
    true_c = hypotenuse(a, b)
    user_c = float(answer_input.value)
    tol = 1e-2
    with quiz_out:
        if abs(user_c - true_c) <= tol:
            display(Markdown(f':white_check_mark: Correct! True c = {true_c:.5f}'))
        else:
            display(Markdown(f':x: Not quite. True c = **{true_c:.5f}**. Your answer = {user_c:.5f}'))

check_btn.on_click(_check_answer)

# Random quiz generator
rand_btn = Button(description='New random problem', button_style='info')

import random

def _new_problem(btn=None):
    a_val = round(random.uniform(1.0, 10.0), 2)
    b_val = round(random.uniform(1.0, 10.0), 2)
    exercise_a.value = a_val
    exercise_b.value = b_val
    answer_input.value = 0.0
    _update_plot(a_val, b_val, show_squares_chk.value, annotate_chk.value)

rand_btn.on_click(_new_problem)

# assemble quiz UI
quiz_box = VBox([
    Label(value='## Quick quiz — compute the hypotenuse'), # Changed Markdown to Label
    HBox([exercise_a, exercise_b, answer_input]),
    HBox([check_btn, rand_btn]),
    quiz_out
])

# display quiz
display(quiz_box)

# ---------- Extension ideas for students ----------

display(Markdown('''
---
### Extension ideas (for a class exercise or a short project)

1. **Proof by rearrangement**: create an interactive demonstration that divides the square of side (a+b) into pieces and rearranges them to show equality of areas.
2. **Generalize to Euclidean geometry**: demonstrate using vectors why the dot product leads to the theorem (u·u = |u|^2, and orthogonality implies cross terms vanish).
3. **Data-collection exercise**: measure (with a ruler) multiple right triangles and build a scatter plot of a^2 + b^2 vs c^2; compute residuals and discuss measurement error.
4. **3D generalization**: explore distance formula in 3D and compare to the Pythagorean result.

'''))

# End of notebook
display(Markdown('**Notebook ready — change sliders above or use the quiz to explore Pythagoras.**'))

```


## Gradio

- [Gradio](https://www.gradio.app/)

- # Gradio

This Python code uses the gradio and plotly.express libraries to create an interactive web application that visualizes car-sharing data on a map.

Here's a breakdown of what it does:

* Loads Data: It starts by loading a built-in spatial dataset called carshare from Plotly, which contains information about car availability, centroids (latitude and longitude), and peak hour usage.

* generate_map function: This function takes a peak_hour_threshold as input. It filters the carshare data to only include entries where the peak_hour is less than or equal to the provided threshold. Then, it creates a scatter mapbox plot using plotly.express, displaying car availability (car_hours) at different geographical locations (centroid_lat, centroid_lon). The color and size of the points on the map are determined by car_hours, and the map style is set to carto-positron.

* Gradio Interface: It defines a Gradio application using `gr.Blocks`:

It adds a title and a descriptive markdown text.
It includes a `gr.Slider` component, allowing users to select a peak_hour value (from 0 to 23). This slider acts as the input to filter the data.
It defines a gr.Plot() component as the output, which will display the Plotly map generated by the generate_map function.

* Interaction Logic: The hour_slider.change() method connects the slider's value to the generate_map function. This means that whenever the slider's value changes, the generate_map function is called with the new slider value, and the updated map is displayed in map_output.

* Initial Load: demo.load() ensures that the map is generated and displayed with the initial slider value (12) when the application first loads.

* Launch: Finally, demo.launch() starts the Gradio web server, making the interactive application accessible.


- Code is here

```python
import gradio as gr
import plotly.express as px

# 1. Load a built-in spatial dataset from Plotly
df = px.data.carshare()

def generate_map(peak_hour_threshold):
    """
    Filters the dataframe based on peak hour and returns a Plotly figure.
    """
    # Filter data based on the user's slider input
    filtered_df = df[df['peak_hour'] <= peak_hour_threshold]
    
    # Create the spatial scatter plot
    fig = px.scatter_mapbox(
        filtered_df, 
        lat="centroid_lat", 
        lon="centroid_lon", 
        color="car_hours", 
        size="car_hours",
        color_continuous_scale=px.colors.sequential.Plasma, 
        size_max=15, 
        zoom=10,
        mapbox_style="carto-positron",
        title=f"Car Availability (Peak Hour ≤ {peak_hour_threshold})"
    )
    
    fig.update_layout(margin={"r":0,"t":40,"l":0,"b":0})
    return fig

# 2. Define the Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("# 🚗 Montreal Ride-Sharing Explorer")
    gr.Markdown("Adjust the slider to filter car availability by peak hour usage.")
    
    with gr.Row():
        # Input: A slider for filtering
        hour_slider = gr.Slider(
            minimum=0, 
            maximum=23, 
            value=12, 
            step=1, 
            label="Filter by Peak Hour"
        )
    
    # Output: The Plotly Map
    map_output = gr.Plot()

    # Trigger logic: When the slider moves, update the map
    hour_slider.change(fn=generate_map, inputs=hour_slider, outputs=map_output)
    
    # Run the map on load
    demo.load(fn=generate_map, inputs=hour_slider, outputs=map_output)

if __name__ == "__main__":
    demo.launch()
```