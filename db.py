import os
from dotenv import load_dotenv

load_dotenv()


def get_db():
    from pymongo import MongoClient

    client = MongoClient(os.getenv('URI'))
    db = client['jwtpassport']

    return db
