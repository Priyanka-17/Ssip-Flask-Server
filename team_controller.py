from flask import jsonify
from mongoengine import *
from team_model import Team
connect('ssipdb')

def get_all_teams(user):
    teams = user.teams
    return jsonify({'teams': [team.to_json() for team in teams]})

def create_a_team(team_json):
    name = team_json['name']
    team = Team(name=name)
    team.save()
    return jsonify(team.to_json())
