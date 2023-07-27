from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.sqltypes import TIMESTAMP #Aunque es similar a DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

app = Flask(__name__)

#Create database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///tienda.db"

db = SQLAlchemy()
db.init_app(app)

# ------------------------------- CREATE TABLES ------------------------------ #

'''
SmallInteger es el equivalente a TINYINT al igual que String con VARCHAR
'''

class Categories(db.Model):
    id = db.Column(db.Integer, autoincrement=True ,primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.SmallInteger) #nullable=False
    
class Products(db.Model):
    id = db.Column(db.Integer, autoincrement=True ,primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id") ,nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.SmallInteger, nullable=False)
    
    categories = relationship("Categories", backref="Products")

class Providers(db.Model):
    id = db.Column(db.Integer, autoincrement=True ,primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    full_address = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.SmallInteger, nullable=False)

class Purchase_orders(db.Model):
    provider_id = db.Column(db.Integer, db.ForeignKey("providers.id"),primary_key=True)
    date = db.Column(TIMESTAMP, nullable=False)
    total = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.SmallInteger, nullable=False)
    
    categories = relationship("Providers", backref="Purchase_orders")

class Purchase_order_detail(db.Model):
    purchase_order_id = db.Column(db.Integer, db.ForeignKey("purchase_orders.provider_id"), nullable=False, primary_key = True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    created_by = db.Column(db.SmallInteger, nullable=False)
    
    purchase_order = relationship("Purchase_orders", backref="Purchase_order_details")
    products = relationship("Products", backref="Purchase_order_detail")
    
with app.app_context():
    db.create_all()

# ---------------------------------- CREATE ---------------------------------- #

#CATEGORIES
@app.route("/add-category", methods=["POST"])
def add_category():
    created_at_date = request.form.get("created_at")
    new_created_at_date = datetime.strptime(created_at_date, "%Y-%m-%d")
    
    new_category = Categories(
        name = request.form.get("name"),
        description = request.form.get("description"),
        created_at = new_created_at_date,
        created_by  = request.form.get("created_by")
    )
    db .session.add(new_category)
    db.session.commit()
    return jsonify(response={"success": "Category added successfully"})

#PRODUCTS
@app.route("/add-product", methods=["POST"])
def add_product():
    created_at_date = request.form.get("created_at")
    new_created_at_date = datetime.strptime(created_at_date, "%Y-%m-%d")
    
    new_product = Products(
        name = request.form.get("name"),
        description = request.form.get("description"),
        category_id = request.form.get("category_id"),
        created_at = new_created_at_date,
        created_by  = request.form.get("created_by")
    )
    db .session.add(new_product)
    db.session.commit()
    return jsonify(response={"success": "Product added successfully"})

#PROVIDERS
@app.route("/add-provider", methods=["POST"])
def add_provider():
    created_at_date = request.form.get("created_at")
    new_created_at_date = datetime.strptime(created_at_date, "%Y-%m-%d")
    
    new_provider = Providers(
        name = request.form.get("name"),
        full_address = request.form.get("full_address"),
        created_at = new_created_at_date,
        created_by  = request.form.get("created_by")
    )
    db .session.add(new_provider)
    db.session.commit()
    return jsonify(response={"success": "Provider added successfully"})

#PURCHASE ORDERS
@app.route("/add-purchase-order", methods=["POST"])
def add_purchase_order():
    date = request.form.get("date")
    new_date = datetime.strptime(date, "%Y-%m-%d")
    
    created_at_date = request.form.get("created_at")
    new_created_at_date = datetime.strptime(created_at_date, "%Y-%m-%d")
    
    new_purchase_order = Purchase_orders(
        provider_id = request.form.get("provider_id"),
        date = new_date,
        total = request.form.get("total"),
        created_at = new_created_at_date,
        created_by  = request.form.get("created_by")
    )
    db .session.add(new_purchase_order)
    db.session.commit()
    return jsonify(response={"success": "Purchase order added successfully"})

#PURCHASE ORDERS DETAIL
@app.route("/add-purchase-order-detail", methods=["POST"])
def add_purchase_order_detail():
    
    created_at_date = request.form.get("created_at")
    new_created_at_date = datetime.strptime(created_at_date, "%Y-%m-%d")
    
    new_purchase_order_detail = Purchase_order_detail(
        purchase_order_id = request.form.get("purchase_order_id"),
        product_id = request.form.get("product_id"),
        quantity = request.form.get("quantity"),
        total = request.form.get("total"),
        created_at = new_created_at_date,
        created_by  = request.form.get("created_by")
    )
    db .session.add(new_purchase_order_detail)
    db.session.commit()
    return jsonify(response={"success": "Purchase order detail added successfully"})

# --------------------------------- HOME PAGE -------------------------------- #
 
@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True) 