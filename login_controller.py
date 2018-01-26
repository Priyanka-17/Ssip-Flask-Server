from flask import jsonify
from mongoengine import *
from user_model import User
from bson import ObjectId
connect('ssipdb')

def authenticate(username, password):
    users = User.objects(username=username, password=password)
    if users is None or len(users) != 1:
        return None
    else:
        return users[0]

def get_user(user_id):
    return User.objects.get(username=user_id)

def create_user(name, username, password, team_list):
    user = User(name=name, username=username, password=password)
    for team in team_list:
        user.teams.append(ObjectId(team))
    user.save()
