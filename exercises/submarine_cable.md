Nice — I went looking for an authoritative, *public* dataset you can use instead of (or alongside) TeleGeography, and the best match is the European open dataset from EMODnet (the EMODnet Human Activities “Cables — Telecommunication” layer). It’s licensed **CC-BY 4.0**, includes cable polylines for European waters, and is exactly what you want for a reproducible North Sea / Baltic topology. 

Two quick notes before the runnable work:

* I attempted to fetch the ZIP directly from the EMODnet geonetwork inside the assistant environment, but the runtime blocked downloading that large binary here. The dataset is nevertheless public and downloadable from EMODnet (link and WFS service are below). ([ows.emodnet-humanactivities.eu][1])
* TeleGeography’s interactive map is the canonical commercial map; it’s excellent but the underlying data is licensed (you may need TeleGeography permission for publication). ([submarinecablemap.com][2])

Because I can’t reliably transfer the EMODnet ZIP into this environment, I prepared a **complete, ready-to-run Python script** (and short alternative WFS/R examples) that will:

1. Download the EMODnet ZIP (official link),
2. Extract the shapefile layer(s),
3. Build a **precise North Sea / Baltic** node & edge CSV pair (landing points as nodes; cables as edges), and
4. Produce a **high-resolution map** (PNG or PDF) showing cable routes and landing stations (suitable for a paper figure).

Run this locally (or on any machine with internet). I also include exact bbox coordinates and optional improvements (basemap, styling). Everything uses open data & CC-BY attribution.

---

# What to download / endpoints

Recommended dataset (EMODnet, CC-BY 4.0):
`https://ows.emodnet-humanactivities.eu/geonetwork/srv/api/records/39ebe289-410b-4a5d-88a4-51bfcde538de/attachments/EMODnet_HA_Cables_Telecommunication_20230628.zip` (the EMODnet geonetwork record & download page). ([ows.emodnet-humanactivities.eu][1])

Other useful references/tools:

* EMODnet WFS endpoint & docs (you can pull features by WFS if you prefer). ([emodnet.ec.europa.eu][3])
* TeleGeography Submarine Cable Map (commercial). ([submarinecablemap.com][2])

---

# Ready-to-run Python script

Save as `build_northsea_baltic_topology.py` and run in a conda / venv environment.

