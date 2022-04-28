from fhir import db

class User(db.Document):
    useremail = db.EmailField()
    password = db.StringField()
    otp=db.StringField()
    otp_valid_time=db.DateTimeField()

