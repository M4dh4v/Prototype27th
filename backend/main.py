from fastapi import FastAPI
from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient

app = FastAPI()
uri = "mongodb+srv://discordboosterm_db_user:WaawNoiceCluster@cluster0.czjyvje.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

@app.get('/')
def root():
    return {'Hello':'Erripooka'}


@app.post('/items')
def giveItems():
    pass