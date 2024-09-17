"""
This module contains the CheckPoint model.
author: Ivan Hidalgo
date: 2024-09-09

"""

from typing import Optional
from uuid import uuid4
import datetime
from pymongo import MongoClient
from pydantic import BaseModel, Field

class CheckPoint(BaseModel):
    
    id: str = Field(default_factory=uuid4, alias="_id")
    execution_id: Optional[str] = Field(None, alias="execution_id")
    createdDate: str = Field(str, required=True, alias="createdDate")
    origin: str = Field(str, required=True, alias="origin")
    env: str = Field(str, required=True, alias="env")
    cluster_index: Optional[str] = Field(None, alias="cluster_index")
    entity_type: str = Field(str, required=True, alias="entity_type")
    tenant_id: Optional[str] = Field(None, alias="tenant_id")
    user_id: Optional[str] = Field(None, alias="user_id")
    user_email: Optional[str] = Field(None, alias="user_email")
    previous_activity: str = Field(str, required=True, alias="previous_activity") 
    last_activity: str = Field(str, required=True, alias="last_activity") 
    tier: str = Field(str, required=True, alias="tier") 
    catalog_number: str = Field(str, required=True, alias="catalog_number") 
    error_code: Optional[str] = Field(None, alias="error_code")
    error_description: Optional[str] = Field(None, alias="error_description")
    
    def __init__(self, execution_id: str, created_date: str, origin: str, env: str, cluster_index: str, entity_type: str,
                 tenant_id: str, user_id: str, user_email: str, previous_activity: str, last_activity: str, tier: str, 
                 catalog_number: str, error_code: str, error_description: str):
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
    