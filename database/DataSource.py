# encoding:utf-8

from peewee import *
from ConfigTool import getConnString

mqtt_test =getConnString('mqtt_test')
mqtt_test_database = MySQLDatabase('mqtt_test',
                               threadlocals=True,**{'host':mqtt_test.host,
                                                    'password':mqtt_test.passwd,
                                                    'port':mqtt_test.port,
                                                    'user':mqtt_test.user,
                                                    'charset':mqtt_test.charset
                                                    })