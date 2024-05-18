import sys
import requests
import socket
import json

if len(sys.argv)<2:
    print("usage "+sys.argv[0]+"<url>")
    sys.exit(1)

print(sys.argv)

req= requests.get("http://google.com")
print("\n"+str(req.headers))

gethostby_ = socket.gethostbyname(sys.argv[1])
print("the ip of "+sys.argv[1]+" is "+gethostby_+"\n")
req_two = requests.get("https://ipinfo.io/"+gethostby_+"/json")
resp_ = json.loads(req_two.text)

print(resp_)

print("location is: "+resp_['loc'])
print("region is: "+resp_['region'])