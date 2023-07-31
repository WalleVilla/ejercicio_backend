from sqlalchemy import Column, Integer, String, DateTime, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship
from models.table import db, Table

class Products(db.Model, Table):
    id = db.Column(Integer, autoincrement=True, primary_key=True)
    name = db.Column(String(50), nullable=False)
    description = db.Column(String(255), nullable=False)
    category_id = db.Column(Integer, ForeignKey("categories.id"))
    created_at = db.Column(DateTime, nullable=False)
    created_by = db.Column(SmallInteger, nullable=False)

    categories = relationship("Categories", backref="products")