import json
import sqlite3
import urllib.request
from datetime import datetime

# Set line and agency
line = '804'
agency = 'lametro-rail'

#open database
conn = sqlite3.connect('log.db')
c = conn.cursor()

# Define SQL commands and URLs
create_db = f"CREATE TABLE IF NOT EXISTS log_{line} (id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp DATETIME NOT NULL, vehicle_id INTEGER NOT NULL, route_id INTEGER NOT NULL, lat REAL NOT NULL, lon REAL NOT NULL, direction REAL NOT NULL)"
insert_row = f"INSERT INTO log_{line} (timestamp, vehicle_id, route_id, lat, lon, direction) VALUES (?, ?, ?, ?, ?, ?)"
vehicles_url = f"http://api.metro.net/agencies/{agency}/routes/{line}/vehicles/"

c.execute(create_db)

# get vehicles data from API
req = urllib.request.Request(vehicles_url)
req.add_header('Accept', 'application/json')
response = urllib.request.urlopen(req)
data = response.read()

# derive timestamp from datetime string in returned header
time_string = response.info()['Date']
date_obj = datetime.strptime(time_string, '%a, %d %b %Y %H:%M:%S %Z')
ts = date_obj.timestamp()

# load data into dict object and access array of items
parsed = json.loads(data)
items = parsed["items"]

# these fields must be present in each item for data to be valid
fields = ['id', 'seconds_since_report', 'route_id', 'latitude', 'longitude', 'heading']
# list of valid items
valid = []
# check all fields are present
for vehicle in items:
    for field in fields:
        if not field in vehicle.keys():
            all_fields_present = False
            break
        else:
            all_fields_present = True
    if all_fields_present == True:
        # push vehicle into valid array
        valid.append(vehicle)

for vehicle in valid:
    # calculate timestamp of each position entry and add key to dict
    vehicle['timestamp'] = ts - int(vehicle['seconds_since_report'])
    # insert each vehicle position entry into database
    c.execute(insert_row, [float(vehicle['timestamp']), int(vehicle['id']),int(vehicle['route_id']), float(vehicle['latitude']), float(vehicle['longitude']), float(vehicle['heading'])])

conn.commit()
conn.close()
print("DONE")

