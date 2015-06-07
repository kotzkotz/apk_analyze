import urllib2,httplib
class SmartRedirectHandler(urllib2.HTTPRedirectHandler):     
    def http_error_301(self, req, fp, code, msg, headers):  
        result = urllib2.HTTPRedirectHandler.http_error_301( 
            self, req, fp, code, msg, headers)              
        result.status = code                                 
        return result                                       

    def http_error_302(self, req, fp, code, msg, headers):  
        result = urllib2.HTTPRedirectHandler.http_error_302(
            self, req, fp, code, msg, headers)              
        result.status = code                                
        return result    

def get(url):
	request = urllib2.Request(url)
	httplib.HTTPConnection.debuglevel = 1
	opener = urllib2.build_opener(SmartRedirectHandler())
	f = opener.open(request)
	return f.url
	return f.status


#print get("http://apk.hiapk.com/appdown/com.moji.mjweather")
