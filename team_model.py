from mongoengine import *
import datetime

class Team(Document):
    name = StringField(required=True)
    createdDate = DateTimeField(default=datetime.datetime.now)

    def to_json(self):
        return {
            "id": str(self.id),
            "createdDate": self.createdDate,
            "name": self.name
        }
