from pymongo import MongoClient
from bson.objectid import ObjectId
from fastapi import FastAPI
import os
import re

app = FastAPI()

mongoString = os.environ.get('MONGO_STRING')

db = 'sample_mflix'
collection = 'movies'

client = MongoClient(mongoString, maxPoolSize=50)
database = client[db]

@app.get("/movies")
def get_filme():
    '''Return all movies from base'''
    filmes = database[collection].find()
    filmes = [{**doc, "_id": str(doc["_id"])} for doc in filmes]
    return filmes

@app.get("/movie/{filme}")
def get_file_name(filme: str):
    '''Search and Return movie by tittle'''
    filme = filme.replace("%20"," ")
    name_pattern = re.compile(f".*{re.escape(filme)}.*", re.IGNORECASE)
    filmes = database[collection].find({"title": name_pattern})
    filmes = [{**doc, "_id": str(doc["_id"])} for doc in filmes]
    return filmes

@app.get("/movie/id/{id}")
def get_file_id(id: str):
    '''Return movie by ID'''
    objInstance = ObjectId(id)
    filmes = database[collection].find_one({"_id" : objInstance})
    filmes["_id"] = str(filmes["_id"])
    return filmes