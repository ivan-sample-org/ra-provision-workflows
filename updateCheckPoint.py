"""
This script queries the MongoDB database for the last checkpoint with the given last_activity and entity_type.
author: Ivan Hidalgo
date: 2024-09-09

python3 getCheckPoint.py COMPLETED tenant 

"""

import sys
import os
import certifi
from checkPoint import CheckPoint
from checkPointRepository import CheckPointRepository
from dotenv import load_dotenv
from pymongo import MongoClient

DEFAULT_LAST_ACTIVITY = "REGISTERED"
DEFAULT_ENTITY_TYPE = "tenant"

def query_mongodb(last_activity = "REGISTERED", entity_type = "tenant"):
    
    print("Fetching last check point in MongoDB")
   
    
    mongo_uri = os.getenv('MONGO_URI')
    if not mongo_uri:
        raise ValueError("MONGO_URI environment variable is not set")
        
    mongo_db = os.getenv('MONGO_DB')
    if not mongo_db:
        raise ValueError("MONGO_DB environment variable is not set")
    
    mongo_collection = os.getenv('MONGO_COLLECTION')
    if not mongo_collection:
        raise ValueError("MONGO_COLLECTION environment variable is not set")

    client = MongoClient(mongo_uri,tls=True,tlsCAFile=certifi.where())
    db = client[mongo_db]
    print(f"Connected to {mongo_db} database")
    
    
    
    checkpoint_repository = CheckPointRepository(db)
    retrieve_checkpoints = list(checkpoint_repository.find_with_filter({"last_activity": last_activity, "entity_type": entity_type}))
    if len(retrieve_checkpoints) == 0:
        print(f"No checkpoints found with last_activity: {last_activity} and entity_type: {entity_type}")
        return
    
    documents = retrieve_checkpoints
    for doc in documents:
       print(doc)

if __name__ == "__main__":
    load_dotenv()
    
    if len(sys.argv) == 2:
        if sys.argv[1] is not None:
            last_activity = sys.argv[1]
        else:
            last_activity = DEFAULT_LAST_ACTIVITY 
        if sys.argv[2] is not None:    
            entity_type = sys.argv[2]
        else:
            entity_type = DEFAULT_ENTITY_TYPE
    else:
        last_activity = DEFAULT_LAST_ACTIVITY
        entity_type = DEFAULT_ENTITY_TYPE
    
    print(f"Querying MongoDB with last_activity: {last_activity} and entity_type: {entity_type}")
    
    query_mongodb(last_activity, entity_type)