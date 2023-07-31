from flask import request, jsonify, redirect, url_for
from datetime import datetime
from models.products import Products
from models.table import db

# ---------------------------------- CREATE ---------------------------------- #

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

# --------------------------------- READ ALL --------------------------------- #

def get_products():
    result = db.session.execute(db.select(Products).order_by(Products.id))
    all_results = result.scalars().all()
    return jsonify(products=[product.to_dict() for product in all_results])

# -------------------------------- READ BY ID -------------------------------- #

def search_product():
    id = request.args.get("id")
    result = db.session.execute(db.select(Products).where(Products.id == id))
    all_results = result.scalars().all()
    if all_results:
        return jsonify(product=[product.to_dict() for product in all_results])
    else:
        return jsonify(error={"Not Found": "The id doesn't exist"}), 404

# -------------------------- UPDATE BY ID | PATCH | -------------------------- #

def change_product(id, column):
    new_value= request.args.get("new_value")
    product = db.get_or_404(Products, id)
    
    if product:
        setattr(product, column, new_value)
        db.session.commit()
        return redirect(url_for("route_get_products"))
    else:
        return jsonify(error={"Not Found": "The id doesn't exist"}), 404

# ------------------------------- DELETE BY ID ------------------------------- #