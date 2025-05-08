from flask import Flask,render_template, request, redirect, url_for, flash, session, abort
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import os
load_dotenv()


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

mongo_uri = os.environ.get("MONGO_URI")
client = MongoClient(mongo_uri)
db = client.get_default_database()
users_db = db['users']
boloes_db = db['boloes']

@app.route('/')
def home():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    meus_boloes = boloes_db.find({'criador_id': session.get('user_id')})
    return render_template('index.html')


@app.route('/gerenciar/<bolao_id>')
def gerenciar(bolao_id):
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('home'))
    
    bolao = boloes_db.find_one({
        '_id': bolao_id
    })

    if not bolao or bolao['criador_id']!= user_id:
        abort(403)
    
    return render_template('gerenciar_bolao.html', bolao=bolao)

@app.route('criar_bolao', methods=["GET", "POST"])
def criar_bolao():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('home'))

    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form.get('descricao','')
        user_name = session.get('user_name', '')  

        novo_bolao = {  
            'nome': nome,  
            'descricao': descricao,  
            'criador_id': user_id,  
            'criador_nome': user_name,  
            'participantes': [],  
            'rodadas': [],  
            'criado_em': datetime.utcnow().isoformat()  
        }
        resultado = boloes_db.insert_one(novo_bolao)  
        flash('Bolão criado com sucesso!', 'success')  
        return redirect(url_for('detalhes_bolao', bolao_id=str(resultado.inserted_id)))  
    return render_template('criar_bolao.html')

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])
        if users_db.find_one({'email':email}):
            flash("E-mail já cadastrado :/", 'danger')
        
        else:
            users_db.insert_one({
                'name': name,
                'email':email,
                'password': password
            })
            flash('Cadastro realizado com sucesso!', 'success')
            return redirect(url_for('home'))
        
    return render_template('register.html')



@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['password']

        user = users_db.find_one({
            'email': email
            })
            
        if user and check_password_hash(user['password'], senha):
            flash('Login successful.', 'success')
            session['user_id'] = str(user['_id'])
            session['user_name'] = str(user['name'])
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password. Please try again.', 'danger')

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('user_name', None)
    flash('Você saiu da sua conta.')  
    return redirect(url_for('login'))



if __name__ == "__main__":
    app.run(debug=True)