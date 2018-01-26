from flask import jsonify
from mongoengine import *
from post_model import Post
connect('ssipdb')

def get_all_posts(user):
    teams = user.teams
    posts = Post.objects(team__in = teams)
    return jsonify({'posts': [post.to_json() for post in posts]})

def create_a_post(post_json):
    content = post_json['content']
    team = post_json['team']
    post = Post(content=content, team=team)
    post.save()
    return jsonify(post.to_json())
