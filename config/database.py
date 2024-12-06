import json
from pymongo import MongoClient

configuration = {
    "host": "mongodb",
    "port": 27017,
    "database": "qr_code",
    "useauth": False,
    "user": "admin_bdd",
    "password": "admin123mongod",
    "tableauth": "admin"
}

mongo_config = configuration


def connector():
    if mongo_config['useauth']:
        uri = (f"mongodb://{mongo_config['user']}:{mongo_config['password']}"
                f"@{mongo_config['host']}:{mongo_config['port']}/{mongo_config['tableauth']}")
    else:
        uri = f"mongodb://{mongo_config['host']}:27017/"
    client = MongoClient(uri)
    db = client[mongo_config['database']]
    return db
