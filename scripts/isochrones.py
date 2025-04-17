import osmnx as ox
import networkx as nx
import geopandas as gpd
from shapely.geometry import Point, Polygon
import matplotlib.pyplot as plt

# Загрузка графа
G = ox.load_graphml("E:/public_transport_accessibility/data/processed/osm_graph_with_time.graphml")
stops = gpd.read_file("E:/public_transport_accessibility/data/processed/gtfs_stops.geojson")

# Убедимся, что граф имеет атрибуты скорости и времени
G = ox.add_edge_speeds(G)
G = ox.add_edge_travel_times(G)

def get_isochrone_polygons(G, center_node, times):
    isochrone_polys = []
    for time in times:
        subgraph = nx.ego_graph(G, center_node, radius=time, distance='travel_time')
        node_points = [Point((data['x'], data['y'])) for node, data in subgraph.nodes(data=True)]
        polygon = gpd.GeoSeries(node_points).unary_union.convex_hull
        isochrone_polys.append((polygon, time))
    return isochrone_polys

# Временные интервалы в секундах (5, 10, 15 минут)
times = [300, 600, 900]

isochrones = []

for idx, stop in stops.iterrows():
    node = ox.distance.nearest_nodes(G, stop.geometry.x, stop.geometry.y)
    isochrone_polys = get_isochrone_polygons(G, node, times)
    isochrones.extend(isochrone_polys)

# Создание GeoDataFrame с атрибутом времени
iso_gdf = gpd.GeoDataFrame(isochrones, columns=['geometry', 'time'], crs="EPSG:4326")
iso_gdf.to_file("E:/public_transport_accessibility/data/processed/isochrones.geojson", driver="GeoJSON")
