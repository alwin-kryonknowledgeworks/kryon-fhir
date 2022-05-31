from fhir.database_collection.collection import User
from passlib.hash import sha256_crypt


def create_user():
    admin_user = User.objects(user_email='gowthamsenthamilselvan0796@gmail.com').first()

    if not admin_user:
        user = User()
        user.user_email = "gowthamsenthamilselvan0796@gmail.com"
        user.password = sha256_crypt.encrypt("admin")
        user.save()


create_user()
