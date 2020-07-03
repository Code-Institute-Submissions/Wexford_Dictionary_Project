import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)


app.config["MONGO_DBNAME"] = "wexfordDictionary"
app.config["MONGO_URI"] = "mongodb+srv://johnmurphy:Admin12345@wexforddictionary.a6e7r.mongodb.net/wexfordDictionary?retryWrites=true&w=majority"

mongo = PyMongo(app)

@app.route('/')
@app.route('/getslang')
def getslang ():
    return render_template("slangs.html", slangs=mongo.db.slangs.find())

@app.route('/addslang')
def add_slang():
        return render_template("addslangwords.html", categories=mongo.db.categories.find())

@app.route('/insertslang', methods=['POST'])
def insertslang():
    slang = mongo.db.slangs
    slang.insert_one(request.form.to_dict())
    return redirect(url_for('getslang'))

@app.route('/editslang/<slangid>')
def editslang(slangid):
    _slang = mongo.db.slangs.find_one({"_id": ObjectId(slangid)})
    _categories = mongo.db.categories.find()
    category_list = [category for category in _categories]
    return render_template("editslangwords.html", slang=_slang, categories= category_list)

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=(os.environ.get("PORT")),
        debug=True)