```python
"""
Produce North Sea / Baltic submarine cable topology CSVs + high-resolution map
Source data: EMODnet "Cables - Telecommunication" (CC-BY 4.0).
Usage:
  python build_northsea_baltic_topology.py --outdir ./output

Requires:
  pip install geopandas shapely fiona requests matplotlib contextily pyproj rtree
  (contextily optional but recommended for basemap; rtree helps spatial indexing)
Notes:
  - The script downloads the EMODnet ZIP, extracts shapefile layers, then
    filters polys inside the bbox for North Sea & Baltic and exports:
      - nodes.csv (landing points: lat, lon, id, cable_name)
      - edges.csv (cable segments referencing node ids)
      - topology_map.png (high-res map)
  - Attribution: EMODnet Human Activities (CC-BY 4.0).
"""

import os
import io
import sys
import argparse
import zipfile
import requests
import geopandas as gpd
from shapely.geometry import Point, LineString
import pandas as pd
import matplotlib.pyplot as plt
import contextily as ctx

EMODNET_ZIP_URL = "https://ows.emodnet-humanactivities.eu/geonetwork/srv/api/records/39ebe289-410b-4a5d-88a4-51bfcde538de/attachments/EMODnet_HA_Cables_Telecommunication_20230628.zip"

# bbox covering North Sea + Baltic (lon_min, lat_min, lon_max, lat_max)
NORTHSEA_BALTIC_BBOX = (-6.5, 53.5, 30.5, 61.5)

def download_and_unpack_zip(url, workdir):
    print("Downloading EMODnet dataset...")
    r = requests.get(url, stream=True, timeout=60)
    r.raise_for_status()
    zpath = os.path.join(workdir, "EMODnet_cables.zip")
    with open(zpath, "wb") as fh:
        for chunk in r.iter_content(chunk_size=8192):
            fh.write(chunk)
    print("Downloaded to", zpath)
    print("Extracting...")
    with zipfile.ZipFile(zpath, "r") as zf:
        zf.extractall(workdir)
    print("Extracted files to", workdir)
    return workdir

def find_shapefiles(workdir):
    shp_files = []
    for root, _, files in os.walk(workdir):
        for f in files:
            if f.lower().endswith(".shp"):
                shp_files.append(os.path.join(root, f))
    return shp_files

def line_endpoints(line):
    """Return first and last coordinate tuple for a LineString (or MultiLineString)"""
    if line.geom_type == "MultiLineString":
        # choose the first subline
        line = list(line.geoms)[0]
    coords = list(line.coords)
    return coords[0], coords[-1]

def main(outdir):
    os.makedirs(outdir, exist_ok=True)
    workdir = os.path.join(outdir, "raw")
    os.makedirs(workdir, exist_ok=True)

    # 1) Download & unpack
    download_and_unpack_zip(EMODNET_ZIP_URL, workdir)

    # 2) Find shapefiles and load the cable polylines (choose the relevant layer)
    shp_files = find_shapefiles(workdir)
    print("Found shapefiles:", shp_files)
    # Heuristics: pick the shapefile whose name contains 'cable' or 'tele'
    cable_shp = None
    for s in shp_files:
        name = os.path.basename(s).lower()
        if "cable" in name or "tele" in name or "submarine" in name:
            cable_shp = s
            break
    if cable_shp is None and shp_files:
        cable_shp = shp_files[0]
    if cable_shp is None:
        raise RuntimeError("No shapefile found in downloaded EMODnet archive.")

    print("Loading cable shapefile:", cable_shp)
    gdf = gpd.read_file(cable_shp)
    print("Loaded features:", len(gdf))

    # Reproject to WGS84 if needed
    if gdf.crs is None:
        gdf.set_crs(epsg=4326, inplace=True)
    else:
        gdf = gdf.to_crs(epsg=4326)

    # 3) Clip to bbox
    lonmin, latmin, lonmax, latmax = NORTHSEA_BALTIC_BBOX
    bbox_poly = gpd.GeoSeries([LineString([(lonmin,latmin),(lonmin,latmax),(lonmax,latmax),(lonmax,latmin),(lonmin,latmin)])]).set_crs(epsg=4326).envelope[0]
    gdf_clipped = gdf[gdf.intersects(bbox_poly)].copy()
    print("Features after bbox filter:", len(gdf_clipped))

    # 4) Build nodes (landing points) by extracting line endpoints
    nodes = []
    edges = []
    node_index = {}
    next_node_id = 1

    for idx, row in gdf_clipped.iterrows():
        geom = row.geometry
        try:
            start, end = line_endpoints(geom)
        except Exception:
            # skip invalid
            continue
        cable_name = row.get('name') or row.get('Name') or row.get('cable') or f"cable_{idx}"
        for pt, tag in [(start, 'start'), (end, 'end')]:
            lon, lat = pt[0], pt[1]
            key = (round(lat,6), round(lon,6))
            if key not in node_index:
                nid = f"N{next_node_id:05d}"
                node_index[key] = nid
                nodes.append({"node_id": nid, "lat": lat, "lon": lon, "label": f"{cable_name}_{tag}"})
                next_node_id += 1
        # add edge referencing node ids
        n1 = node_index[(round(start[1],6), round(start[0],6))]
        n2 = node_index[(round(end[1],6), round(end[0],6))]
        edges.append({"cable": cable_name, "source": n1, "target": n2})

    nodes_df = pd.DataFrame(nodes)
    edges_df = pd.DataFrame(edges)

    # Save CSVs
    nodes_csv = os.path.join(outdir, "northsea_baltic_nodes.csv")
    edges_csv = os.path.join(outdir, "northsea_baltic_edges.csv")
    nodes_df.to_csv(nodes_csv, index=False)
    edges_df.to_csv(edges_csv, index=False)
    print("Saved CSVs:", nodes_csv, edges_csv)

    # 5) Produce a high-resolution map
    # Convert nodes to GeoDataFrame
    nodes_gdf = gpd.GeoDataFrame(nodes_df, geometry=gpd.points_from_xy(nodes_df.lon, nodes_df.lat), crs="EPSG:4326")
    # Plot cables and nodes
    fig, ax = plt.subplots(1,1, figsize=(14,12), dpi=300)
    # plot base cables (clipped)
    gdf_clipped.plot(ax=ax, linewidth=0.7, alpha=0.8, edgecolor="tab:blue")
    nodes_gdf.plot(ax=ax, markersize=20, color="red", label="Landing points")
    # annotate (optional) - limit number of annotations to keep map clean
    for i, r in nodes_gdf.iterrows():
        ax.annotate(r['node_id'], xy=(r.geometry.x, r.geometry.y), xytext=(3,3), textcoords="offset points", fontsize=6)
    ax.set_title("North Sea / Baltic — Submarine Cable Routes & Landing Points\nSource: EMODnet Human Activities (CC-BY 4.0)")
    ax.set_xlim(lonmin - 1.0, lonmax + 1.0)
    ax.set_ylim(latmin - 1.0, latmax + 1.0)
    # add a tiled basemap if contextily available
    try:
        ctx.add_basemap(ax, crs=nodes_gdf.crs.to_string(), source=ctx.providers.Stamen.TonerLite)
    except Exception:
        pass
    ax.axis('off')
    outmap = os.path.join(outdir, "northsea_baltic_topology_map.png")
    plt.tight_layout()
    plt.savefig(outmap, bbox_inches="tight", dpi=300)
    plt.close()
    print("Saved map:", outmap)

    print("\nDONE. Attribution: EMODnet Human Activities — Cables (CC-BY 4.0).")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--outdir", default="./output", help="Output directory")
    args = parser.parse_args()
    main(args.outdir)
```

