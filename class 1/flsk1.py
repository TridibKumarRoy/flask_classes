from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask_class_2023'
db = SQLAlchemy(app)

class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(30))
    phone = db.Column(db.String(10))
    message = db.Column(db.String(100))
    date = db.Column(db.String(120))
    

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

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
    return render_template('contact.html')

@app.route("/post")
def post():
    return render_template('post.html')


app.run(debug = True)