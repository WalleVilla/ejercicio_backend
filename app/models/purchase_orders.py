from sqlalchemy import Column, Integer, Float, DateTime, SmallInteger, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP #Aunque es similar a DateTime
from sqlalchemy.orm import relationship
from models.table import db, Table

class Purchase_orders(db.Model, Table):
    provider_id = db.Column(db.Integer, db.ForeignKey("providers.id"),primary_key=True)
    date = db.Column(TIMESTAMP, nullable=False)
    total = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.SmallInteger, nullable=False)
    
categories = relationship("Providers", backref="Purchase_orders")