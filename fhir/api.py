from flask import request, jsonify
from fhir import app
import json
from flask_jwt_extended import create_access_token
from passlib.hash import sha256_crypt
from fhir.collection import User


@app.route('/api/v1/login', methods=['POST'])
def login():
    data = request.json
    user = User.objects(username__in=[data.get("username")]).first()

    if user:
      if sha256_crypt.verify(data.get("password"), user.password):
        access_token = create_access_token(identity=user.username)
        return jsonify({"access_token":access_token}),200

    return jsonify({"msg":"user_not_found"}),400