from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://mongodb-service:27017/")
db = client["devopsdb"]
collection = db["messages"]

@app.route("/message", methods=["GET"])
def get_messages():

    data=list(collection.find({},{"_id":0}))

    return jsonify(data)

@app.route("/message", methods=["POST"])
def add_message():

    msg=request.json["msg"]

    collection.insert_one({"msg":msg})

    return jsonify({"status":"saved"})


if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)