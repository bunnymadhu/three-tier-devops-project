from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://mongodb-service:27017/")
db = client["devopsdb"]
collection = db["messages"]

@app.route("/message")
def message():
    data = collection.find_one()

    if not data:
        collection.insert_one({"msg":"Hello from Backend + MongoDB"})
        data = collection.find_one()

    return jsonify({"message": data["msg"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
