import requests, json, os
from elasticsearch import Elasticsearch

directory = '/home/angel/TFG/2019-tfg-angel-perea/Django-prototype/prototypePolls/logs/temporalDir/'


res = requests.get('http://localhost:9200')
print (res.content)
es = Elasticsearch([{'host': 'localhost', 'port': '9200'}])

i = 1

for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        f = open(filename)
        docket_content = f.read()
        # Send the data into es
        es.index(index='myindex', ignore=400, doc_type='docket',
        id=i, body=json.loads(docket_content))
        i = i + 1
