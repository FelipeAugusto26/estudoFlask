from flask import Flask, abort, render_template
from aplication import app
from aplication.models import userform


# Pagina inicial do site
@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/')
def index():
    return render_template('index.html')

##################
# SETOR CLIENTES ################################
##################

@app.route('/cad-client')
def cad_cliente():
    return render_template('cad_cliente.html')

@app.route('/edit_cliente')
def edit_cliente():
    return render_template('edit_cliente.html')

@app.route('/list_cliente')
def list_cliente():
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