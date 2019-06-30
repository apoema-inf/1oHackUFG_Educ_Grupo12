from flask import Flask, render_template
from models import *


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app


app = create_app()


@app.route('/test')
def test():
	db.create_all()
	return 'dae'

@app.route('/table')
def table():
	pesquisas = Pesquisa.query.limit(10).all()
	return render_template('table.html', projects=pesquisas)

@app.route('/home')
def home():
	return render_template('index.html')

@app.route('/project/<int:project_id>')
def project(project_id):
	project = Pesquisa.query.get(project_id)
	return render_template('project.html', project=project)
