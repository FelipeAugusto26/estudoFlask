from aplication import db

class User(db.Model):
    __tablename__= 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))

    def __init__(self, email, password):
        self.email = email
        self.password = password


    def __repr__(self):
        return '<User %r'.format(self.username)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    @property
    def get_id(self):
        return



class Cliente(db.Model):
    __tablename__= 'clientes'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(64))
    telefone = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(100), unique=True)
    endereco = db.Column(db.String)

    def __repr__(self):
        return '<cliente %r'.format(self.nome)
