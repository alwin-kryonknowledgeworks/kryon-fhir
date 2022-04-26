from flask import request, jsonify
from passlib.hash import sha256_crypt
from fhir import app
from fhir.collection import User

@app.route('/api/v1/user',methods=['POST'])
def registration():
    data = request.json
    print(data)
    useremail=data['useremail']
    password=data['password']
    if useremail and password:
        hashing_password=sha256_crypt.encrypt(password)
        user=User.objects(useremail=useremail)
        if not user:
            usersave=User(useremail=useremail,password=hashing_password)
            print(usersave)
            usersave.save()

        return jsonify({"create user":"user_created"}),200
