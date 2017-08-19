"""import itertools as e

a=open("a.txt","wb+")
#r=open("al.txt","r")

averg=['55', '53', '54', '99', '98', '22', '23', '24']
numb= ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

#word=map(str,r.read().splitlines())
s=0
for d in averg:
 for i in e.product(numb,repeat=6):
	s+=1
	for j in i:
		 j.replace("\n","")
	a.write(d+(''.join(i))+'\r\n')
	print s," word :" ,d+("".join(i))


print "[*] done building the world list"


a.close()
r.close()
"""



import socket as s
from  time import time as t
import urllib,urllib2
data = urllib.urlencode({'user' : 'med','pass'  : '96451827med'})
b=t()
content = urllib2.urlopen(url="http://127.0.0.1:80/inner/pass", data=data)
print "[*] burning time" ,t()-b
print content.read()

