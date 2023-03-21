import mongoengine


class Car(mongoengine.Document):
    # id # --> _id = ObjectId() ... dodawane automatycznie

    model = mongoengine.StringField()
    make = mongoengine.StringField()
    year = mongoengine.IntField()
    mileage = mongoengine.FloatField()
    vi_number = mongoengine.StringField()

    #
    meta = {
        'db_alias': 'core',
        'collection': 'cars'
    }