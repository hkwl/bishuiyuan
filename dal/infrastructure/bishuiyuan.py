# encoding:utf-8

from peewee import *
from database.DataSource import mqtt_test_database

class UnKnowField(object):
    pass

class BaseModel(Model):
    class Meta:
        database = mqtt_test_database

class BiShuiYuan(BaseModel):
    id = IntegerField()
    tds = IntegerField()
    water = IntegerField()
    create_time = CharField()
    class Meta:
        db_table = 'bishuiyuan'
