from datetime import datetime
from MyBlog import db


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    # ошения один ко многим. backref='author' - говорит что создасться колонка автор в моделе пост
    # Пост указывается таблица с с какой отношения
    # lazy = True - определяет когда скл алхимия загружает данные из базы данных. Это означает что она
    # загрузит данные по необходимости за один раз. тоесть если вызвать свойство пост у автора то он
    # загрузит все посты автора

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"