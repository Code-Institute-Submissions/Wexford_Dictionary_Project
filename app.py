import os
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)


app.config["MONGO_DBNAME"] = "wexfordDictionary"
app.config["MONGO_URI"] = "mongodb+srv://johnmurphy:Admin12345@wexforddictionary.a6e7r.mongodb.net/wexfordDictionary?retryWrites=true&w=majority"

mongo = PyMongo(app)

@app.route('/')
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/insertuser', methods=['POST'])
def insertuser():
   
    user = mongo.db.users
    if user.find_one({'username': request.form.get('username')}) == None:
        newuser = {
            'username': request.form.get('username'),
            'firstname': request.form.get('firstname'),
            'lastname': request.form.get('lastname'),
            'country': request.form.get('country')
        }
        user.insert_one(newuser)
        return redirect(url_for('login'))
    else:
        return redirect(url_for('register'))


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
    slang = mongo.db.slangs.find_one({"_id": ObjectId(slangid)})
    categories = mongo.db.categories.find()
    category_list = [category for category in categories]
    return render_template("editslangwords.html", slang=slang, categories= category_list)

@app.route('/updateslang/<slangid>', methods=['POST'])
def updateslang(slangid):
    slang = mongo.db.slangs
    slang.update( {'_id': ObjectId(slangid)},
    {
        'category_name':request.form.get('category_name'),
        'slang_name':request.form.get('slang_name'),
        'slang_description':request.form.get('slang_description'),
        'slang_example':request.form.get('slang_example'),
    })
    return redirect(url_for('getslang'))


@app.route('/deleteslang/<slangid>')
def deleteslang(slangid):
    mongo.db.slangs.remove({'_id': ObjectId(slangid)})
    return redirect(url_for('getslang'))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=(os.environ.get("PORT")),
        debug=True)


    
   