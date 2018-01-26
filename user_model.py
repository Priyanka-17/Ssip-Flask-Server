from mongoengine import *
from flask_login import UserMixin
from team_model import Team
import datetime

class User(Document, UserMixin):
    name = StringField(required=True)
    teams = ListField(ReferenceField(Team))
    username = StringField(primary_key=True, required=True)
    password = StringField(required=True)
    createdDate = DateTimeField(default=datetime.datetime.now)

    def to_json(self):
        return {
            "id": str(self.id),
            "name": self.name
        }
