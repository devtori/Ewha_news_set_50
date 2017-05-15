#정답셋을 그나마 쉽게 만들어봅시다

import requests

from konlpy.tag import Twitter
from collections import Counter
from bs4 import BeautifulSoup as bs

twitter = Twitter()

#사이트 크롤링
url = input("url = ")
#url = "http://inews.ewha.ac.kr/news/articleView.html?idxno=19930"
res = requests.get(url)
soup = bs(res.content,'html.parser')
body = soup.select_one('#articleBody')
content = body.text
para = body.text.split('\n' or '\xa0')

#모든 문장 골라내기
sent=[]
for i in range(0, len(para)):
    temp = str(para[i]).split('. ')
    for j in range(0, len(temp)):
        if (temp[j] != '' and temp[j] != '\xa0\xa0' and temp[j] != '\r' and temp[j] != '\xa0' and temp[j] != '\xa0\x08' and temp[j] != '\x08\x08' and temp[j] != '\xa0\r') :
            sent.append(temp[j])

#모든 문장 형식에 맞게 출력
for i in range(0, len(sent)):
    print('"',sent[i],'",')

#문장개수
print(len(sent))

#인덱스와 함께 보기
for i in range(0, len(sent)):
    print(i)
    print(sent[i])
