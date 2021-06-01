from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_RECORD_QUERIES'] = True
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'something_very_secret'
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)


from MyBlog import routes