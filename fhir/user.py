from fhir.collection import User
from passlib.hash import sha256_crypt

def create_user():
    admin_user = User.objects(useremail='').first()

    if not admin_user:
        user = User()
        user.useremail=""
        user.password=sha256_crypt.encrypt("admin")
        user.save()

create_user()
