from mongoengine import register_connection, Document, StringField
from settings import MONGODB_URI

register_connection('default', host=MONGODB_URI)


class Fruit(Document):
    name = StringField()
    meta = {'collection': 'fruits'}
