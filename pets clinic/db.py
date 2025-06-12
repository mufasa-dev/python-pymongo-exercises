import pymongo

cli = pymongo.MongoClient("mongodb://localhost:27017/")
db = cli["clinic_db"]