#-*:utf-8 -*-
import string
def findall(db_object):
    try:
       res = db_object.objects.all()
    except:
       res = None
    return res
def findallif(db_object,data):
    try:
       res = db_object.objects.filter(**data)
    except:
       res = None
    return res
def finddata(db_object,data):
    try:
       res = db_object.objects.get(**data)
    except:
       res = None 
    return res
def savedata(db_object,data):
    try:
       db_object.objects.create(**data)
       res = 1
    except:
       res = 0
    return res
def updatedata(db_object,data,storedata):
    db_object.objects.filter(**data).update(**storedata)
    #return data
