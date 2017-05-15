# 정답셋으로 설정한 문장들과 각 문단의 첫문장들의 유사도 계산하기

import json
import codecs
import requests

from konlpy.tag import Twitter
from collections import Counter
from bs4 import BeautifulSoup as bs

twitter = Twitter()


num = input("json 번호 = ")
index = num + '.json'

with codecs.open(index, encoding='utf-8') as data_file:
    data = json.loads(data_file.read())


url = data["source"]
res = requests.get(url)
soup = bs(res.content,'html.parser')
body = soup.select_one('#articleBody')
para = body.text.split('\n' or '\xa0')


first = []
sent = []
F = []
S = []

for i in range(0, len(para)):
    temp = str(para[i]).split('. ')
    if(temp[0] != '' and temp[0] != '\xa0\xa0' and temp[0] != '\r' and temp[0] != '\xa0' and temp[0] != '\xa0\x08' and temp[0] != '\x08\x08' and temp[0] != '\xa0\r'):
        first.append(str(temp[0]))

for i in range(0, len(data["summaries"])):
    sent.append(data["sentences"][data["summaries"][i]])


for i in range(0, len(first)):
    F = F + (twitter.pos(first[i], norm=True, stem=True))
F = list(set(F))

for i in range(0, len(sent)):
    S = S + (twitter.pos(sent[i], norm=True, stem=True))
S = list(set(S))


total = F + S
same = []

for i in range (0, len(F)):
    for j in range (0, len(S)):
        if (F[i]==S[j]):
            total.remove(S[j])
            same.append(S[j])

Tl = len(total)
Sl = len(same)

result = Sl/Tl * 100

print(Tl,'개의 형태소 중', Sl,'개의 형태소 일치')
print(round(result,3),'% similar')
print('\n 일치 형태소')
print(same)
