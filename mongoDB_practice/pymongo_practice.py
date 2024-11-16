from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017")

db = client["pf36"]
collection = db["apps"]

cd = collection.find({"tier":2})

for i in cd:
    print(i)
