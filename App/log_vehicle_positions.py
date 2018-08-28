import sys
from classes.Table import Table
from classes.Database import Database
from classes.Metro import Metro

if len(sys.argv) != 3:
    print('Please provide the agency and line number')
    exit()

agency = str(sys.argv[1])
agency_sanitized = agency.replace('-', '_')
line = str(sys.argv[2])

tracking_data = Database('log.db')
table = Table(agency_sanitized, line)

tracking_data.execute(table.create())
vehicles = Metro.get_vehicles(agency, line)
server_time = int(vehicles.timestamp())

for vehicle in vehicles.parse():
    if table.all_fields_present(vehicle):
        tracking_data.cursor.execute(
                table.insert(), 
                [
                    int(server_time), 
                    int(vehicle['seconds_since_report']),
                    int(vehicle['id']), 
                    float(vehicle['latitude']), 
                    float(vehicle['longitude']), 
                    float(vehicle['heading'])
                ]
            )

tracking_data.save_and_close()
