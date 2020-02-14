#10. 공공/단체
from bs4 import BeautifulSoup
from pprint import pprint #예쁘게 출력하기 위한 용도
import requests
import urllib.request
import re
import pandas as pd


#웹페이지 열고 소스코드 읽기
url="https://www.shinhancard.com/conts/person/card_info/dream/credit/life/1540955_46588.jsp"
req = urllib.request.urlopen(url)
res = req.read()
 
soup = BeautifulSoup(res,'html.parser')
cardname=soup.find('h1', class_='shcd-card-name')
keywords = soup.find_all('div', class_='cardName')
details=soup.select('shcd-card-annual-free')
print(details)

#get_text() == 데이터에서 문자열만 추출
#strip() == 데이터의 양옆 공백제거
#[:20]의 이유? 인기검색어의 중복을 막고 20위까지만 출력하기 위함
keywords = [each_line.get_text().strip() for each_line in keywords[:10]]

print(cardname.get_text())
print(keywords)

