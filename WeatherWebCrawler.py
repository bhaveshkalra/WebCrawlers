import re
import urllib.request
from urllib.request import Request, urlopen

correct="Y"


for i in range(0,20):
    city=input("Enter any city :")

    url="https://www.weather-forecast.com/locations/"+city+"/forecasts/latest"

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    data=urlopen(req).read()

    message=data.decode("utf-8")

    m=re.search('span class="phrase">',message)
    start=m.end()
    end=start+300

    string1=message[start:end]
     
    m=re.search("</span>",string1)
    end=m.start()-1

    final=string1[0:end]
    print("The details of the weather of "+city.capitalize() +" are:\n"+final+"\n\n\n\n")

    choice=input("Do you wish to continue and check for other cities:(Yes/No)")
    if correct != (choice[0:1].upper()):
        break
    else:
        pass
 
