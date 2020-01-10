from datetime import datetime

from elasticsearch import Elasticsearch


def main():
    es = Elasticsearch(hosts={"host": "localhost", "port": 9200})

    doc = {
        'author': 'kimchy',
        'text': 'Elasticsearch: cool. bonsai cool.',
        'timestamp': datetime.now(),
    }

    res = es.index(index="test-index", doc_type='tweet', id=1, body=doc)
    print(res)


if __name__ == '__main__':
    main()