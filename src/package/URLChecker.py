import re
class URLChecker:
    def __init__(self, url):
        self.url = url
    #hasprotocol
    def checkProtocol(self):
        """Search for protocol in url string. Return true if exists"""
        #protocols = ('http','https','ftp')
        pattern_string = 'http:\/\/|https:\/\/|ftp:\/\/'
        pattern = re.compile(pattern_string)
        if pattern.search(self.url):
            return True
        else:
            return False
    #hasSubdomain
    def checkSubdomain(self):
        pattern_string='\w+\.\w+\.com|net'
        pattern = re.compile(pattern_string)
        if pattern.match(self.url):
            return "{0} has a subdomain".format(self.url)
        else:
            return "There is no subdomain in {0}".format(self.url)

    #hasPath
    def checkPath(self):
        #pattern_string='(com|net)\/.*'
        if self.url == True:
            noprotocol=self.url.split['://']
            return noprotocol[1].split('/')
        else:
            return self.url.split('/')[1]
