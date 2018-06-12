import os.path

basedir = os.path.abspath(os.path.dirname(__file__))

class Conf(object):
    DEBUG = True
    SECRET_KEY = 'senha-secreta'
    #QLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'banco.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
