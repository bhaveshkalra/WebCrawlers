#two modules in this app re and urllib.request
import re
import urllib.request
from urllib.request import Request, urlopen

stocks=["FB","DAL","GOOG","NIFTY","BABA"]
stock=input("Enter your stock:")

url="https://www.google.com/finance?q="

url=url+(stock.upper())   

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
data=urlopen(req).read()

data1=data.decode("utf-8")
#print(data1)

m=re.search('<span style="white-space:normal;word-spacing:6px"> ',data1)
#print(m)
start=m.start()
end=start+200
string1=data1[start:end]
#print(string1)

m=re.search('<span>',string1)
start=m.end()
string2=string1[start:]
#print(string2)

m=re.search("</span>",string2)
end=m.start()

final=string2[0:end]
print("The value of stock of "+stock.upper()+" is:\n" + final)
