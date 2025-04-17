import osmnx as ox

place_name = "Przemyśl, Poland"  # например: "Minsk, Belarus"
try:
    G = ox.graph_from_place(place_name, network_type='walk')  # пешие маршруты
    print("Граф успешно загружен.")
    
    save_path = "E:/public_transport_accessibility/data/processed/osm_graph.graphml" # путь к файлу
    ox.save_graphml(G, filepath=save_path)
    print(f"Граф сохранен в {save_path}.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
    