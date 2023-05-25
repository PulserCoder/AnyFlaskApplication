from flask import Flask
from config import Config
from models import Movies
from setup_db import db


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    db.init_app(app)
    return app


def create_data(app, db):
    with app.app_context():
        db.create_all()

        u1 = Movies(name='movie1')
        u2 = Movies(name='movie2')
        u3 = Movies(name='movie3')

        with db.session.begin():
            db.session.add_all([u1, u2, u3])

def model_list_to_dict_list(model_list):
    dict_list = []
    for item in model_list:
        dict_list.append(item.__dict__)
    return dict_list



app = create_app(Config())
create_data(app, db)

@app.route('/movies')
def movies():
    return str(model_list_to_dict_list(db.session.query(Movies).all()))



if __name__ == '__main__':
    app.run(debug=True)