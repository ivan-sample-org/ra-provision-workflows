"""
 Helper script to update check point in MongoDB
 author: Ivan Hidalgo
 date: 2024-09-09
 
 python updateCheckPoint.py "REGISTERED" "tenant" "86a3710a-6357-482c-8896-1bdf1abce7ae"
 
""" 

import os
import sys
import certifi
from checkPoint import CheckPoint
from checkPointRepository import CheckPointRepository
from dotenv import load_dotenv
from pymongo import MongoClient

DEFAULT_LAST_ACTIVITY = "REGISTERED"
DEFAULT_ENTITY_TYPE = "tenant"
DEFAULT_EXECUTION_ID = ""

def query_mongodb(execution_id=DEFAULT_EXECUTION_ID, last_activity = DEFAULT_LAST_ACTIVITY, entity_type = DEFAULT_ENTITY_TYPE):
    
    print("Updating check point in MongoDB")
    
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
    retrieve_checkpoints = list(checkpoint_repository.find_with_filter({"entity_type": entity_type, "execution_id": execution_id}))
    print(f"Retrieved {checkpoint_repository.count()} checkpoints with last_activity: {last_activity} and entity_type: {entity_type} and execution_id: {execution_id}")
    if len(retrieve_checkpoints) == 0:
        print(f"No checkpoints found with last_activity: {last_activity} and entity_type: {entity_type} and execution_id: {execution_id}")
        return
    documentToBeUpdated = retrieve_checkpoints[0]
    documentToBeUpdated['previous_activity'] = documentToBeUpdated['last_activity']
    documentToBeUpdated['last_activity'] = last_activity
    print(f"Updating document with last_activity: {documentToBeUpdated['last_activity']} and previous_activity: {documentToBeUpdated['previous_activity']}")
    checkpoint_repository.update_one(documentToBeUpdated['execution_id'], documentToBeUpdated)
    
    documents = retrieve_checkpoints
    for doc in documents:
       print(doc)

if __name__ == "__main__":
    load_dotenv()
    
    if len(sys.argv) == 4:
        if sys.argv[1] is not None:
            last_activity = sys.argv[1]
        else:
            last_activity = DEFAULT_LAST_ACTIVITY 
        if sys.argv[2] is not None:    
            entity_type = sys.argv[2]
        else:
            entity_type = DEFAULT_ENTITY_TYPE
        if sys.argv[3] is not None:
            execution_id = sys.argv[3]
        else:
            execution_id = DEFAULT_EXECUTION_ID
    
    print(f"Updating check point with last_activity: {last_activity} and entity_type: {entity_type} and execution_id: {execution_id}")
    
    query_mongodb(execution_id, last_activity, entity_type)