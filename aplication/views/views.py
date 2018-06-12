from flask import Flask, abort, render_template, flash, request, redirect, url_for, session
from aplication import app, login_manager
from aplication.models.form import LoginForm, CadCliente
from aplication.models.tables import User

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)


# Pagina inicial do site
@app.route('/login', methods=["GET","POST"])
def login():
    erro = None
    form = LoginForm()
    email = 'ld.desenvolvimentos@gmail.com'
    password = '14022016'

    if not session.get('logged_in'):
        if request.method=="POST":
            if form.email.data == email and form.password.data == password:
                session['logged_in'] = True
                return redirect(url_for('index'))
            else:
                flash("Usuario ou senha Invalidos")
    return render_template("login.html", form=form)

@app.route('/')
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    return render_template('index.html')

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect(url_for('login'))

##################
# SETOR CLIENTES ################################
##################

@app.route('/cad-cliente', methods=["GET","POST"])
def cad_cliente():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    cliente = CadCliente()

    if request.method=='POST':
        pass
    return render_template('cad_cliente.html')

@app.route('/edit_cliente')
def edit_cliente():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('edit_cliente.html')

@app.route('/list_cliente')
def list_cliente():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('list_cliente.html')

########################
# SETOR CLIENTES - FIM ##########################
########################

@app.route('/new_orca')
def new_orca():
    return render_template('new_orca.html')

@app.route('/edit_orca')
def edit_orca():
    return render_template('edit_orca.html')

@app.route('/list_orca')
def list_orca():
    return render_template('list_orca.html'), 200


@app.route('/conf_empresa')
def conf_empresa():
    return render_template('conf_empresa.html')


# caso a pagina nao seja encontrada sera redirecionada para pagina escolhida
@app.errorhandler(404)
def page_not_found(error):
    return render_template('_404.html'), 404