from .Request import MetroRequest

class Metro:
    def get_vehicles(agency, line):
        query = f"http://api.metro.net/agencies/{agency}/routes/{line}/vehicles/"
        req = MetroRequest(query)
        return req.make()
