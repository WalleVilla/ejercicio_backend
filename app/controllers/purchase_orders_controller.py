from flask import request, jsonify, redirect, url_for
from datetime import datetime
from models.purchase_orders import Purchase_orders
from models.table import db

# ---------------------------------- CREATE ---------------------------------- #

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

# --------------------------------- READ ALL --------------------------------- #

def get_purchase_orders():
    result = db.session.execute(db.select(Purchase_orders).order_by(Purchase_orders.provider_id))
    all_results = result.scalars().all()
    return jsonify(purchase_orders=[purchase.to_dict() for purchase in all_results])

# -------------------------------- READ BY ID -------------------------------- #

def search_purchase_order():
    id = request.args.get("id")
    result = db.session.execute(db.select(Purchase_orders).where(Purchase_orders.provider_id == id))
    all_results = result.scalars().all()
    if all_results:
        return jsonify(order=[order.to_dict() for order in all_results])
    else:
        return jsonify(error={"Not Found": "The id doesn't exist"}), 404

# -------------------------- UPDATE BY ID | PATCH | -------------------------- #

def change_purchase_order(id, column):
    new_value= request.args.get("new_value")
    purchase = db.get_or_404(Purchase_orders, id)
    
    if purchase:
        setattr(purchase, column, new_value)
        db.session.commit()
        return redirect(url_for("route_get_purchase_orders"))
    else:
        return jsonify(error={"Not Found": "The id doesn't exist"}), 404

# ------------------------------- DELETE BY ID ------------------------------- #