from redis import StrictRedis
from rq import Worker, Queue, Connection
from sqlalchemy import Table, Column, Integer, String, ForeignKey
import requests, sqlalchemy

listen = ['default']

redis_url = 'redis://:redis.flask-rq@redis:6379'

conn = StrictRedis.from_url(redis_url)

postgres_url = 'postgresql://0rzuvvvi:5efnbj173cea5bt5796un@postgres.flask-rq:5432/postgres'

postgres_con = sqlalchemy.create_engine(postgres_url, client_encoding='utf8')

meta = sqlalchemy.MetaData(bind=postgres_con, reflect=True)

def count_words_at_url(url):
    url = 'http://'+url
    resp = requests.get(url)
    result = len(resp.text.split())
    clause = meta.tables['jobs'].insert().values(results=result)
    entry = postgres_con.execute(clause)
    print result, entry.inserted_primary_key

if __name__ == "__main__":
  with Connection(conn):
    worker = Worker(listen)
    worker.work()