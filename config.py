import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


basedir = os.path.abspath(os.path.dirname(__file__))
connex_app=connexion.App(__name__, specification_dir=basedir)
main_app = connex_app.app

# Database
main_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'apiServiceDB.sqlite')
main_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(main_app)
# Init ma
ma = Marshmallow(main_app)
