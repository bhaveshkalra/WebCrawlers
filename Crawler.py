#crawling the weather from web using beautiful soup

import urllib.request
from urllib.request import Request,urlopen
from bs4 import *
city=input("enter your city and country as:(country/city)\n")
url="https://www.accuweather.com/en/"+city+"/10007/weather-forecast/349727"

#request_data=requests.get("https://www.accuweather.com/en/us/new-york-ny/10007/weather-forecast/349727")

request_data = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

data=urlopen(request_data).read()

html=data.decode("utf-8")
soup=BeautifulSoup(html,"html.parser")

info=soup.find('div',{'class':'info'})
#print(info)

temp=info.find('span',{'class':'large-temp'}).contents
temp.append(info.find('span',{'class':'real-feel'}).contents)


print("Temp is:"+temp[0]+"F  \tfeels like:"+temp[1][0]+"F")


##not working properly
#working for only a a particluar city NewYork
