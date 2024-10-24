import http.client as httplib, urllib
import zlib
import time
headers = {
"Host": "khalti.com",
"User-Agent": "/*deleted*/",
"Accept": "application/json, text/plain, */*",
"Accept-Language": "en-US,en;q=0.5",
"Accept-Encoding": "gzip, deflate, br",
"X-CSRFToken": "/*deleted*/",
"Connection": "keep-alive",
"Referer": "https://khalti.com/",
"Cookie": "/*deleted*/"}

for i in range(275):#may be need to change this now....
    conn = httplib.HTTPSConnection("khalti.com")
    conn.request("GET","/api/v2/vuservote/?page="+str(i+1),"",headers)
    res=conn.getresponse()
    print(res.status, res.reason)
    data=res.read()
    data=zlib.decompress(data,16+zlib.MAX_WBITS)
    print(len(data))
    conn.close()
    open(str(i+1)+".txt","wb").write(data)
