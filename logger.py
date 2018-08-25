from classes.Table import Table
from classes.Database import Database
from classes.Metro import Metro

line = '804'
agency = 'lametro-rail'

tracking_data = Database('log.db')
table = Table('lametro-rail', '804')

tracking_data.execute(table.create())
vehicle_positions = Metro.get_vehicles(agency, line)

def all_fields_present(obj):
    necessary_fields = ['id', 'seconds_since_report', 'route_id', 'latitude', 'longitude', 'heading']
    if all (key in obj for key in necessary_fields):
        return True
    return False

timestamp = vehicle_positions.timestamp()
for vehicle in vehicle_positions.parse():
    if all_fields_present(vehicle):
        vehicle['timestamp'] = timestamp - int(vehicle['seconds_since_report']) # get offset, REFACTOR THIS
        tracking_data.cursor.execute(table.insert(), [float(vehicle['timestamp']), int(vehicle['id']),int(vehicle['route_id']), float(vehicle['latitude']), float(vehicle['longitude']), float(vehicle['heading'])])

tracking_data.save_and_close()
print("DONE")

