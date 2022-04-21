from datetime import timedelta
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'fhir',
    'host': 'localhost',
    'port': 27017
}

app.config["JWT_TOKEN_LOCATION"] = ["headers"]
app.config["JWT_SECRET_KEY"] = "supersecret"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=7)

JWTManager(app)

db = MongoEngine(app)

from fhir import collection,user,api, swagger, static
