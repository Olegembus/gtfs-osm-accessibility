import networkx as nx
import osmnx as ox

# Загрузка графа из файла
input_path = "E:/public_transport_accessibility/data/processed/osm_graph.graphml"
G = ox.load_graphml(input_path)

# Преобразуем граф в формат, где ребра имеют значение travel_time
G = ox.add_edge_speeds(G)
G = ox.add_edge_travel_times(G)

# Сохранение графа с добавленным временем в тот же каталог
output_path = "E:/public_transport_accessibility/data/processed/osm_graph_with_time.graphml"
ox.save_graphml(G, output_path)
