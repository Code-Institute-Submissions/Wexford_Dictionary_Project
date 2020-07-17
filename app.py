import os
from flask import Flask, render_template, redirect, request, url_for, flash  # imports tools from flask
from flask_pymongo import PyMongo   # imports pymongo to allow 
                                    # interaction between python 
                                    # and mongodb
from bson.objectid import ObjectId  # pulls objectid to allow 
                                    # data be pulled for editing
from os import path                 # used to create secret key hidden 
                                    # MongoURI and store within env.py 
                                    # which is called out in .gitignore
if path.exists("env.py"):
    import env

app = Flask(__name__)


app.config["MONGO_DBNAME"] = "wexfordDictionary"    # DB name
app.config["MONGO_URI"] = os.getenv('MONGO_URI')    # MongoURI located in env.py 
                                                    # hidden by .gitignore for security

app.secret_key = os.getenv('SECRET_KEY')    # Secret Key located in env.py 
                                            # hidden by .gitignore for security

mongo = PyMongo(app)
 
@app.route('/')     # Default route for the 
                    # website directs to login page
@app.route('/login')   # login app route renders login.html
def login():
    return render_template('login.html')

@app.route('/register')   # register app route render login.html
def register():
    return render_template('register.html')

@app.route('/home')   # home app route render home.html
def home():
    return render_template('home.html')


@app.route('/insertuser', methods=['POST'])     # queries username in Mongo DB
                                                # if user exists prompts user with 
                                                # a flash message, If does not exist
                                                #  creates a new user
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
        flash('Username already exists!')
        return redirect(url_for('register'))


@app.route('/isuser', methods=['POST'])     # queries users in mongo db
                                            # if user exists - logs in
                                            # if user doesn't exist prompts 
                                            # the user to register an account
def isuser():

    formusername = request.form.get('username')
    user = mongo.db.users.find_one({'username': formusername})

    if user != None:
       return redirect(url_for('home'))
    else:
        flash('Username does not exist!')
    return redirect(url_for('login'))


@app.route('/getslang')     # renders the slangs.html template
                            # pulls in the categories from mongoDB
                            # sorts them A-Z and applies filter to 
                            # the categories filter dropdown
def getslang ():
    category = request.args.get('category')
    if category is None:
        filter = {}
    else:
        filter = {'category_name': { '$eq': category }} 
    return render_template("slangs.html", slangs=mongo.db.slangs.find(filter).sort("slang_name"), categories=mongo.db.categories.find(),  selectedCategory=category)

@app.route('/addslang')     # renders the addslangwords.html page
                            # pulls in categories to be selected
                            # from dropdown list
def add_slang():
        return render_template("addslangwords.html", categories=mongo.db.categories.find())

@app.route('/insertslang', methods=['POST'])    # posts new slang form to MongoDB 
                                                # and renders the browse all page
def insertslang():
    slang = mongo.db.slangs
    slang.insert_one(request.form.to_dict())
    return redirect(url_for('getslang'))

@app.route('/editslang/<slangid>')      # pulls the specific slang object
                                        # back to the edit screen using the 
                                        # slangid in Mongo DB, pulls back 
                                        # categories to select from dropdownlist.
def editslang(slangid):
    slang = mongo.db.slangs.find_one({"_id": ObjectId(slangid)})
    categories = mongo.db.categories.find()
    category_list = [category for category in categories]
    return render_template("editslangwords.html", slang=slang, categories= category_list)

@app.route('/updateslang/<slangid>', methods=['POST'])      # posts update to the database 
                                                            # on screen using the object ID
                                                            # and renders the browse all/get 
                                                            # slang screen.
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


@app.route('/deleteslang/<slangid>')    # deletes a specific record 
                                        # of slang in mongoDB using the 
                                        # object/slang id then redirects 
                                        # to browse/get slang page
def deleteslang(slangid):
    mongo.db.slangs.remove({'_id': ObjectId(slangid)})
    return redirect(url_for('getslang'))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=(os.environ.get("PORT")),
        debug=True)

