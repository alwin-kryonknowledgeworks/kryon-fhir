from fhir import db


class User(db.Document):
    user_email = db.EmailField()
    password = db.StringField()
    otp = db.StringField()
    otp_validtime = db.DateTimeField()
