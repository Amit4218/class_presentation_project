from pymongo import MongoClient
import uuid
from bson import ObjectId


def connect_db():
    try:
        client = MongoClient("mongodb://localhost:27017/")
        db = client["class_project"]
        return db
    except Exception as e:
        print(f"Error connecting to db: {e}")
        return None


def get_random_riddle():
    try:
        db = connect_db()
        collection = db["riddles"]
        if collection is None:
            return {"error": "DB connection failed"}

        results = collection.aggregate([{"$sample": {"size": 1}}])
        for riddle in results:
            riddle["_id"] = str(riddle["_id"])
            return riddle
    except Exception as e:
        return {"error": f"Error fetching random riddle: {e}"}


def create_session_token(id=None):
    try:
        token = str(uuid.uuid4())
        db = connect_db()
        collection = db["sessions"]
        if collection is None:
            return {"error": "DB connection failed"}

        collection.insert_one(
            {
                "token": token,
                "question_id": id,
                "correct_answer": 0,
                "total_attempts": 0,
            }
        )
        return token
    except Exception as e:
        return {"error": f"Error creating session token: {e}"}


def verify_answer(token, answer):
    try:
        db = connect_db()
        collection = db["sessions"]
        if collection is None:
            return {"error": "DB connection failed"}

        session = collection.find_one({"token": token})
        if not session:
            return {"error": "Invalid token"}

        question_id = session["question_id"]
        riddles_collection = db["riddles"]

        riddle = riddles_collection.find_one({"_id": ObjectId(question_id)})

        if not riddle:
            return {"error": "Riddle not found"}

        if riddle["answer"].strip().lower() == answer.strip().lower():
            new_riddle = get_random_riddle()

            collection.update_one(
                {"token": token},
                {
                    "$set": {"question_id": new_riddle["_id"]},
                    "$inc": {"correct_answer": 1, "total_attempts": 1},
                },
            )
            return new_riddle
        else:
            collection.update_one(
                {"token": token},
                {"$inc": {"total_attempts": 1}},
            )
            return new_riddle
    except Exception as e:
        return {"error": f"Error verifying answer: {e}"}


def submit_riddle(token):
    try:
        db = connect_db()
        collection = db["sessions"]
        if collection is None:
            return {"error": "DB connection failed"}

        session = collection.find_one({"token": token})
        if not session:
            return {"error": "Invalid token"}

        total_attempts = session.get("total_attempts", 0)
        correct_answers = session.get("correct_answer", 0)

        # Clean up the session after submission
        collection.delete_one({"token": token})

        return {
            "total_attempts": total_attempts,
            "correct_answers": correct_answers,
            "token": token,
        }

    except Exception as e:
        return {"error": f"Error submitting riddle: {e}"}
