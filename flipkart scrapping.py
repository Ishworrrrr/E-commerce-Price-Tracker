from bs4 import BeautifulSoup
import requests
from time import sleep
import time
from pushbullet import Pushbullet

def flip_tracking(u):
    url=u
    r=requests.get(url)
    htmlContent=r.content
    print(r.raise_for_status) 
    soup=BeautifulSoup(htmlContent,'html.parser')
    
    p1=soup.find('div',class_="_30jeq3 _16Jk6d").text.strip('₹')
    p2=int(p1.replace(',',''))
    
    return(p2)


web="https://www.flipkart.com/boat-rockerz-551-anc-hybrid-anc-100-hrs-playback-40mm-drivers-asap-charge-bluetooth-headset/p/itmbd436ac6c4964?pid=ACCGZYG5EDAVXZQ8&lid=LSTACCGZYG5EDAVXZQ89IQVU0&marketplace=FLIPKART&q=boat+rockerz+551+anc&store=0pm%2Ffcn%2Fgc3%2Fka8&spotlightTagId=FkPickId_0pm%2Ffcn%2Fgc3%2Fka8&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_2_15_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_2_15_na_na_ps&fm=search-autosuggest&iid=430198e1-11cd-4e8a-a111-68c5e48668e4.ACCGZYG5EDAVXZQ8.SEARCH&ppt=sp&ppn=sp&ssid=58ppqevbvk0000001691074942975&qH=ea6b3bca0cba8b6b"

price=flip_tracking(web)

#h=int(time.strftime("%H"))
#m=int(time.strftime("%M"))
print(price)
if(price<500):
    API_KEY="o.ocsvFPtkFiRYk87ne1k2dWzqSru0nYko"
    pb=Pushbullet(API_KEY)
    push=pb.push_note("Headphone's price:", str(price))

time.sleep(3600)
