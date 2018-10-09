from shapely.geometry import Point
import geopandas as gpd
import pandas as pd

def rawLogToGDF(log):
  log['datetime'] = pd.to_datetime(log['report_date'] + ' ' + log['report_time'])
  log = log.drop_duplicates(subset=['datetime', 'lat', 'lon', 'vehicle_id'])
  log = log.set_index(pd.DatetimeIndex(log['datetime']))
  log = log.drop(['report_date', 'report_time', 'id', 'datetime'], axis=1)
  log = log.sort_index()
  geometry = [Point(xy) for xy in zip(log.lon, log.lat)]
  return gpd.GeoDataFrame(log[['vehicle_id', 'direction']], crs = {'init': 'epsg:4326'}, geometry = geometry)
  
def selectAnalysisWindow(log, start_date, end_date):
  start_date = pd.to_datetime(start_date)
  end_date = pd.to_datetime(end_date)
  return log[start_date:end_date].reset_index()

def findRelativePositions(positions, line):
  relative_positions = [line.project(position.geometry) / line.length for index, position in positions.iterrows()]
  positions.loc[:,'relative_position'] = pd.Series(relative_positions, index=positions.index)
  return positions

def analyzeSelection(log, stations, line):
  log = findRelativePositions(log, line)
  for index, train in log.iterrows():
    surrounding_stops = find_surrounding_stops(train.relative_position, train.direction, stations)
    previous_stop = surrounding_stops[0]
    next_stop = surrounding_stops[1]
    log.loc[index, 'previous_stop'] = previous_stop['display_name']
    log.loc[index, 'next_stop'] = next_stop['display_name']
  return log
  
def find_surrounding_stops(relative_pos_of_train, direction, stations):
    reverse = direction / 180
    next_stop = None
    previous_stop = None
    for index, station in stations.iterrows():        
        if relative_pos_of_train < station.relative_position:
            next_stop = stations.loc[max(index - reverse, 0)]
            previous_stop = stations.loc[max(index - 1 + reverse, 0)]
            break
    if (next_stop is None):
        next_stop = {"display_name": "EOL"}
    if (previous_stop is None):
        previous_stop = {"display_name": "EOL"}
    return [previous_stop, next_stop]
          