from datetime import timedelta
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_mongoengine import MongoEngine
from pymongo import MongoClient

app = Flask(__name__)
mail = Mail(app)
client =MongoClient()
app.config['MONGODB_SETTINGS'] = {
    'db': 'fhir',
    'host': 'localhost',
    'port': 27017
}
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

app.config["JWT_TOKEN_LOCATION"] = ["headers"]
app.config["JWT_HEADER_NAME"] = "Authorization"
app.config["JWT_HEADER_TYPE"] = ""
app.config["JWT_SECRET_KEY"] = "supersecret"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=7)

JWTManager(app)
clustor=client['fhir']
fhir_collection=clustor['fhir_resources']
db = MongoEngine(app)

from fhir import collection,user,login_api, swagger, static,login_validation,search_api,user_create_api

