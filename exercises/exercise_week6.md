# John Snow visualizations (Broad Street pump London)

John Snow’s 1854 map of the [Soho cholera outbreak](https://applieddatascience.cmp.uea.ac.uk/02/1/observation-and-visualization-john-snow-and-the-broad-street-pump.html) is a foundational case study in data visualization 🗺️. By plotting deaths as individual black bars at specific addresses, Snow provided spatial evidence that challenged the prevailing "miasma" theory (the belief that disease spread through "bad air") and identified the Broad Street pump as the source of the contagion 🧪. 

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

In this setup, we didn't specify a "weight" for the points. Folium's `HeatMap` simply looks at the coordinate list and says, "There is 1 death at this exact spot." When ten rows have nearly identical coordinates, the color turns from cool blue to a "hot" red.

Since we are trying to prove a causal link between the pumps and the deaths, the visual contrast is key.

Looking at the code above, the **radius** and **blur** parameters in `HeatMap` are essentially your "statistical tuning knobs." If you set the `radius` too high, the whole map becomes a red blob; too low, and it looks like a scattered rash.

How do you think changing the **radius** might affect your students' ability to identify the specific pump responsible for the outbreak? 🧐

---

[Interactive John Snow Map Tutorial](https://www.youtube.com/watch?v=H8Ypb8Ei9YA)
This video demonstrates how to take raw CSV data and transform it into a dynamic Folium map, which is exactly what we are doing with the cholera records.


## Questions

Visualizing Uncertainty: How we can use Python to show where the data might be "fuzzy" because of how it was digitized from a paper map 📜?

