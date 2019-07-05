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


# Our object to run queries against
allusers = User.query

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


