import os
from pymongo import MongoClient

def query_mongodb():
    print("Querying MongoDB")
    mongo_uri = os.getenv('MONGO_URI')
    mongo_db = os.getenv('MONGO_DB')
    mongo_collection = os.getenv('MONGO_COLLECTION')

    client = MongoClient(mongo_uri)
    db = client[mongo_db]
    collection = db[mongo_collection]

    documents = collection.find()
    for doc in documents:
        print(doc)

if __name__ == "__main__":
    query_mongodb()