# Environmental Data Visualization - Starter Notebooks
# 3 ready-to-run notebook-style sections in one Python script.
# Save as .py and open in Jupyter, or paste each section into separate notebook cells.

# -----------------------------
# Notebook 1: GBIF occurrences -> map + simple charts
# -----------------------------

"""
Notebook 1: GBIF species occurrences (example: harbour porpoise Phocoena phocoena)
- Installs: pygbif, pandas, geopandas, matplotlib, folium
- What it does: download occurrence records for a bounding box (North Sea area),
  clean coordinates, plot occurrence density on a static map and an interactive folium map.
"""

# Install dependencies (uncomment to run in a notebook)
# !pip install pygbif pandas geopandas matplotlib folium contextily

# Imports
import warnings
warnings.filterwarnings('ignore')

try:
    import pandas as pd
    import geopandas as gpd
    import matplotlib.pyplot as plt
    from pygbif import occurrences
    import folium
    from shapely.geometry import Point
except Exception as e:
    print('Missing packages. Run the pip install line at the top of the notebook. Error:', e)

# Parameters (North Sea bounding box)
min_lon, min_lat, max_lon, max_lat = -4.0, 50.0, 10.0, 61.0
# WKT polygon for GBIF geometry parameter (polygon made from bbox)
wkt = f"POLYGON(({min_lon} {min_lat},{max_lon} {min_lat},{max_lon} {max_lat},{min_lon} {max_lat},{min_lon} {min_lat}))"

print('Requesting some GBIF occurrences for Phocoena phocoena inside the North Sea bbox...')
# Fetch occurrences (limit small for demo - students can increase; for full exports use GBIF download API)
res = occurrences.search(scientificName='Phocoena phocoena', geometry=wkt, limit=300)

# Turn into DataFrame
records = res.get('results', [])
if not records:
    print('No records returned. Try increasing the limit or removing geometry filters.')
else:
    df = pd.json_normalize(records)
    # Keep useful columns
    cols = ['gbifID', 'species', 'decimalLatitude', 'decimalLongitude', 'year', 'country', 'basisOfRecord']
    df = df[[c for c in cols if c in df.columns]]
    df = df.dropna(subset=['decimalLatitude','decimalLongitude'])
    print(f'Fetched {len(df)} records')

    # Convert to GeoDataFrame
    gdf = gpd.GeoDataFrame(df, geometry=[Point(xy) for xy in zip(df.decimalLongitude.astype(float), df.decimalLatitude.astype(float))], crs='EPSG:4326')

    # Static plot with contextily basemap (optional)
    fig, ax = plt.subplots(figsize=(8,8))
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    # Plot base
    world.cx[min_lon-2:max_lon+2, min_lat-2:max_lat+2].plot(ax=ax, color='#f0f0f0', edgecolor='gray')
    gdf.plot(ax=ax, markersize=20, alpha=0.6)
    ax.set_title('GBIF occurrences: Phocoena phocoena (sample)')
    ax.set_xlim(min_lon, max_lon)
    ax.set_ylim(min_lat, max_lat)
    plt.show()

    # Interactive map (folium)
    m = folium.Map(location=[(min_lat+max_lat)/2,(min_lon+max_lon)/2], zoom_start=5)
    for _, r in gdf.iterrows():
        folium.CircleMarker(location=(r.decimalLatitude, r.decimalLongitude), radius=3, popup=str(r.species), fill=True).add_to(m)
    # Save to HTML
    m.save('gbif_phocoena_northsea_map.html')
    print("Interactive map saved to gbif_phocoena_northsea_map.html")

# -----------------------------
# Notebook 2: Marine Protected Areas (MPA) shapefile -> map + overlap with occurrences
# -----------------------------

"""
Notebook 2: Download MPA polygons from Defra / Natural England / JNCC and plot
- Installs: geopandas, matplotlib, folium, requests, zipfile
- What it does: download a boundary shapefile (or zipped shapefile), load into GeoDataFrame,
  and plot MPAs together with GBIF occurrence points from Notebook 1.
"""

# !pip install geopandas folium requests matplotlib

import os
import requests
from io import BytesIO
import zipfile

# Try JNCC MPA download (JNCC provides zipped shapefiles). If this fails, students can paste another URL.
jncc_url = 'https://hub.jncc.gov.uk/assets/a8b6f0a2-3a1b-4f0f-9fbb-0a3d9d7f9f7e'  # placeholder: students may replace with real JNCC file URL

mpa_local_zip = 'mpa_jncc.zip'

