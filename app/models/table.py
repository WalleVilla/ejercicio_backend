from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Table():
    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary
