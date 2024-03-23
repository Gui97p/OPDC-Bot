import pymongo
from .model import Model

mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')
db = mongo_client['OPDC']

# Model
def getDB(name):
    return Model(db[name])
