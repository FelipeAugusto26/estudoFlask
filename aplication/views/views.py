from flask import Flask, abort, render_template
from aplication import app


# Pagina inicial do site
@app.route('/')
def home():
    return render_template("login.html")

#@app.route('/index')
#def index():
#    return render_template('index.html')



# caso a pagina nao seja encontrada sera redirecionada para pagina escolhida
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404