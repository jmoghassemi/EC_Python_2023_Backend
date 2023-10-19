from flask import Flask

print("The name of the flask application = ", __name__)

# app is where we will store the Flask object. 
app = Flask(__name__)

from app_directory import routes
