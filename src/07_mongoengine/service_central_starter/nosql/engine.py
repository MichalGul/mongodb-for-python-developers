import mongoengine
import uuid

class Engine(mongoengine.EmbeddedDocument): # use as sub document of other element
    horsepower = mongoengine.IntField()
    liters = mongoengine.FloatField()
    mpg = mongoengine.FloatField()
    serial_number = mongoengine.StringField(default=lambda: str(uuid.uuid4()))


