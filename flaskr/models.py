# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Pesquisa(db.Model):
    __tablename__ = "pesquisas"
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String, nullable=False)
    unidade = db.Column(db.String, nullable=False)
    titulo = db.Column(db.String, nullable=False)
    area_de_conhecimento = db.Column(db.String, nullable=False)
    vinculacao = db.Column(db.String, nullable=False)
    financiada = db.Column(db.String, nullable=False)
    participacao = db.Column(db.String, nullable=False)
    periodo_de_vigencia = db.Column(db.String, nullable=False)
