from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch([{"host": "172.21.144.1", "port": 9200, "scheme":"https"}], basic_auth=('elastic','-GQ-d39pR8iaZHhD83uo'))
print(es.ping())