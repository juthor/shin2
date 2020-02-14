#10. 공공/단체
from bs4 import BeautifulSoup
from pprint import pprint #예쁘게 출력하기 위한 용도
import requests
import urllib.request
import re
import pandas as pd


#웹페이지 열고 소스코드 읽기
response=requests.get("https://www.shinhancard.com/conts/person/card_info/dream/credit/life/1210252_46588.jsp")




html=response.text 
soup = BeautifulSoup(html,'html.parser')

cardname=soup.find('h1', class_='shcd-card-name')
keywords = soup.find_all('div', class_='cardName')
annual=soup.select('div.shcd-card-spec>dl.shcd-card-annual-fee>dd')


#get_text() == 데이터에서 문자열만 추출
#strip() == 데이터의 양옆 공백제거

keywords = [each_line.get_text().strip() for each_line in keywords[:10]]
annual=[each_line.get_text().strip() for each_line in annual[:]]

name=[]
name.insert(1, cardname.get_text())

dotdetails=soup.select('#pbTabDepth1-1 li')
dotdetails=[each_line.get_text().strip() for each_line in dotdetails[:]]

temp=str()
for x in range (len(keywords)):
    temp+=str(keywords[x])+"-"+str(dotdetails[x])+","+"\n"    

#print(temp)
detail=[]
detail.insert(1, temp)


data={"name":name, "annual":annual, "detail":detail}
db=pd.DataFrame(data, columns=["name", "annual", "detail"])
#db.to_csv('DB.csv', mode='a', header=False, index=True)
db.to_csv('db.csv', encoding='cp949')

