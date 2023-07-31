from sqlalchemy import Column, Integer, Float, DateTime, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship
from models.table import db, Table

class Purchase_order_detail(db.Model, Table):
    purchase_order_id = db.Column(db.Integer, db.ForeignKey("purchase_orders.provider_id"), primary_key = True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
    quantity = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.SmallInteger, nullable=False)
    
    purchase_order = relationship("Purchase_orders", backref="Purchase_order_details")
    products = relationship("Products", backref="Purchase_order_detail")
