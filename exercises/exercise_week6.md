# John Snow visualizations (Broad Street pump London)

- In the mid-19th century, London was a city struggling with rapid urbanization and a recurring, deadly mystery: cholera.

- At the time, the medical establishment overwhelmingly favored miasma theory, believing that diseases were spread by "bad air" or foul odors. 

- During the 1854 outbreak in Soho, physician John Snow challenged this dogma by hypothesizing that cholera was actually waterborne. 

- To prove it, he conducted what we now recognize as a landmark piece of shoe-leather epidemiology; he meticulously interviewed residents and plotted every recorded death as a black bar on a street map. 

- This map revealed a startling spatial cluster centered directly around the Broad Street water pump. Snow’s ability to transform raw data into a visual narrative not only convinced local officials to remove the pump handle—halting the epidemic

- John Snow’s 1854 map of the [Soho cholera outbreak](https://applieddatascience.cmp.uea.ac.uk/02/1/observation-and-visualization-john-snow-and-the-broad-street-pump.html) is a foundational case study in data visualization 🗺️. 

- By plotting deaths as individual black bars at specific addresses, Snow provided spatial evidence that challenged the prevailing "miasma" theory (the belief that disease spread through "bad air") and identified the Broad Street pump as the source of the contagion 🧪. 

- _Things to ponder_: 🤔❓ Observe how John Snow plotted bars/barplots to denote number of cases at a particular location

- This is a clever use of symbols: think back to the lesson on [data semiotics and the gestalt theory of visualization](../gestalt_theory.md)

- Read the article and the [visualization on the progress of the war in Iran](https://www.economist.com/middle-east-and-africa/2026/03/12/what-data-reveal-about-the-wars-progress). Notice how different colours have been used for the different nations and the size of the bubbles indicates the severity.


* [R package and resources for John Snow cholera data and visualization](https://arxiv.org/html/2504.13970v1)


1. **Visual Encoding & Design Analysis**: This track focuses on the "how." You can teach students about Snow’s choice of marks (the bars) and channels (spatial position) ✒️. We can also look at the **Voronoi diagram** added to later versions, which used geometry to show which houses were mathematically closest to the Broad Street pump.
2. **Evidence-Based Storytelling**: This track focuses on the "why." It explores how Snow used data to pivot public health policy. It’s an excellent way to discuss the ethics of data ⚖️ and how a visualization can be a tool for advocacy rather than just a neutral report.
3. **Modern Technical Re-creation**: This is a hands-on track where students use modern datasets to recreate Snow’s analysis. We can develop a lab guide for using tools like **R (ggplot2)**, **Python (Folium/GeoPandas)**, or **GIS software** to create heat maps and spatial joins 💻.


---

[John Snow's map reimagined](https://www.youtube.com/watch?v=sMVjScewXwM)

This video provides a modern geospatial walkthrough of how Snow's data is visualized today, which can help your students see the connection between 19th-century methods and current technology.



## Exercise

To get started with your lab, we will use a digitized version of the **1854 Soho** data that includes modern GPS coordinates.

### 🗺️ The Data

The most reliable source for this exercise is the **Robin Wilson** dataset, which has been formatted into CSVs. You can read these directly into Pandas using the URLs below:

[Data from Robin's Blog](https://blog.rtwilson.com/john-snows-cholera-data-in-more-formats/)

* **Deaths (Individual Records):** `https://raw.githubusercontent.com/JimGrum/JohnSnow/master/data/deaths.csv`
* **Pumps:** `https://raw.githubusercontent.com/JimGrum/JohnSnow/master/data/pumps.csv`

---

### 🐍 Boilerplate Python Code

This script handles the heavy lifting: it loads the data, centers a map on the historic **Broad Street pump**, and layers on the density.

_Folium_ is a powerful Python library used to create interactive maps 🗺️. It acts as a bridge between Python’s data manipulation capabilities and **Leaflet.js**, a popular JavaScript library for mobile-friendly interactive maps.

With Folium, you can:

* **Create base maps** using different providers like OpenStreetMap or CartoDB.
* **Add markers** and popups to specific coordinates.
* **Overlay data** using heatmaps, choropleths (shaded regions), or vector layers.

### 🛠️ Basic Intro Code

To get a map running, you only need a few lines. This example centers a map on the **Broad Street Pump** coordinates and adds a simple marker.

```python
import folium

# 1. Create a Map object 
# 'location' takes [latitude, longitude]
# 'tiles' changes the background style
study_area = folium.Map(location=[51.5132, -0.1367], zoom_start=17, tiles="OpenStreetMap")

# 2. Add a simple Marker
folium.Marker(
    location=[51.5132, -0.1367],
    popup="Broad Street Pump",
    tooltip="Click for info",
    icon=folium.Icon(color="red", icon="info-sign")
).add_to(study_area)

# 3. Display the map
study_area

```


```python
import pandas as pd
import folium
from folium.plugins import HeatMap

# 1. Load the data
#deaths = pd.read_csv("https://raw.githubusercontent.com/JimGrum/JohnSnow/master/data/deaths.csv")
#pumps = pd.read_csv("https://raw.githubusercontent.com/JimGrum/JohnSnow/master/data/pumps.csv")


import numpy as np

# 1. Generate Synthetic Data
# Define the main Broad Street Pump location
broad_st_pump = [51.5132, -0.1367]

# Create 50 deaths clustered tightly around the Broad Street pump
# np.random.normal adds a small 'jitter' to the coordinates
lat_cluster = np.random.normal(51.5132, 0.0005, 50)
lon_cluster = np.random.normal(-0.1367, 0.0005, 50)

# Create a small DataFrame for these synthetic deaths
deaths = pd.DataFrame({'Lat': lat_cluster, 'Lon': lon_cluster})

# Create a simple DataFrame for 2 pumps
pumps = pd.DataFrame({
    'Pump_Name': ['Broad Street Pump', 'Oxford Street Pump'],
    'Lat': [51.5132, 51.5150],
    'Lon': [-0.1367, -0.1350]
})

# 🛠️ Now plot! Without looking at the code below!
```

* Solution


```python

# 2. Initialize the map (Centered on Soho, London)
# Coordinates: 51.5132, -0.1367
m = folium.Map(location=[51.5132, -0.1367], zoom_start=17, tiles="cartodbpositron")

# 3. Add Pumps as markers
for _, pump in pumps.iterrows():
    folium.Marker(
        location=[pump['Lat'], pump['Lon']],
        popup=pump['Pump_Name'],
        icon=folium.Icon(color='blue', icon='tint')
    ).add_to(m)

# 4. Create the HeatMap
# Because we have individual records, we just need a list of [lat, lon] pairs.
heat_data = deaths[['Lat', 'Lon']].values.tolist()

# The 'radius' and 'blur' determine how the "heat" spreads between points
HeatMap(heat_data, radius=15, blur=20).add_to(m)

# 5. Display the map
m

```

### 🧪 Understanding the "Heat"

In this setup, we did not specify a "weight" for the points. Folium's `HeatMap` simply looks at the coordinate list and says, "There is 1 death at this exact spot." When ten rows have nearly identical coordinates, the color turns from cool blue to a "hot" red.

Since we are trying to prove a causal link between the pumps and the deaths, the visual contrast is key.

Looking at the code above, the **radius** and **blur** parameters in `HeatMap` are essentially your "statistical tuning knobs." If you set the `radius` too high, the whole map becomes a red blob; too low, and it looks like a scattered rash.

How do you think changing the **radius** might affect your students' ability to identify the specific pump responsible for the outbreak? 🧐

---

[Interactive John Snow Map Tutorial](https://www.youtube.com/watch?v=H8Ypb8Ei9YA)
This video demonstrates how to take raw CSV data and transform it into a dynamic Folium map, which is exactly what we are doing with the cholera records.


## Questions

Visualizing Uncertainty: How we can use Python to show where the data might be "fuzzy" because of how it was digitized from a paper map 📜?



## 🎮🛠️ Advanced Exercise: Hunt for Epidemic Center in COVID-19

* Scavenger hunt exercise: generate new data and determine source of COVID-19 epidemic.

* This is a way to bridge 19th-century epidemiological methods with a 21st-century context. We are going to move the "detective work" to **Wuhan, China**, focusing on the early days of the COVID-19 pandemic.

In this scenario, your students are _Digital Epidemiologists._ They have been handed a "noisy" dataset of hospital admissions and must determine if there is a single point of origin or if the spread is truly random.

---

## 🕵️‍♂️ The Mission: The Wuhan "Patient Zero" Hunt

**The Backstory:** It’s early January 2020. Hospitals across Wuhan are reporting a "pneumonia of unknown cause." Your task is to map the first 500 reported cases. If John Snow was right, the "Pump" (the source) will be at the heart of the highest density cluster.

- An ipython notebook is available [here](https://colab.research.google.com/drive/1kP_smN-ho_NA8SV4yBFABq6qG6bmVMNc?usp=sharing)

### Step 1: Generate the Evidence (Synthetic Data)

Students will run this block first to create their "Evidence Files" (`cases.csv` and `points_of_interest.csv`).

```python
import pandas as pd
import numpy as np

# 1. Set the "Hidden" Source: Huanan Seafood Market
# Coordinates: 30.6195, 114.2577
market_lat, market_lon = 30.6195, 114.2577

# 2. Generate 500 Synthetic Cases
# 70% of cases are tightly clustered around the market (The Source)
cluster_count = 350
cluster_lats = np.random.normal(market_lat, 0.005, cluster_count)
cluster_lons = np.random.normal(market_lon, 0.005, cluster_count)

# 30% are scattered randomly across the city (Community spread/noise)
noise_count = 150
noise_lats = np.random.uniform(30.50, 30.70, noise_count)
noise_lons = np.random.uniform(114.20, 114.40, noise_count)

# Combine into a DataFrame
df_cases = pd.DataFrame({
    'case_id': range(500),
    'lat': np.concatenate([cluster_lats, noise_lats]),
    'lon': np.concatenate([cluster_lons, noise_lons])
})

# 3. List of Potential "Sources" (The Scavenger Hunt Targets)
df_pois = pd.DataFrame({
    'name': ['Wuhan International Plaza', 'Huanan Seafood Market', 'Hankou Railway Station', 'Wuhan CDC'],
    'lat': [30.584, 30.6195, 30.618, 30.612],
    'lon': [114.271, 114.2577, 114.250, 114.265]
})

df_cases.to_csv('wuhan_cases.csv', index=False)
df_pois.to_csv('wuhan_pois.csv', index=False)
print("Data Generated! You now have 'wuhan_cases.csv' and 'wuhan_pois.csv'.")

cases = df_cases
pois = df_pois

```

---

### Step 2: The Scavenger Hunt Challenge

Now, students can take this boilerplate. Their goal is to visualize the data and answer the **Investigation Questions** below.

```python
import pandas as pd
import folium
from folium.plugins import HeatMap

# LOAD DATA
cases = pd.read_csv('wuhan_cases.csv')
pois = pd.read_csv('wuhan_pois.csv')

# INITIALIZE MAP
# Center on Wuhan
m = folium.Map(location=[30.6, 114.3], zoom_start=13, tiles='cartodbpositron')

# TASK 1: Create a Heatmap of the 'cases'
heat_data = cases[['lat', 'lon']].values.tolist()
HeatMap(heat_data, radius=12, blur=15).add_to(m)

# TASK 2: Add markers for the POIs (Points of Interest)
# Use a different color to distinguish them from the 'heat'
for _, poi in pois.iterrows():
    folium.Marker(
        location=[poi['lat'], poi['lon']],
        popup=poi['name'],
        icon=folium.Icon(color='black', icon='question-sign')
    ).add_to(m)

m.save('wuhan_investigation.html')
m

```

---

### 🔍 Investigation Questions for Students

1. **The "Hot Zone":** Looking at the heatmap, which of the four black markers sits directly in the center of the "red" zone?
2. **The Red Herring:** One marker is near a major transportation hub (Hankou Station). Why might an epidemiologist mistake a **transportation hub** for a **source**?
3. **Data Noise:** You see cases scattered far away from the center. Does this disprove the "Market Theory," or does it represent a different stage of an outbreak? (Think: *Secondary Transmission*).
4. **The "Broad Street" Moment:** In 1854, Snow removed the pump handle. If you were the health official in Wuhan based *only* on this map, what would be your first "emergency" recommendation?

---

### 💡 Pro-Tip for the Lab

- Encourage students to tweak the `radius` and `blur` in the `HeatMap` function. 

- If they set the radius to **2**, the map will look like a scattered mess; if they set it to **50**, the entire city will look like it's on fire. 

- Finding the "just right" visualization is part of the data visualization craft!


## 🎮💡🛠️ Activity: use the `drawdata` package

- Use the []`drawdata` package](https://koaning.github.io/drawdata/) to draw data and make an interesting visualization

- You can draw data using the cursor!

- Credit: Thanks to Mark Fernandes for suggesting this


## 🎮💡🛠️ Activity: visualizing potholes

- Use data from Wales on [potholes](https://www.gov.wales/resurfaced-roads-potholes-repaired-and-potholes-prevented-april-2025-january-2026) and do a spatial visualization


## 🎮🛡️ Activity: Spatial Visualization of Cyber Attacks

In this activity, you will apply principles of spatial visualization to explore and communicate patterns in cyber attack data. Cyber security analysts often need to understand the geographic origin, target, and propagation of attacks in real-time or for post-incident analysis. Standard markers are often insufficient to capture the complexity of these events.

### Task 1: Data Acquisition or Synthesis
Choose **one** of the following approaches to obtain your dataset:
* **Option A (Public Data):** Find a publicly available dataset containing geographic information about cyber attacks (e.g., source IP geolocation, target location, attack type, timestamp). You can look at resources like Kaggle or open cybersecurity feeds.
* **Option B (Synthetic Data):** Create a synthetic dataset in Python that simulates a coordinated global cyber attack. Your dataset should include variables such as `Timestamp`, `Source_Lat`, `Source_Lon`, `Target_Lat`, `Target_Lon`, `Attack_Type` (e.g., DDoS, Phishing, Malware), and `Severity`.

Here is some starter Python code to help you generate synthetic data for Option B. You can run this snippet in a Jupyter Notebook or Python script to create a CSV file with mock cyber attack records.

```python
import pandas as pd
import numpy as np
import datetime

# Setup parameters
num_records = 500
np.random.seed(129)

# Generate synthetic timestamps over 24 hours
base_time = pd.Timestamp(datetime.datetime.now().date())
timestamps = [base_time + pd.Timedelta(minutes=np.random.randint(0, 1440)) for _ in range(num_records)]

# Types of attacks and severities
attack_types = ['DDoS', 'Malware', 'Phishing', 'Ransomware', 'SQL Injection']
severities = ['Low', 'Medium', 'High', 'Critical']

# Generate random geographical coordinates (approximate global bounds)
# Lat: -90 to +90, Lon: -180 to +180
src_lats = np.random.uniform(-90, 90, num_records)
src_lons = np.random.uniform(-180, 180, num_records)
tgt_lats = np.random.uniform(-90, 90, num_records)
tgt_lons = np.random.uniform(-180, 180, num_records)

# Generate categorical data
attacks = np.random.choice(attack_types, num_records)
sevs = np.random.choice(severities, num_records, p=[0.5, 0.3, 0.15, 0.05]) # Weighted probabilities

# Create DataFrame
df_cyber = pd.DataFrame({
    'Timestamp': sorted(timestamps),
    'Source_Lat': src_lats,
    'Source_Lon': src_lons,
    'Target_Lat': tgt_lats,
    'Target_Lon': tgt_lons,
    'Attack_Type': attacks,
    'Severity': sevs
})

# Save to CSV
df_cyber.to_csv('synthetic_cyber_attacks.csv', index=False)
print(f"Generated {num_records} synthetic cyber attack records in 'synthetic_cyber_attacks.csv'")
```

### Task 2: Design Special Symbols and Notations
Standard map markers (like simple dots or pins) are not enough for visualizing complex cyber threats. Design a custom set of symbols or a visual notation system tailored explicitly for cyber attacks. Consider:
* How will you visually distinguish between different *types* of attacks?
* How will you represent the *severity* or volume of an attack?
* Can you design glyphs that indicate the *state* of a target (e.g., compromised, under attack, secure)?

**Deliverable:** Create a legend or a sketch of your "symbol dictionary" explaining your choices for visual encoding.

### Task 3: Spatial Visualization Design
Using your dataset (Task 1) and your custom symbols (Task 2), design a spatial visualization (a map or a network graph projected onto a map) that tells the story of the cyber attack(s).
* Consider the map projection and base layer. E.g., Dark mode base maps are often used in cyber maps to make bright symbols pop—justify your choice.
* If your data is temporal, how will you represent changes over time? 

**Deliverable:** Produce a programmatic prototype of your visualization (e.g., using `folium`, `geopandas`, or similar tools) or a high-fidelity mockup using your designed notations.