from pymongo import MongoClient

def connect_db():
    try:
        client = MongoClient("mongodb://localhost:27017/")
        db = client["class_project"]
        collection = db["riddles"]
        return collection
    except Exception as e:
        print(f"Error connecting to db: {e}")
        return None


def get_random_riddle():
    try:
        collection = connect_db()
        if collection is None:
            return {"error": "DB connection failed"}

        results = collection.aggregate([{"$sample": {"size": 1}}])
        for riddle in results:
            riddle["_id"] = str(riddle["_id"]) 
            return riddle
    except Exception as e:
        return {"error": f"Error fetching random riddle: {e}"}
