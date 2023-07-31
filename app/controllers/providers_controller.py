from flask import request, jsonify, redirect, url_for
from datetime import datetime
from models.providers import Providers
from models.table import db

# ---------------------------------- CREATE ---------------------------------- #

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

# --------------------------------- READ ALL --------------------------------- #

def get_providers():
    result = db.session.execute(db.select(Providers).order_by(Providers.id))
    all_results = result.scalars().all()
    return jsonify(providers=[provider.to_dict() for provider in all_results])

# -------------------------------- READ BY ID -------------------------------- #

def search_provider():
    id = request.args.get("id")
    result = db.session.execute(db.select(Providers).where(Providers.id == id))
    all_results = result.scalars().all()
    if all_results:
        return jsonify(provider=[provider.to_dict() for provider in all_results])
    else:
        return jsonify(error={"Not Found": "The id doesn't exist"}), 404

# -------------------------- UPDATE BY ID | PATCH | -------------------------- #

def change_provider(id, column):
    new_value= request.args.get("new_value")
    provider = db.get_or_404(Providers, id)
    
    if provider:
        setattr(provider, column, new_value)
        db.session.commit()
        return redirect(url_for("route_get_providers"))
    else:
        return jsonify(error={"Not Found": "The id doesn't exist"}), 404

# ------------------------------- DELETE BY ID ------------------------------- #