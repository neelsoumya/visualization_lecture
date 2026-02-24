# 🎮🛠️ Exercise on visual storytelling (Superintelligence)

How to bridge the gap between abstract technical concepts and data-driven storytelling? Below is a structured exercise designed for a Python-based data visualization class.

- Reading [Michale Nielsen superintelligence risk](https://michaelnotebook.com/whichfuture/index.html)

---

## Exercise: The Velocity Gap – A Narrative Data Storytelling Challenge

### **Objective**

In this exercise, you will use Python to model a speculative future. You will generate synthetic data representing the growth of AI benefits versus AI harms, constrained by "Institutional Inertia." Your goal is to create a compelling visualization and a 300-word narrative that explains the "Velocity Gap" to a non-technical audience.

---

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