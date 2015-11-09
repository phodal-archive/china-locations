#!/usr/bin/python
# -*- coding: utf-8 -*-

from peewee import *
import codecs

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
provinces = Sheng.select().where(Sheng.parentId == "0")

with codecs.open("location.csv", "w", "utf-8") as text:
    for province in provinces:
        cities = Sheng.select().where(Sheng.parentId == province.id)
        for city in cities:
            zones = Sheng.select().where(Sheng.parentId == city.id)
            for zone in zones:
                tones = Sheng.select().where(Sheng.parentId == zone.id)
                for tone in tones:
                    print province.areaname + city.areaname + zone.areaname + tone.areaname
                    # text.write("%s" % province.areaname + city.areaname + zone.areaname + tone.areaname)
db.close()
