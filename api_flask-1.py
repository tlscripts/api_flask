from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sample.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Model your databases. Be sure to match all fields
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    First_name = db.Column(db.String(100))
    Last_name = db.Column(db.String(100))
    Gender= db.Column(db.String(100))
    Text1 = db.Column(db.String(500))

# Base class to instantiate object with all fields, or to subclass
class UserInfo:
    
    def get():
        a = User.query
        all_users = []
        for item in a:
            row = {}
            row['id'] = item.id
            row['first'] = item.First_name
            row['last'] = item.Last_name
            row['gender'] = item.Gender
            row['text1'] = item.Text1
            all_users.append(row)
        return all_users

# Our object to run queries against
allusers = UserInfo.get()

@app.route('/<first>/<last>', methods=['GET'])
def gets(first, last):
    a = []
    for p in allusers:
        if first in p['first'] and last in p['last']:
            a.append(p)
    return jsonify({'users':a})

portno=5000
if __name__ == '__main__':
    app.run(port=portno, debug=True)


