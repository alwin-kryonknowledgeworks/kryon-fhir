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
    print(data)
    useremail=data['useremail']
    password=data['password']
    if useremail and password:
        hashing_password=sha256_crypt.encrypt(password)
        user=User.objects(useremail=useremail).first()
        if not user:
            usersave=User(useremail=useremail,password=hashing_password,otp=str(otp))
            print(usersave)
            usersave.save()
            msg = Message(subject='OTP', sender='', recipients=[useremail])
            msg.body = str(otp)
            msg.html = render_template("otp.html",otp=otp)
            mail.send(msg)
            return jsonify({"message":"sent otp"}),200
        return jsonify({"Error":"Email is already registered"}),401


@app.route('/validate',methods=['POST'])
def validate():
    data=request.json
    usermail=data["useremail"]
    userotp=data['otp']
    if usermail and userotp:
        user = User.objects(otp=userotp).first()
        try:
           if user.otp == userotp:
             return "Otp varification succesfull" ,200
        except AttributeError:
             return "Please Try Again",401
