import urllib.request
from .MetroResponse import MetroResponse

class MetroRequest:
    def __init__(self, url):
        self.req = urllib.request.Request(url)
        self.req.add_header('Accept', 'application/json')

    def make(self):
        return MetroResponse(urllib.request.urlopen(self.req))

