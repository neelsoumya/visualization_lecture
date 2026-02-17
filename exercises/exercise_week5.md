# Interactive plots

- [Plotly](https://plotly.com/studio/)

- [Code plotly](https://plotly.com/python/waterfall-charts/)


"""
=============================================================
  INTERACTIVE DATA VISUALIZATION WITH PLOTLY
  Script 00 — Setup & Introduction
=============================================================

SETUP INSTRUCTIONS (run these in your terminal once):
------------------------------------------------------
  pip install plotly pandas numpy kaleido

  - plotly   → the visualization library
  - pandas   → data manipulation
  - numpy    → numerical computing
  - kaleido  → needed only if you want to export static images (.png/.pdf)

HOW TO RUN ANY SCRIPT IN THIS SERIES:
------------------------------------------------------
  python 01_bar_and_line.py     # runs in terminal, opens chart in browser
  python 02_scatter_bubble.py
  python 03_choropleth_maps.py
  python 04_3d_plots.py

Each script will open your chart automatically in your default browser.
No Jupyter required — these are plain Python files.

PLOTLY'S TWO APIS (know both):
------------------------------------------------------
  plotly.express (px)         — high-level, 1–2 lines per chart
  plotly.graph_objects (go)   — low-level, full control over every detail

  Best practice: start with px, use go when you need customization
  beyond what px exposes. They can be mixed freely.

BUILT-IN DATASETS (no downloads needed for practice):
------------------------------------------------------
  import plotly.express as px
  df = px.data.gapminder()   # world development indicators
  df = px.data.iris()        # flower measurements
  df = px.data.tips()        # restaurant tipping data
  df = px.data.stocks()      # stock price time series
"""

```python
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

print("Checking your installation...\n")
print(f"  plotly  version: {px.__version__}")  # type: ignore
print(f"  pandas  version: {pd.__version__}")
print(f"  numpy   version: {np.__version__}")
print("\n✅ All good! Run the numbered scripts to see each chart type.")

# Quick sanity-check plot — opens in browser
fig = px.bar(
    x=["Setup", "Complete", "Let's Go!"],
    y=[1, 2, 3],
    color=["Setup", "Complete", "Let's Go!"],
    title="✅ Plotly is installed and working",
    template="plotly_white",
)
fig.update_layout(showlegend=False)
fig.show()
```


```python
"""
=============================================================
  INTERACTIVE DATA VISUALIZATION WITH PLOTLY
  Script 01 — Bar Charts & Line Charts
=============================================================

CONCEPTS COVERED:
  - px.bar()           basic and grouped bars
  - barmode            'group', 'stack', 'overlay'
  - px.line()          single and multi-line
  - markers=True       dots on line charts
  - add_hline/vline    reference lines
  - update_traces()    modify visual properties after creation
  - update_layout()    titles, axes, templates, fonts

Run with:  python 01_bar_and_line.py
"""

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np


# ─────────────────────────────────────────────────────────────
#  SECTION 1: Basic Bar Chart
# ─────────────────────────────────────────────────────────────

def chart_01_basic_bar():
    """
    A simple bar chart. Key ideas:
      - Pass a DataFrame to px.bar()
      - color= assigns a different color per bar
      - text= labels the bars with a data column
      - update_traces() controls how the text is displayed
    """
    df = pd.DataFrame({
        "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"],
        "Population_M": [8.3, 4.0, 2.7, 2.3, 1.6],
        "Region": ["Northeast", "West", "Midwest", "South", "West"],
    })

    fig = px.bar(
        df,
        x="City",
        y="Population_M",
        color="Region",             # color bars by a categorical column
        text="Population_M",        # display values on top of bars
        title="US City Populations (millions)",
        labels={"Population_M": "Population (millions)"},  # rename axis label
        template="plotly_white",    # clean white background theme
    )

    # texttemplate formats the label; textposition controls placement
    fig.update_traces(texttemplate="%{text:.1f}M", textposition="outside")
    fig.update_layout(
        uniformtext_minsize=8,
        uniformtext_mode="hide",
        yaxis_range=[0, 10],        # set y-axis range manually
    )

    fig.show()  # opens in browser
    # fig.write_html("01_basic_bar.html")  # uncomment to save


# ─────────────────────────────────────────────────────────────
#  SECTION 2: Grouped & Stacked Bar Charts
# ─────────────────────────────────────────────────────────────

def chart_02_grouped_bar():
    """
    Grouped and stacked bars for comparing multiple series.

    TEACHING NOTE: Change barmode between 'group', 'stack', and 'overlay'
    and discuss with students:
      - 'group'   → best for comparing individual values across categories
      - 'stack'   → best for showing part-to-whole relationships
      - 'overlay' → rarely useful; shows overlap (needs opacity)
    """
    df = pd.DataFrame({
        "Quarter": ["Q1", "Q2", "Q3", "Q4"] * 2,
        "Revenue": [120, 150, 130, 180, 90, 110, 140, 160],
        "Product": ["Widget A"] * 4 + ["Widget B"] * 4,
    })

    # --- Grouped version ---
    fig_grouped = px.bar(
        df,
        x="Quarter",
        y="Revenue",
        color="Product",
        barmode="group",            # try: 'stack' or 'overlay'
        title="Quarterly Revenue by Product — Grouped",
        text="Revenue",
        template="plotly_white",
    )
    fig_grouped.update_traces(textposition="outside")
    fig_grouped.show()

    # --- Stacked version (same data, different story) ---
    fig_stacked = px.bar(
        df,
        x="Quarter",
        y="Revenue",
        color="Product",
        barmode="stack",
        title="Quarterly Revenue by Product — Stacked (shows totals better)",
        template="plotly_white",
    )
    fig_stacked.show()


# ─────────────────────────────────────────────────────────────
#  SECTION 3: Multi-Line Chart with Reference Lines
# ─────────────────────────────────────────────────────────────

def chart_03_line_chart():
    """
    A multi-line time-series chart. Key ideas:
      - color= in px.line() creates one line per category
      - markers=True adds a dot at every data point
      - add_hline() draws a horizontal reference line
      - add_vrect() shades a vertical region
    """
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    df = pd.DataFrame({
        "Month": months * 2,
        "Temp_F": [
            35, 38, 48, 60, 70, 78, 83, 81, 74, 62, 50, 39,   # New York
            57, 60, 65, 72, 79, 85, 92, 91, 86, 76, 64, 57,   # Los Angeles
        ],
        "City": ["New York"] * 12 + ["Los Angeles"] * 12,
    })

    fig = px.line(
        df,
        x="Month",
        y="Temp_F",
        color="City",
        markers=True,               # show a dot at each data point
        title="Monthly Average Temperature — NYC vs LA",
        labels={"Temp_F": "Temperature (°F)", "Month": ""},
        template="plotly_white",
        color_discrete_map={        # manually assign specific colors
            "New York": "#1f77b4",
            "Los Angeles": "#ff7f0e",
        },
    )

    # Add a horizontal dashed line at the freezing point
    fig.add_hline(
        y=32,
        line_dash="dot",
        line_color="lightblue",
        annotation_text="Freezing (32°F)",
        annotation_position="bottom right",
    )

    # Shade the summer months (Jun–Aug = indices 5–7)
    fig.add_vrect(
        x0="Jun", x1="Aug",
        fillcolor="yellow", opacity=0.1,
        layer="below", line_width=0,
        annotation_text="Summer", annotation_position="top left",
    )

    fig.update_layout(hovermode="x unified")  # single tooltip for all lines at x
    fig.show()


# ─────────────────────────────────────────────────────────────
#  SECTION 4: graph_objects — Building a Chart from Scratch
# ─────────────────────────────────────────────────────────────

def chart_04_go_bar():
    """
    The same bar chart built with graph_objects (go) instead of express.
    Use this to show students what px is doing under the hood.

    go gives you:
      - Full control over every trace property
      - Ability to add multiple trace types to one figure
      - Useful when px doesn't expose the parameter you need
    """
    categories = ["Apples", "Bananas", "Cherries", "Dates"]
    values_2023 = [45, 30, 60, 20]
    values_2024 = [55, 40, 50, 35]

    fig = go.Figure()

    # Each add_trace() call adds a new data series
    fig.add_trace(go.Bar(
        name="2023",
        x=categories,
        y=values_2023,
        marker_color="#636EFA",
        text=values_2023,
        textposition="auto",
    ))

    fig.add_trace(go.Bar(
        name="2024",
        x=categories,
        y=values_2024,
        marker_color="#EF553B",
        text=values_2024,
        textposition="auto",
    ))

    fig.update_layout(
        barmode="group",
        title="Fruit Sales 2023 vs 2024",
        xaxis_title="Fruit",
        yaxis_title="Units Sold",
        template="plotly_white",
        legend=dict(title="Year", orientation="h", y=1.1),
    )

    fig.show()


# ─────────────────────────────────────────────────────────────
#  RUN ALL CHARTS
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("Opening charts in your browser...")
    print("  Chart 1: Basic bar chart")
    chart_01_basic_bar()

    print("  Chart 2: Grouped + stacked bar charts")
    chart_02_grouped_bar()

    print("  Chart 3: Multi-line time series")
    chart_03_line_chart()

    print("  Chart 4: graph_objects bar (advanced)")
    chart_04_go_bar()

    print("\nDone! All charts opened.")
```