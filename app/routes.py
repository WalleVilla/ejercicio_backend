from flask import Flask, render_template, request, jsonify, redirect, url_for
from models.table import db
from models.categories import Categories
from models.products import Products
from models.providers import Providers
from models.purchase_orders import Purchase_orders
from models.purchase_order_detail import Purchase_order_detail
from datetime import datetime

# -------------------------- FUNCIONES DE LAS RUTAS -------------------------- #

from controllers.categories_controller import add_category, get_categories, search_category, change_category
from controllers.products_controller import add_product, get_products, search_product, change_product
from controllers.providers_controller import add_provider, get_providers, search_provider, change_provider
from controllers.purchase_orders_controller import add_purchase_order, get_purchase_orders, search_purchase_order, change_purchase_order
from controllers.purchase_order_detail_controller import add_purchase_order_detail, get_purchase_order_detail, search_purchase_order_detail, change_purchase_order_detail, delete_purchase_order_detail

# ---------------------------- INSTANCIA DE LA APP --------------------------- #

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///tienda.db"
db.init_app(app)

# Crear todas las tablas en la base de datos
with app.app_context():
    db.create_all()
    
# ------------------------------- CREATE ROUTES ------------------------------ #

#CATEGORIES
@app.route("/add-category", methods=["POST"])
def route_add_category():
    return add_category()

#PRODUCTS
@app.route("/add-product", methods=["POST"])
def route_add_product():
    return add_product()

#PROVIDERS
@app.route("/add-provider", methods=["POST"])
def route_add_provider():
    return add_provider()

#PURCHASE ORDERS
@app.route("/add-purchase-order", methods=["POST"])
def route_add_purchase_order():
    return add_purchase_order()

#PURCHASE ORDERS DETAIL
@app.route("/add-purchase-order-detail", methods=["POST"])
def route_add_purchase_order_detail():
    return add_purchase_order_detail()

# ------------------------------ READ ALL ROUTES ----------------------------- #

#CATEGORIES
@app.route("/get-categories")
def route_get_categories():
   return get_categories()

#PRODUCTS
@app.route("/get-products")
def route_get_products():
    return get_products()

#PROVIDERS
@app.route("/get-providers")
def route_get_providers():
    return get_providers()

#PURCHASE ORDERS
@app.route("/get-purchase-orders")
def route_get_purchase_orders():
    return get_purchase_orders()

#PURCHASE ORDER DETAIL
@app.route("/get-purchase-order-detail")
def route_get_purchase_order_detail():
    return get_purchase_order_detail()

# ----------------------------- READ BY ID ROUTES ---------------------------- #

#CATEGORIES
@app.route("/search-category")
def route_search_category():
    return search_category()

#PRODUCTS
@app.route("/search-product")
def route_search_product():
    return search_product()

#PROVIDERS
@app.route("/search-provider")
def route_search_provider():
    return search_provider()

#PURCHASE ORDERS
@app.route("/search-purchase-order")
def route_search_purchase_order():
    return search_purchase_order()
    
#PURCHASE ORDER DETAIL
@app.route("/search-purchase-order-detail")
def route_search_purchase_order_detail():
    return search_purchase_order_detail()

# ------------------------------- UPDATE ROUTES ------------------------------ #

#CATEGORIES 
@app.route("/change-category/<int:id>/<column>", methods=["PATCH"])
def route_change_category(id, column):
    return change_category(id, column)

#PRODUCTS
@app.route("/change-product/<int:id>/<column>", methods=["PATCH"])
def route_change_product(id, column):
    return change_product(id, column)

#PROVIDERS
@app.route("/change-provider/<int:id>/<column>", methods=["PATCH"])
def route_change_provider(id, column):
    return change_provider(id, column)

#PURCHASE ORDERS
@app.route("/change-purchase-order/<int:id>/<column>", methods=["PATCH"])
def route_change_purchase_order(id, column):
    return change_purchase_order(id, column)

#PURCHASE ORDER DETAIL
@app.route("/change-purchase-order-detail/<int:id>/<column>", methods=["PATCH"])
def route_change_purchase_order_detail(id, column):
    return change_purchase_order_detail(id, column)

# ------------------------------- DELETE ROUTES ------------------------------ #

#PURCHASE ORDER DETAIL
@app.route("/delete-purchase-order-detail/<int:id>", methods=["DELETE"])
def route_delete_purchase_order_detail(id):
    return delete_purchase_order_detail(id)

# --------------------------------- HOME PAGE -------------------------------- #

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True) 