---

# How this script works (short)

* It downloads the EMODnet ZIP and extracts shapefiles. (If you prefer the WFS route, see the alternative notes below.) ([ows.emodnet-humanactivities.eu][1])
* It loads the cable polylines (GeoDataFrame), filters to a North Sea/Baltic bbox, extracts each polyline’s endpoints to produce landing points (nodes) and a simple edges table.
* It writes `northsea_baltic_nodes.csv` and `northsea_baltic_edges.csv` and exports a high-resolution PNG map (`northsea_baltic_topology_map.png`) suitable for conference figures.

If you want landing *stations* matched to official station names rather than endpoints inferred from the line endpoints, we can postprocess by snapping endpoints to a known landing-station point layer (if a point layer exists in the EMODnet package or another dataset). EMODnet’s package sometimes includes separate landing-station point layers — if present the script can be adjusted to use them.

---

# WFS / R alternative (quick)

If you prefer not to download the ZIP but query EMODnet WFS directly (feature-level), EMODnet documents show WFS examples and there’s an R client `emodnet.wfs` that makes pulling layers straightforward. Example R snippet (uses emodnet.wfs):

```r
# install.packages("emodnet.wfs", repos = c("https://ropensci.r-universe.dev", "https://cloud.r-project.org"))
library(emodnet.wfs)
wfs <- emodnet_init_wfs_client("human_activities")  # example service name
layers <- emodnet_get_layer_info(wfs)
# then emodnet_get_layers(wfs, layers = "cables") with bbox filter etc
```

See EMODnet Web Services documentation for exact layer names and parameters. ([emodnet.ec.europa.eu][3])

---

# Licensing & citation

* Use and publish results under **CC-BY 4.0** attribution to EMODnet. Full metadata & download link: EMODnet geonetwork. ([ows.emodnet-humanactivities.eu][1])
* If you also use TeleGeography data, check their license and cite appropriately (TeleGeography data is licensed and often requires purchase/permission). ([submarinecablemap.com][2])

---

# If you’d like, next steps I can provide immediately (pick any, I will produce them now):

1. A polished figure-ready map style (colours, legend, lat/lon graticules) — I’ll give you the exact matplotlib code and CSS-like style tweaks.
2. A variant of the script that writes a GeoJSON topology and a GraphML for import into Gephi / NetworkX.
3. A short methods appendix paragraph you can paste into your paper describing how the topology was built (incl. bbox, filtering, endpoint extraction, attribution).

Which of 1–3 do you want *right now*? (No waiting — I’ll produce the script/text in this reply.)

[1]: https://ows.emodnet-humanactivities.eu/geonetwork/srv/api/records/39ebe289-410b-4a5d-88a4-51bfcde538de "EMODnet Human Activities, Cables, Telecommunication, Actual Routes"
[2]: https://www.submarinecablemap.com/?utm_source=chatgpt.com "Submarine Cable Map"
[3]: https://emodnet.ec.europa.eu/en/emodnet-web-service-documentation?utm_source=chatgpt.com "EMODnet web service documentation - European Union"
