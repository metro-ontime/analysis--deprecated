python ./log_vehicle_positions.py lametro-rail 804
sqlite3 -header -csv ./log.db "SELECT * FROM lametro_rail_804;" > ./log.csv
