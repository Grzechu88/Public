# -*- coding: utf-8
"""
Created on Sat Aug 24 07:39:43 2019

@author: Grzechu
"""
import requests
import pandas as pd
from bs4 import BeautifulSoup

#url = 'https://www.efortuna.pl/pl/strona_glowna/pilka-nozna/' + str(date.today()) + '?tickLeft=0&selectDates=1&tickRight=0'
url = 'https://www.efortuna.pl/zaklady-bukmacherskie/pi%C5%82ka-nozna/ekstraklasa-polska?selectDates=1'

response = requests.get(url)    
if response is False:
    print("Error " + str(response))
    exit()

soup = BeautifulSoup(response.text, 'lxml')

#events = soup.select('.toggable_row')
events = soup.select('td')

lsData = []
lsOdds = []
#for event in events:
#    event_name = event.select('.bet_item_detail_href')
#    event_id = event.select('.bet_item_info_id')
#    odds = event.select('.col_bet')
#    event_date = event.select('.col_date')
#    event_stripped = event_name[0].text
#    event_id_stripped = event_id[0].text
#    date_stripped = event_date[0].text.strip()
#    lsOdds = [singlebet.text.strip() for singlebet in odds]
#    lsData.append([event_stripped, event_id_stripped, lsOdds, date_stripped])
print(len(events[2].select('.odds-value')))

for event in events:
    if len(event.select('.market-name')) > 0:
        event_name = event.select('.market-name')
        event_stripped = event_name[0].text
    elif len(event.select('.odds-value')) > 0:
        event_odd = event.select('.odds-value')
        lsOdds.append(event_odd[0].text)
    elif len(event.select('.event-datetime')) > 0:
        event_date = event.select('.event-datetime')
        date_stripped = event_date[0].text.strip()
        lsData.append([event_stripped, lsOdds, date_stripped])
        lsOdds = []

dfList = pd.DataFrame(lsData)
dfList.to_csv("output.csv")