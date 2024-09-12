"""
This module contains the CheckPoint model.
author: Ivan Hidalgo
date: 2024-09-09

"""

from typing import Optional

class CheckPoint:
    
    def __init__(self, execution_id, created_date, origin, env, cluster_index, entity_type,
                 tenant_id, user_id, user_email, previous_activity, last_activity, tier, 
                 catalog_number, error_code, error_description):
        self.execution_id = execution_id
        self.createdDate = created_date
        self.origin = origin
        self.env = env
        self.cluster_index = cluster_index
        self.entity_type = entity_type
        self.tenant_id = tenant_id
        self.catalog_number = catalog_number
        self.user_id = user_id
        self.user_email = user_email
        self.previous_activity = previous_activity
        self.last_activity = last_activity
        self.tier = tier
        self.error_code = error_code
        self.error_description = error_description
    