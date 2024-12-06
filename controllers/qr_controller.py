from config.database import connector


def save_qr(data):
    db = connector()
    collection = db["qr-code"]
    collection.insert_one(data)
