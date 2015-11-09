from peewee import *

db = MySQLDatabase('location_with_zone', host="localhost", port=3306, user="root", passwd="")

class Sheng(Model):
    id = IntegerField()
    areaname = CharField()
    parentId = IntegerField()
    shortname = CharField()
    areacode = IntegerField()
    zipcode = IntegerField()
    pinyin = CharField()
    lng = CharField()
    lat = CharField()
    level = IntegerField()
    position = CharField()
    sort = IntegerField()

    class Meta:
        database = db

db.connect()
shengs = Sheng.select().where(Sheng.id == "110000")
for sheng in shengs:
    print sheng.id, sheng.areaname, sheng.shortname
db.close()