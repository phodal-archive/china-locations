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
                    text.write("%s" % province.areaname)
                    text.write(",%s" % city.areaname)
                    text.write(",%s" % zone.areaname)
                    text.write(",%s" % tone.areaname)
                    text.write(",%s" % tone.lng)
                    text.write(",%s" % tone.lat)
                    text.write("\n")
db.close()
