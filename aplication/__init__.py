from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
#app.config.from_object('Conf') # Carregar Configuraçoes

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from aplication.models import tables
from aplication.views import views