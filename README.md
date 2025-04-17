# Public Transport Accessibility Analysis🚍

**RU 🇷🇺 | EN 🇬🇧**

---

## 🧭 Описание | Description

**RU:**  
Этот проект анализирует доступность общественного транспорта, строя **изохроны** — зоны, до которых можно добраться пешком от остановок за определённое время (например, 5, 10, 15 минут).  
Используются данные **OpenStreetMap** и **GTFS**, а также библиотеки Python: `osmnx`, `networkx`, `geopandas`.

Данные:

    OpenStreetMap:
        Используется библиотека osmnx для загрузки уличной сети

    GTFS:
        Скачайте архив GTFS для вашего города на transitfeeds.com или официальных сайтах транспортных операторов. Распакуйте его в data/raw/

**EN:**  
This project performs a transit accessibility analysis by generating **isochrones** (travel-time zones) from public transport stops.  
It uses **OpenStreetMap** and **GTFS** data, along with Python libraries: `osmnx`, `networkx`, and `geopandas`.

Data:
    
    OpenStreetMap:
        Used osmnx library to load street network

    GTFS:
        Download the GTFS archive for your city at transitfeeds.com or official websites of transport operators. Unzip it to data/raw/

##  Структура проекта | Project Structure 

```
public_transport_accessibility/
├── data/
│   ├── raw/              # Raw data: OSM, GTFS
│   ├── processed/        # Processed data: graphs, isochrones
├── scripts/              # Processing and analysis scripts
├── requirements.txt      # Python dependencies list
└── README.md             # Project description
```

## ⚙️ Установка | Setup


```bash
python -m venv venv
source venv/bin/activate  # или venv\Scripts\activate на Windows

pip install -r requirements.txt


