from mongoengine import *
from team_model import Team
import datetime

class Comment(EmbeddedDocument):
    content = StringField(required=True)
    createdDate = DateTimeField(default=datetime.datetime.now)

    def to_json(self):
        return {
            "content": self.content,
            "createdDate": self.createdDate
        }

class Post(Document):
    team = ReferenceField(Team)
    createdDate = DateTimeField(default=datetime.datetime.now)
    content = StringField(required=True)
    upVoteCount = IntField(min_value=0, default=0)
    downVoteCount = IntField(min_value=0, default=0)
    comments = ListField(EmbeddedDocumentField(Comment))

    def to_json(self):
        return {
            "id": str(self.id),
            "team": self.team.to_json(),
            "createdDate": self.createdDate,
            "content": self.content,
            "upVoteCount": self.upVoteCount,
            "downVoteCount": self.downVoteCount,
            "comments": [comment.to_json() for comment in self.comments]
        }
