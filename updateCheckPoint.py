import os
import certifi
from checkPoint import CheckPoint
from checkPointRepository import CheckPointRepository
from dotenv import load_dotenv
from pymongo import MongoClient

def query_mongodb():
    print("Querying MongoDB")
    
    mongo_uri = os.getenv('MONGO_URI')
    mongo_db = os.getenv('MONGO_DB')
    mongo_collection = os.getenv('MONGO_COLLECTION')

    client = MongoClient(mongo_uri,tls=True,tlsCAFile=certifi.where())
    db = client[mongo_db]
    
    
    
    checkpoint_repository = CheckPointRepository(db)
    retrieve_checkpoints = checkpoint_repository.find_with_filter({"last_activity":"PENDING", "entity_type":"tenant"})
    print("Retrieved checkpoints:", retrieve_checkpoints.count())
    documentToBeUpdated = retrieve_checkpoints[0]
    documentToBeUpdated['last_activity'] = "COMPLETED"
    print(documentToBeUpdated['last_activity'])
    checkpoint_repository.update_one(documentToBeUpdated['execution_id'], documentToBeUpdated)
    
    
    documents = retrieve_checkpoints
    for doc in documents:
       print(doc)

if __name__ == "__main__":
    load_dotenv()
    query_mongodb()