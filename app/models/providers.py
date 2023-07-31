from sqlalchemy import Column, Integer, String, DateTime, SmallInteger
from models.table import db, Table

class Providers(db.Model, Table):
    id = db.Column(Integer, autoincrement=True, primary_key=True)
    name = db.Column(String(50), nullable=False)
    full_address = db.Column(String(255), nullable=False)
    created_at = db.Column(DateTime, nullable=False)
    created_by = db.Column(SmallInteger, nullable=False)
