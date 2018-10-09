import json
from App.classes.LineBuilder import create_ordered_line
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point

def buildLineFromJSON(path):
  data = json.load(open(path))
  return create_ordered_line(data)

def loadStations(stations, line):
  stations = pd.DataFrame(stations)
  stations = gpd.GeoDataFrame(stations, geometry = [Point(xy) for xy in zip(stations.longitude, stations.latitude)])
  stations = stations.drop(['latitude', 'longitude'], axis=1)
  rel_pos = [line.project(station.geometry) / line.length for index, station in stations.iterrows()]
  line_ids = list(map(lambda x: str(x)[0:3], list(stations.id)))
  station_ids = list(map(lambda x: str(x)[3:5], list(stations.id)))
  stations.loc[:,'relative_position'] = pd.Series(rel_pos, index=stations.index)
  stations.loc[:, 'line_id'] = pd.Series(line_ids, index=stations.index)
  stations.loc[:, 'station_id'] = pd.Series(station_ids, index=stations.index)
  return stations

# get the first 3 digits of the stop_id = route_id
# station ids are last 2 digits

# gold_line_stations_sorted = gold_line_stations.sort_values('relative_position').reset_index().drop(['index'], axis=1)
# gold_line_stations_sorted[['display_name','relative_position','approx_lat','approx_lon','geometry']]