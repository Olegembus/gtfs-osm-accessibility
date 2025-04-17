import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

stops = pd.read_csv("E:/public_transport_accessibility/data/raw/gtfs/stops.txt") # путь к файлу со стопами

gdf = gpd.GeoDataFrame(
    stops,
    geometry=gpd.points_from_xy(stops.stop_lon, stops.stop_lat),
    crs="EPSG:4326"
)

gdf.to_file("E:/public_transport_accessibility/data/processed/gtfs_stops.geojson", driver='GeoJSON')
