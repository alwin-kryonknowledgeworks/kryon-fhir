from fhir import db

class User(db.Document):
    username = db.StringField()
    password = db.StringField()
