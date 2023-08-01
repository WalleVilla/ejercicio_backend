from flask import request, jsonify, redirect, url_for
from datetime import datetime
from models.categories import Categories
from models.table import db

# ---------------------------------- CREATE ---------------------------------- #

def add_category():
    created_at_date = request.form.get("created_at")
    new_created_at_date = datetime.strptime(created_at_date, "%Y-%m-%d")

    new_category = Categories(
        name=request.form.get("name"),
        description=request.form.get("description"),
        created_at=new_created_at_date,
        created_by=request.form.get("created_by")
    )
    db.session.add(new_category)
    db.session.commit()
    return jsonify(response={"success": "Category added successfully"})

# --------------------------------- READ ALL --------------------------------- #

def get_categories():
    result = db.session.execute(db.select(Categories).order_by(Categories.id))
    all_results = result.scalars().all()
    return jsonify(categories=[category.to_dict() for category in all_results])

# -------------------------------- READ BY ID -------------------------------- #

def search_category():
    id = request.args.get("id")
    result = db.session.execute(db.select(Categories).where(Categories.id == id))
    all_results = result.scalars().all()
    if all_results:
        return jsonify(category=[cat.to_dict() for cat in all_results])
    else:
        return jsonify(error={"Not Found": "The id doesn't exist"}), 404

# -------------------------- UPDATE BY ID | PATCH | -------------------------- #

def change_category(id, column):
    new_value= request.args.get("new_value")
    category = db.get_or_404(Categories, id)
    
    if category:
        setattr(category, column, new_value)
        db.session.commit()
        return redirect(url_for("route_get_categories"))
    else:
        return jsonify(error={"Not Found": "The id doesn't exist"}), 404

# ------------------------------- DELETE BY ID ------------------------------- #

def delete_category(id):
    category = db.get_or_404(Categories, id)
    
    if category:
        db.session.delete(category)
        db.session.commit()
        return redirect(url_for("route_get_categories"))
    else:
        return jsonify(error={"Not Found": "The id doesn't exist"}), 404
    