import re
import urllib.request
from urllib.request import Request,urlopen


correct="Y"

for i in range(0,20):
    try:
        word=input("Enter your Word:")

        url="http://dictionary.reference.com/browse/"+word

        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

        data=urlopen(req).read()

        decoded=data.decode("utf-8")

        m=re.search('meta name="description" content="',decoded)
        start=m.end()
        end=start+300

        string1=decoded[start:end]
         
        m=re.search("See more.",string1)
        end=m.start()-1

        finalString=string1[0:end]

        m=re.search("definition",finalString)
        start=m.end()+1
        Definition=finalString[start:]
        
        print(word.capitalize()+" defined as:"+Definition.capitalize()+".\n\n")

        choice=input("Do you wish to continue and check for other words:(Yes/No)")
        if correct != (choice[0:1].upper()):
            break
        else:
            pass

    except:
        print("Sorry,there is no such word in the dictionary.\n\n")

        choice=input("Do you wish to continue and check for other words:(Yes/No)")
        if correct != (choice[0:1].upper()):
            break
        else:
            pass
            
