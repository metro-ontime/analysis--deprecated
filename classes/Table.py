class Table:
    def __init__(self, agency, line):
        self.agency = agency
        self.line = line

    def create(self):
        line = self.line
        return f"CREATE TABLE IF NOT EXISTS log_{line} (id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp DATETIME NOT NULL, vehicle_id INTEGER NOT NULL, route_id INTEGER NOT NULL, lat REAL NOT NULL, lon REAL NOT NULL, direction REAL NOT NULL)"

    def insert(self):
        line = self.line
        return f"INSERT INTO log_{line} (timestamp, vehicle_id, route_id, lat, lon, direction) VALUES (?, ?, ?, ?, ?, ?)"

