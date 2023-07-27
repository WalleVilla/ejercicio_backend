from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.sqltypes import TIMESTAMP #Aunque es similar a DateTime
from sqlalchemy.orm import relationship

app = Flask(__name__)

#Create database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///tienda.db"

db = SQLAlchemy()
db.init_app(app)

# ------------------------------- CREATE TABLES ------------------------------ #

'''
SmallInteger es el equivalente a TINYINT al igual que String con VARCHAR
'''

class categories(db.Model):
    id = db.Column(db.Integer, autoincrement=True ,primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.SmallInteger, nullable=False)
    
class products(db.Model):
    id = db.Column(db.Integer, autoincrement=True ,primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id") ,nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.SmallInteger, nullable=False)
    
    categories = relationship("categories", backref="products")

class providers(db.Model):
    id = db.Column(db.Integer, autoincrement=True ,primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    full_address = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.SmallInteger, nullable=False)

class purchase_orders(db.Model):
    provider_id = db.Column(db.Integer, db.ForeignKey("providers.id"),primary_key=True)
    date = db.Column(TIMESTAMP, nullable=False)
    total = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.SmallInteger, nullable=False)
    
    categories = relationship("providers", backref="purchase_orders")

class purchase_order_detail(db.Model):
    purchase_order_id = db.Column(db.Integer, db.ForeignKey("purchase_orders.provider_id"), nullable=False, primary_key = True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.SmallInteger, nullable=False)
    
    purchase_order = relationship("purchase_orders", backref="purchase_order_details")
    products = relationship("products", backref="purchase_order_detail")
    
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True) 