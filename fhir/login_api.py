from flask import request, jsonify
from fhir import app
from flask_jwt_extended import create_access_token
from passlib.hash import sha256_crypt
from fhir.collection import User
from fhir.login_validation import schema


@app.route('/api/v1/login', methods=['POST'])
def login():
    data = request.json
    validation_result = schema.validate(request.json)
    if validation_result.get('success', False) is False:
        return jsonify({
            "status": "Error",
            "errors": validation_result.get("error")
        })
    user = User.objects(useremail__in=[data.get("useremail")]).first()
    if not user:
        return jsonify({
            "warnings":[],
            "errors":"wrong_useremail"
        })

    if user:
      if sha256_crypt.verify(data.get("password"), user.password):
        access_token = create_access_token(identity=user.useremail)
        return jsonify({"access_token":access_token}),200

    return jsonify({
        "warnings":[],
        "errors":"wrong_password"
    }),400
