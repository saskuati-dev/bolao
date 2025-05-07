from flask import Flask,render_template, request, redirect, url_for, flash, session
from pymongo import MongoClient
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash
import os
load_dotenv()


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

mongo_uri = os.environ.get("MONGO_URI")
client = MongoClient(mongo_uri)
db = client.get_default_database()
users_db = db['users']


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form[name]
        email = request.form[email]
        password = generate_password_hash(request.form[password])
        if users_db.find_one({'email':email}):
            flash("E-mail já cadastrado :/", 'danger')
        
        else:
            users_db.insert_one({
                'name': name,
                'email':email,
                'password': password
            })
            flash('Cadastro realizado com sucesso!', 'success')
            return redirect(url_for('login'))
        
    return render_template('register.html')



@app.route("/login", methods=["GET", "POST"])
def login():
    pass




if __name__ == "__main__":
    app.run(debug=True)