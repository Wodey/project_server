import os
import ssl
from dotenv import load_dotenv
import certifi
load_dotenv()


def get_db():
    from pymongo import MongoClient
    print(os.getenv('URI'))
    client = MongoClient(os.getenv('URI'), ssl_cert_reqs=ssl.CERT_NONE)
    db = client.jwtpassport
    print(db)
    print('hey')
    return db
