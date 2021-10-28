import os
import ssl
from dotenv import load_dotenv
import certifi
load_dotenv()


def get_db():
    from pymongo import MongoClient
    client = MongoClient(os.getenv('URI'), ssl_cert_reqs=ssl.CERT_NONE)
    db = client['python_university']
    return db
