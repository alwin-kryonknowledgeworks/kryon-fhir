from datetime import datetime, timedelta
from random import randint
from flask import request, jsonify, render_template
from flask_mail import Message, Mail
from passlib.hash import sha256_crypt
from fhir import app
from fhir.collection import User

mail = Mail(app)
otp=randint(000000,999999)

@app.route('/api/v1/user',methods=['POST'])
def registration():
    data = request.json
    useremail=data['useremail']
    password=data['password']
    if useremail and password:
        hashing_password=sha256_crypt.encrypt(password)
        user=User.objects(useremail=useremail).first()
        otp_vaild_time = datetime.now() + timedelta(minutes=8)
        if not user:
            usersave=User(useremail=useremail,password=hashing_password,otp=str(otp),otp_valid_time=otp_vaild_time)
            usersave.save()
            msg = Message(subject='OTP', sender='', recipients=[useremail])
            msg.body = str(otp)
            msg.html = render_template("otp.html",otp=otp)
            mail.send(msg)
            return jsonify({"message":"sent otp"}),200
        return jsonify({"Error":"Email is already registered"}),401


@app.route('/api/v1/validate',methods=['POST'])
def validate():
    data=request.json
    usermail=data["useremail"]
    userotp=data['otp']
    expiry_time = datetime.now()
    print(expiry_time)
    if usermail and userotp:
        user = User.objects(otp=userotp).first()
        print(user.otp_valid_time,expiry_time)
        if user.otp == userotp:
            if user.otp_valid_time >= expiry_time:
                return "Otp varification succesfull" ,200
        return "Please Try Again",401
