from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

with open('config.json','r') as c:
    params = json.load(c)["params"]

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
db = SQLAlchemy(app)

class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(30))
    phone = db.Column(db.String(10))
    message = db.Column(db.String(100))
    date = db.Column(db.DateTime, default=datetime.utcnow)
    

@app.route("/")
def home():
    return render_template('index.html', p = params)

@app.route("/about")
def about():
    return render_template('about.html', p = params)

@app.route("/contact", methods =['GET','POST'])
def contact():
    if(request.method == 'POST'):
        name = request.form.get('name')
        email_add = request.form.get('email')
        ph_no = request.form.get('phone')
        msg = request.form.get('message')
        
        entry = Contact(name = name, email=email_add,phone=ph_no,message=msg)
        db.session.add(entry)
        db.session.commit()
    return render_template('contact.html', p = params)

@app.route("/post")
def post():
    return render_template('post.html', p = params)


app.run(debug = True)