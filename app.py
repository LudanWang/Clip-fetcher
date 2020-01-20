import pymongo
import os
import json
from flask import Flask
from flask_restful import Api

app=Flask(__name__)
api = Api(app)

@app.route("/")
def home():
    return "Hello world"
@app.route("/insert")
def mongo():
    client = pymongo.MongoClient(os.environ['MONGODB_KEY'])
    db = client.test
    collection = db.ClipFetcher
    test = {
        'id': '20170101',
        'name': 'test',
        'age': 20,
        'gender': 'male'
    }
    collection.insert(test)

    return "OK"

@app.route("/db")
def mongo2():
    client = pymongo.MongoClient(os.environ['MONGODB_KEY'])
    db = client.test
    collection = db.ClipFetcher
    result = collection.find({'name': 'Jordan'})
    print(result)
    # print(os.environ['MONGODB'])
    
    return "OK"

@app.route("/delete")
def mongo3():
    client = pymongo.MongoClient(os.environ['MONGODB_KEY'])
    db = client.test
    collection = db.ClipFetcher
    result = collection.remove({'name': '*'})
    print(result)
    
    return 'OK'

@app.route("/count")
def count():
    client = pymongo.MongoClient(os.environ['MONGODB_KEY'])
    db = client.test
    collection = db.ClipFetcher
    count = collection.find().count()

    # return api.add_resource(count)
    return json.dumps(count)


if __name__=="__main__":
    app.run(port=5001)