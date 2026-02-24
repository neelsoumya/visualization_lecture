# 🎮💡🛠️ Activities

- [Submarine cables](https://www.submarinecablemap.com/)

- [Submarine cable maps](https://www.visualcapitalist.com/submarine-cables/)

- Which parts of the ocean are not covered at all?

- Are there chokepoints, which if taken out, would disrupt connectivity?

- Any `aha` moments? Can you write a narrative around this?

- [The true size](https://thetruesize.com/)

- [How big is the space economy](https://www.visualcapitalist.com/how-big-is-the-space-economy/) 

- [Why Greenland](https://www.visualcapitalist.com/how-greenlands-rare-earth-reserves-compare-to-the-rest-of-the-world/)

- [Code](exercises/submarine_cable.md)

- [Visualize a map of all cameras connected to the Internet using Shodan](https://maps.shodan.io/#53.288615899911065/82.09482192993165/5/satellite/cameras) Can you see any trends?

Data visualization with **Shodan**: messy, real-world data of the Internet of Things (IoT).

Since Shodan provides geographic, categorical, and temporal data, it’s a goldmine for teaching everything from basic bar charts to complex geospatial mapping.

---

## 🛠️ Essential Teacher Resources

* **The Academic Upgrade:** Shodan offers a **free Membership upgrade** for anyone with an `.edu` or university email. This gives students 100 query credits and access to Shodan Maps/Images. They should email `academic@shodan.io` if it doesn't auto-upgrade.
* **Shodan Trends:** [trends.shodan.io]() is perfect for teaching **time-series visualization**. It allows students to see how technologies (like Python versions or SSL protocols) have risen or fallen since 2017.
* **The Shodan CLI:** The Command Line Interface is the best way to "bridge" data into visualization tools. The `shodan parse` and `shodan convert` commands can turn raw JSON into CSVs for Excel, Tableau, or Python.

---

## 📊 3 Visual Data Assignments

These assignments progress from "low-code/no-code" to advanced data science.

### Assignment 1: The Global Exposure Map (Geospatial)

**Objective:** Visualize the density of a specific technology globally using Shodan’s built-in tools.

* **The Task:** Choose a niche technology (e.g., "Tesla Powerwall," "Wind Turbine," or "Minecraft Server"). Use **Shodan Maps** and **Shodan Reports** to generate a geographic distribution.
* **Visualization Goal:** Create a **Choropleth Map** (color-coded by country) and a **Top 10 Cities** bar chart.
* **Critique Point:** Ask students to explain why certain countries appear more "connected." Is it actual technology adoption, or just higher IP density?

### Assignment 2: The "Version Decay" Bar Chart (Categorical)

**Objective:** Extract data via CLI/API and visualize versioning and "technical debt."

* **The Task:** Run a query for a popular web server (e.g., `product:"nginx"` or `product:"Apache"`). Use `shodan stats --facets version` to get a breakdown.
* **Visualization Goal:** Create a **Sorted Bar Chart** or **Treemap** showing the distribution of versions.
* **Insight:** Students must highlight "End-of-Life" (EOL) versions in a different color (red) to visualize security risk as a data story.

### Assignment 3: The IoT Image Mosaic (Visual/Exploratory)

**Objective:** Deal with unstructured "image" data and metadata.

* **The Task:** Use the query `has_screenshot:true` with a filter like `org:"University of [Name]"`.
* **Visualization Goal:** Create an **Image Grid** or **Dashboard** that categorizes these "eyes" of the internet (e.g., webcams vs. VNC desktops vs. industrial dashboards).
* **Discussion:** This is a great springboard for a lecture on **Data Ethics**—just because the data is public doesn't mean it's ethical to visualize it without anonymization.

---

## 💡 Pro-Tips for the Classroom

* **Avoid the "Main" Search:** Encourage students to use **Filters** (e.g., `port:443`, `country:US`) immediately. A generic search for "webcam" is too noisy and often leads to "Forbidden" errors due to credit limits.
* **Data Cleaning:** Shodan data is "dirty." Banners often contain garbled text. Teaching students how to use Python's `json` library or `Pandas` to clean Shodan's nested JSON structure is a lesson in itself.


## Code

This script is designed to be a "starter kit" for your students. It uses the official `shodan` library to fetch data and `pandas` to structure it. This approach is much more powerful than the web interface because it allows students to perform custom aggregations and complex filtering.

### 🛠️ Prerequisites

Students will need to install the necessary libraries via terminal:

```bash
pip install shodan pandas matplotlib seaborn

```

---

### 🐍 The Shodan-to-Pandas Script

```python
import shodan
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Setup API Key
SHODAN_API_KEY = "YOUR_API_KEY_HERE"
api = shodan.Shodan(SHODAN_API_KEY)

# 2. Define the Query
# Example: Looking for industrial control systems (Modbus) or specific servers (nginx)
QUERY = 'product:"nginx" country:"US"'
LIMIT = 100 # Adjust based on credit availability

try:
    # 3. Fetch Data
    print(f"Searching for: {QUERY}...")
    results = api.search(QUERY, limit=LIMIT)
    
    # 4. Extract into a List of Dicts
    data = []
    for result in results['matches']:
        data.append({
            'IP': result['ip_str'],
            'Port': result['port'],
            'Organization': result.get('org', 'n/a'),
            'Country': result.get('location', {}).get('country_name', 'n/a'),
            'City': result.get('location', {}).get('city', 'n/a'),
            'OS': result.get('os', 'n/a'),
            'Transport': result.get('transport', 'tcp')
        })

    # 5. Create DataFrame
    df = pd.DataFrame(data)
    print("\n--- Data Preview ---")
    print(df.head())

    # 6. Basic Visualization: Top Organizations
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, y='Organization', order=df['Organization'].value_counts().iloc[:10].index)
    plt.title(f'Top 10 Organizations for query: {QUERY}')
    plt.xlabel('Count of Devices')
    plt.tight_layout()
    plt.show()

except shodan.APIError as e:
    print(f"Error: {e}")

```

---

### 🎓 Teaching Points for this Script

1. **Nested JSON to Flat Tables:** The most important lesson here is how we "flatten" the data. Shodan returns a deeply nested dictionary (e.g., `result['location']['country_name']`). Teaching students how to extract these specific paths into a flat CSV/DataFrame is a core data engineering skill.
2. **Handling Missing Values:** Shodan data is incomplete. Note the use of `.get('os', 'n/a')`—this prevents the script from crashing if a device doesn't report its Operating System.
3. **API Rate Limiting:** Explain that every `api.search` call consumes "Query Credits." This introduces students to the real-world constraint of **data budgeting**.

### 📈 Suggested Extension Assignment

Ask your students to modify the script to create a **Heatmap** using the `City` and `Port` columns. This will teach them how to perform a "pivot" or a "groupby" operation in Pandas before plotting.


