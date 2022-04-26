from fhir import db

class User(db.Document):
    useremail = db.EmailField()
    password = db.StringField()

