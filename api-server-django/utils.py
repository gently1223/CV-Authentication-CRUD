from pymongo import MongoClient

connection_string = "mongodb://localhost:27017"

client = MongoClient('connection_string')
db = client['db_name']