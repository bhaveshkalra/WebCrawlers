import requests
from bs4 import BeautifulSoup

correct="Y"

for i in range(0,20):
    word=input("Enter your word:\n")
    data=requests.get("http://www.synonym.com/synonyms/"+word)

    soup=BeautifulSoup(data.text,"html.parser")
    
    try:
        syn1=soup.find('ul',{'class':"synonyms"})
        a=syn1.find_all('a')
        count=0
    
        print("Synonyms are:")
        for syn in a:    
            print(syn.string,)
            count+=1
            if count>10:
                break
        print("\n")
    except:
        print("there are no synonyms for this word")

    try:
        ant1=soup.find('ul',{'class':"antonyms"})
        a=ant1.find_all('a')
        count=0
        print("Antonyms are:")
    
        for ant in a:
            print(ant.string,)
            count+=1
            if count>10:
                break
        print("\n\n")
    except:
        print("there are no antonyms for this word")

    choice=input("Do you wish to continue and check for other words:(Yes/No)")
    if correct != (choice[0:1].upper()):
        break
    else:
        pass


