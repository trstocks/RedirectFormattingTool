#get redirect from file, for now it'll be a placeholder

#the input should be a source and destination. The source shouldn't have the protocol
#and it may or may not have the legacy subdomain indicator(i.e. archive, roc, redirect)
#the url subdomain may also be listed as www, but should be updated to the correct legacy subdomain
source="northjersey.com/porkchop"
#we need to make sure the destination is a valid, reachable url.
#we need to make sure it has the protocol regardless of what the customer gives.
destination="https://en.wikipedia.org/wiki/Porky_Pig"




#exceptions should be common. Subdomains like offers. or static. wouldn't be managed in this tool as a source
#['offers','static']
class URLChecker:
    #hasprotocol
    protocols = ('http','https','ftp')
    def checkProtocol(url):
        protocols = ('http','https','ftp')
        #search for protocol in url string
        #return true if exists

    #hasSubdomain
    def checkSubdomain(url):
        pass

    #hasPath
#the results can print on the screen for now, but should ultimately be added to a file
class URLSource(object):
    pass

class Redirect(object):
    def __init__(self):
        pass
    def setSourceAndDestination(self, source, destination):
        self.source = source
        self.destination = destination
        #print(self.source + ' goes to ' + self.destination)

    def checkSource(self):
        #should match SITE.com/alias, www.SITE.com/alias or legacy subdomain
        s=self.source
        def checkSubdomain(s):
            s.split('.')

        split_from_slash = self.source.split('/')
        trailingslash = ""
        count = 0
        for item in split_from_slash:
            if count == 0:
                self.domain = item
            else:
                trailingslash = "/" + item
            count +=1
        print trailingslash
        #print self.source.count('/')
        #print split_from_slash.count('/')

        #print split_from_slash[1]
        #print self.source.split('.')
        #print self.source

a=Redirect()
a.setSourceAndDestination("google.com/cheese/danish","app.com")
a.checkSource()
