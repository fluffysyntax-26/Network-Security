import os
import sys
import json
import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from dotenv import load_dotenv
import certifi # provides consistent, maintain certificate bundle
# used to verify website legitimacy using CA certificates over https:// connections

# load environment variables
load_dotenv()

# url for cluster
MONGO_DB_URL = os.getenv("MONGO_DB_URI")

class NetworkDataExtract(): 
    def __init__(self, database, collection):
        try: 
            self.database = database
            self.collection = collection
            self.mongo_client = pymongo.MongoClient(
                MONGO_DB_URL, 
                tls=True, 
                tlsCAFile=certifi.where()
            )
        except Exception as e: 
            raise NetworkSecurityException(e, sys)
    
    def csv_to_json(self, file_path): 
        try: 
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)

            # convert df into list of dicts
            records = data.to_dict(orient="records")
            return records
        
        except Exception as e: 
            raise NetworkSecurityException(e, sys)
        
    def insert_data_mongodb(self, records): 
        try: 
            db = self.mongo_client[self.database]
            collection = db[self.collection]
            collection.insert_many(records)
            print("Records Successfully Inserted!")
            return len(records)
        except Exception as e:
            raise NetworkSecurityException(e, sys)

if __name__ == "__main__": 
    DATASET_FILE_PATH = "/Users/deepak/Desktop/NetworkSecurity/Network_Data/phisingData.csv"
    DATABASE = "NetSec"
    Collection = "NetworkData"

    network_obj = NetworkDataExtract(DATABASE, Collection)
    records = network_obj.csv_to_json(file_path=DATASET_FILE_PATH)
    num_records = network_obj.insert_data_mongodb(records)

    print(num_records)