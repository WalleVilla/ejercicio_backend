from flask import request, jsonify, redirect, url_for
from datetime import datetime
from models.purchase_order_detail import Purchase_order_detail
from models.table import db

# ---------------------------------- CREATE ---------------------------------- #

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

# --------------------------------- READ ALL --------------------------------- #

def get_purchase_order_detail():
    result = db.session.execute(db.select(Purchase_order_detail).order_by(Purchase_order_detail.purchase_order_id))
    all_results = result.scalars().all()
    return jsonify(purchase_order_detail=[purchase.to_dict() for purchase in all_results])

# -------------------------------- READ BY ID -------------------------------- #

def search_purchase_order_detail():
    id = request.args.get("id")
    result = db.session.execute(db.select(Purchase_order_detail).where(Purchase_order_detail.purchase_order_id == id))
    all_results = result.scalars().all()
    if all_results:
        return jsonify(order=[order.to_dict() for order in all_results])
    else:
        return jsonify(error={"Not Found": "The id doesn't exist"}), 404

# -------------------------- UPDATE BY ID | PATCH | -------------------------- #

def change_purchase_order_detail(id, column):
    new_value= request.args.get("new_value")
    purchase = db.get_or_404(Purchase_order_detail, id)
    
    if purchase:
        setattr(purchase, column, new_value)
        db.session.commit()
        return redirect(url_for("route_get_purchase_order_detail"))
    else:
        return jsonify(error={"Not Found": "The id doesn't exist"}), 404

# ------------------------------- DELETE BY ID ------------------------------- #

def delete_purchase_order_detail(id):
    purchase = db.get_or_404(Purchase_order_detail, id)
    
    if purchase:
        db.session.delete(purchase)
        db.session.commit()
        return redirect(url_for("route_get_purchase_order_detail"))
    else:
        return jsonify(error={"Not Found": "The id doesn't exist"}), 404