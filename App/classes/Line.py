import json
from App.classes.LineBuilder import create_ordered_line
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
from App.classes.Tracker import findRelativePositions

def buildLineFromJSON(path):
  data = json.load(open(path))
  return create_ordered_line(data)

def loadStations(stations, line):
  stations = pd.DataFrame(stations)
  stations = gpd.GeoDataFrame(stations, geometry = [Point(xy) for xy in zip(stations.longitude, stations.latitude)])
  stations = stations.drop(['latitude', 'longitude'], axis=1)
  stations = findRelativePositions(stations, line)
  stations = parseStopIds(stations)
  return stations

def parseStopIds(stationList):
  line_ids = list(map(lambda x: str(x)[0:3], list(stationList.id)))
  station_ids = list(map(lambda x: str(x)[3:5], list(stationList.id)))
  stationList.loc[:, 'line_id'] = pd.Series(line_ids, index=stationList.index)
  stationList.loc[:, 'station_id'] = pd.Series(station_ids, index=stationList.index)
  return stationList
