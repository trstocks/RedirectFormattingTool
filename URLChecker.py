import re
class URLChecker:
    #hasprotocol
    def checkProtocol(self,url):
        """Search for protocol in url string. Return true if exists"""
        #protocols = ('http','https','ftp')
        pattern_string = "http:\/\/|https:\/\/|ftp:\/\/"
        pattern = re.compile(pattern_string)
        if pattern.search(url):
            return True
        else:
            return False
    #hasSubdomain
    def checkSubdomain(self,url):
        pattern_string="\w+\.\w+\.com|net"
        pattern = re.compile(pattern_string)
        if pattern.match(url):
            return "{0} has a subdomain".format(url)
        else:
            return "There is no subdomain in {0}".format(url)

    #hasPath
    def checkPath(self,url):
        pass
