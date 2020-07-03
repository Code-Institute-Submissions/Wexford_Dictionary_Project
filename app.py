import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)


app.config["MONGO_DBNAME"] = 'wexfordDictionary'
app.config["MONGO_URI"] = 'mongodb+srv://johnmurphy:Admin12345@wexforddictionary.a6e7r.mongodb.net/wexfordDictionary?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_slangs')
def hello ():
    return render_template("slangs.html", slangs=mongo.db.slangs.find())

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=(os.environ.get("PORT")),
        debug=True)
