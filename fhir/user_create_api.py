from datetime import datetime, timedelta
from random import randint
from flask import request, jsonify, render_template
from flask_mail import Message, Mail
from passlib.hash import sha256_crypt
from fhir import app
from fhir.collection import User

mail = Mail(app)
otp = randint(000000, 999999)


@app.route('/api/v1/user', methods=['POST'])
def registration():
    data = request.json
    user_email = data['user_email']
    password = data['password']
    if user_email and password:
        hashing_password = sha256_crypt.encrypt(password)
        user = User.objects(user_email=user_email).first()
        otp_validtime = datetime.now() + timedelta(minutes=8)
        if not user:
            usersave = User(user_email=user_email, password=hashing_password, otp=str(otp), otp_validtime=otp_validtime)
            usersave.save()
            msg = Message(subject='OTP', sender='', recipients=[user_email])
            msg.body = str(otp)
            msg.html = render_template("otp.html", otp=otp)
            mail.send(msg)
            return jsonify({"message": "sent otp"}), 200
        return jsonify({"Error": "Email is already registered"}), 401


@app.route('/api/v1/validate', methods=['POST'])
def validate():
    data = request.json
    user_email = data["user_email"]
    userotp = data['otp']
    expiry_time = datetime.now()
    if user_email and userotp:
        user = User.objects(otp=userotp).first()
        if user.otp == userotp:
            if user.otp_validtime >= expiry_time:
                return jsonify({"message": "Otp varification succesfull"}), 201
        return jsonify({"Error": "Please Try Again"}), 401


@app.route('/api/v1/forgot_password', methods=['POST'])
def forgot_password():
    data = request.json
    user_email = data["user_email"]
    user = User.objects(user_email=user_email).first()
    otp_validtime = datetime.now() + timedelta(minutes=8)
    if User:
        user.update(otp=str(otp), otp_validtime=otp_validtime)
        msg = Message(subject='OTP', sender='', recipients=[user_email])
        msg.body = str(otp)
        msg.html = render_template("otp.html", otp=otp)
        mail.send(msg)
        return jsonify({"message": "sent otp"}), 201
    return jsonify({"Error": "Please Try Again"}), 401


@app.route('/api/v1/password_validate', methods=['POST'])
def validate_password():
    data = request.json
    new_password = data["password"]
    user_otp = data['otp']
    hashing_password = sha256_crypt.encrypt(new_password)
    expiry_time = datetime.now()
    if hashing_password and user_otp:
        user = User.objects(otp=user_otp).first()
        if user.otp == user_otp:
            if user.otp_validtime >= expiry_time:
                user.update(password=hashing_password)
                return jsonify({"message": "New Password varification succesfull"}), 201
        return jsonify({"Error": "Please Try Again"}), 201
