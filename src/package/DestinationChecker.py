import requests
from URLChecker import URLChecker

class DestinationURL(URLChecker):
    def __init__(self, url):
        URLChecker.__init__(self,url)

    def ResolveURL(self):
        """URL should have content, not 404's or 500 errors"""
        print self.url
        r = requests.get(self.url)
        print r.status_code
a=DestinationURL('http://google.com')
a.ResolveURL()
