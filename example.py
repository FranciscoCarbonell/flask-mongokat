from flask_mongokat import MongokatDocument,MongokatCollection,MongokatApp
from flask import Flask,jsonify
class User(MongokatDocument):
    def get_name(self):
        return self["name"]

class UserCollection(MongokatCollection):
    document_class = User
    col = 'users'
    structure = {
        'name':str,
        'password':str,
    }
    def find_by_name(self, a_value):
        return self.find_one({"name": a_value})


app = Flask(__name__)
app.config.from_object('config.Developement')
mongo = MongokatApp(app)
@app.route('/')
def index():
    user_collection = UserCollection()
    user = user_collection.find_by_name('francisco')
    name = user.get_name()
    return jsonify(name=name)

@app.route('/insert/')
def insert():
    user_collection = UserCollection()
    user_collection.insert({'name':'francisco','password':'123'})
    return jsonify(bson_id=str(result))

app.run(host='127.0.0.1',port=8000)