try:
    print('Attempting to download MPA shapefile from JNCC (placeholder URL).')
    r = requests.get(jncc_url, stream=True, timeout=30)
    if r.status_code == 200 and 'zip' in r.headers.get('Content-Type',''):
        open(mpa_local_zip, 'wb').write(r.content)
        z = zipfile.ZipFile(mpa_local_zip)
        z.extractall('mpa_shapefile')
        shp_files = [f for f in os.listdir('mpa_shapefile') if f.endswith('.shp')]
        if shp_files:
            mpa_gdf = gpd.read_file(os.path.join('mpa_shapefile', shp_files[0]))
            print('Loaded MPA shapefile with', len(mpa_gdf), 'features')
            ax = mpa_gdf.to_crs('EPSG:4326').plot(figsize=(8,8), alpha=0.5, edgecolor='k')
            ax.set_title('Marine Protected Areas (sample)')
            plt.show()
        else:
            print('No .shp found after extracting zip. Inspect the download URL or use the Defra dataset page to get the correct link.')
    else:
        print('Could not download from the placeholder JNCC URL. Status:', r.status_code)
except Exception as e:
    print('Download failed (this demo uses a placeholder URL). For a robust student exercise, replace `jncc_url` with a real shapefile URL from JNCC or Defra. Error:', e)

# OPTIONAL: overlay occurrences if Notebook 1 produced gbif data
try:
    if 'gdf' in globals() and not gdf.empty and 'mpa_gdf' in globals():
        base = mpa_gdf.to_crs('EPSG:4326').plot(figsize=(9,9), color='#cfe8ff', edgecolor='k')
        gdf.plot(ax=base, markersize=15, color='red')
        plt.title('MPAs and GBIF occurrences (sample)')
        plt.show()
except Exception as e:
    print('Could not overlay occurrences on MPAs:', e)

# -----------------------------
# Notebook 3: Continuous Plankton Recorder (CPR) time-series
# -----------------------------

"""
Notebook 3: CPR plankton dataset (DASSH / SAHFOS)
- Installs: pandas, matplotlib, requests
- What it does: fetch a CPR CSV (if publicly available), create a timeseries of abundance
  aggregated by year and plot trends.
- Note: CPR data licensing sometimes requires attribution; this code demonstrates automated download
  from the DASSH IPT archive if a public CSV is available.
"""

# !pip install pandas matplotlib requests

import io

# DASSH IPT resource page for SAHFOS CPR phytoplankton (resource id seen in web search)
dassh_resource = 'https://www.dassh.ac.uk/ipt/resource?r=sahfos-cpr-phyto'

# Many IPT archives expose 'download' links. We'll try to find a CSV download link by scraping the page.
try:
    r = requests.get(dassh_resource, timeout=20)
    if r.status_code == 200 and 'csv' in r.text.lower():
        # crude scraping: look for href that ends with .csv
        import re
        links = re.findall(r'href="([^"]+\.csv)"', r.text)
        if links:
            csv_url = links[0]
            print('Found CSV:', csv_url)
            csv_resp = requests.get(csv_url)
            csv_resp.encoding = 'utf-8'
            df_cpr = pd.read_csv(io.StringIO(csv_resp.text))
            print('Loaded CPR CSV with', len(df_cpr), 'rows')
            # Example: look for year and abundance-like columns
            # This will vary by CPR dataset version — inspect df_cpr.columns
            print('Columns:', df_cpr.columns.tolist()[:20])
            # Students should modify aggregation based on the dataset structure; here is a generic example:
            if 'year' in df_cpr.columns:
                df_cpr['year'] = pd.to_numeric(df_cpr['year'], errors='coerce')
                ts = df_cpr.groupby('year').size()
                ts.plot(kind='line', marker='o', figsize=(8,4))
                plt.title('CPR records per year (sample)')
                plt.xlabel('Year')
                plt.ylabel('Number of records')
                plt.show()
        else:
            print('No direct CSV link found on DASSH IPT page. Visit the page manually to download or use the CPR Survey data request process.')
    else:
        print('Could not fetch DASSH IPT page or no CSV link present (status code {}).'.format(r.status_code))
except Exception as e:
    print('CPR download attempt failed. Error:', e)

# -----------------------------
# Notes for students / instructors
# -----------------------------
# - Each section is deliberately modular: paste into separate Jupyter notebook cells if preferred.
# - Replace placeholder URLs (particularly the JNCC zip link) with the real download URLs listed on:
#     * JNCC MPA datasets: https://jncc.gov.uk/our-work/uk-marine-protected-area-datasets-for-download/
#     * Defra / Natural England MPA: https://environment.data.gov.uk/
#     * CPR datasets (SAHFOS / DASSH IPT): https://www.cprsurvey.org/ and https://www.dassh.ac.uk/ipt/
# - Encourage students to:
#     * increase GBIF download limits or use the GBIF download API for large exports (pygbif supports downloads)
#     * experiment with spatial joins (which occurrences fall inside which MPA polygons)
#     * add time sliders to folium maps (via plugins) or create animated matplotlib maps
#     * compute species richness per grid cell (use geopandas spatial joins + binning)
#
# End of starter notebooks script.
