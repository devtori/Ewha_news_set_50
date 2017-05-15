#만들어진 정답셋 확인하기


import json
import codecs
from pprint import pprint


num = input("json 번호 = ")
index = num + '.json'

with codecs.open(index, encoding='utf-8') as data_file:
    data = json.loads(data_file.read())

pprint(data)
