from playhouse.db_url import connect
import peewee

db = connect('sqlite:///my_database.db')


class DayBase(peewee.Model):
    day = peewee.CharField()
    date = peewee.CharField()
    temp_morning = peewee.CharField()
    temp_night = peewee.CharField()
    state = peewee.CharField()
    img = peewee.CharField(null=True)


    class Meta:
        database = db

db.create_tables([DayBase])