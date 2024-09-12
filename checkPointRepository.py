class CheckPointRepository:
    
    __collection__ = 'provision-state-machine'
    __database__ = 'deployment'
    
    def __init__(self, db):
        self.collection = db['provision-state-machine']

    def save(self, checkpoint):
        checkpoint_data = {
            'execution_id': checkpoint.execution_id,
            'createdDate': checkpoint.createdDate,
            'origin': checkpoint.origin,
            'env': checkpoint.env,
            'cluster_index': checkpoint.cluster_index,
            'entity_type': checkpoint.entity_type,
            'tenant_id': checkpoint.tenant_id,
            'user_id': checkpoint.user_id,
            'user_email': checkpoint.user_email,
            'previous_activity': checkpoint.previous_activity,
            'last_activity': checkpoint.last_activity,
            'tier': checkpoint.tier,
            'catalog_number': checkpoint.catalog_number,
            'error_code': checkpoint.error_code,
            'error_description': checkpoint.error_description
            
        }
        self.collection.insert_one(checkpoint_data).inserted_id

    def update_one(self, execution_id, checkpoint_data):
        self.collection.update_one({'execution_id': execution_id}, {'$set': checkpoint_data}, upsert=True)
    
    def find(self, execution_id):
        return self.collection.find_one({'execution_id': execution_id})
    
    def find_all(self):
        return self.collection.find()  
    
    def find_with_filter(self, filter):
        return self.collection.find(filter)
    
    def delete(self, execution_id):
        self.collection.delete_one({'execution_id': execution_id})
    
    def delete_all(self):
        self.collection.delete_many({})
    
    def count(self):
        return self.collection.count_documents({})
    
    

    