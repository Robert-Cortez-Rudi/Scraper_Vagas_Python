from pymongo import MongoClient
import os


def get_database(uri=None, db_name=None):

    # Configuração padrão do URI se não for fornecido
    uri = uri or os.getenv("MONGO_URI", "mongodb://localhost:27017/")

    client = MongoClient()

    if db_name:
        db = client[db_name]
    else:
        db = client["db_vagas"]    
    
    return db
