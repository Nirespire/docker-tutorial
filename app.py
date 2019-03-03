from flask import Flask
from redis import Redis, RedisError
import os
import socket
from pymongo import MongoClient

# Connect to Mongo
mongo_host = os.getenv('MONGO_HOST') or 'localhost'
client = MongoClient(host=mongo_host, port=27017, connectTimeoutMS=100, serverSelectionTimeoutMS=100)

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>Cannot connect to Redis, counter disabled</i>"

    try:
        db = client.testdb
        collection = db.test_collection
        results = collection.find_one()
    except:
        results = "<i>Cannot connect to Mongo, no results fetched</i>"

    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname} <br/>" \
           "<b>Mongo data:</b> {results} <br/>" \
           "<b>Visits:</b> {visits} "

    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits, results= str(results))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)