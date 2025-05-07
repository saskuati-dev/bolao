from flask import Flask,render_template, request, redirect, url_for, flash
from pymongo import MongoClient

app = Flask(__name__)


app.config["MONGO_URI"] = "mongodb://localhost:27017/bolaoDatabase"



if __name__ == "__main__":
    app.run(debug=True)