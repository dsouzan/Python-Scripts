#!/usr/bin/env python
import httplib
conn = httplib.HTTPConnection("smartrgtrial.smartrg.com")
conn.request("HEAD", "/")
r1 = conn.getresponse()
print r1.status, r1.reason
print "www.smartrgtrial.smartrg.com is up"

conn = httplib.HTTPConnection("test52.smartrg.com")
conn.request("HEAD", "/")
r1 = conn.getresponse()
print r1.status, r1.reason
print "www.test52.smartrg.com is up"




