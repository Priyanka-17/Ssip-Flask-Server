from flask import jsonify
from mongoengine import *
from user_model import User
connect('ssipdb')

def authenticate(username, password):
    users = User.objects(username=username, password=password)
    if users is None or len(users) != 1:
        return None
    else:
        return users[0]

def get_user(user_id):
    return User.objects.get(username=user_id)
