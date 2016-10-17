#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib
import urllib2
import json
def test_api_v1_users_id_create(uid,Title,Content):
    print "[*******]Test api/v1/users/<id>/create"
    url='http://127.0.0.1:8000/api/v1/users/'+str(uid) +'/create/'
    print "[*] test url" + url
    data = json.dumps({'Title':Title,'Content':Content})
    clen = len(data)
    req = urllib2.Request(url, data, {'Content-Type': 'application/json', 'Content-Length': clen})
    f = urllib2.urlopen(req)
    response = f.read()
    print response
    f.close()
def test_api_v1_users(domain):
    print "[*******]Test api/v1/users"
    url = domain + "/api/v1/users/"
    print "[*] test url" + url
    print "[*]Output:"
    res=urllib2.urlopen(url)
    b=res.read()
    print b
def test_api_v1_users_id(domain,id_):
    print "[*******]Test api/v1/users/<id>"
    url = domain + "/api/v1/users/" +str(id_) + "/"
    print "[*] test url" + url
    print "[*]Output:"
    res=urllib2.urlopen(url)
    b=res.read()
    print b
def test_api_v1_users_id_entry(domain,id_):
    print "[*******]Test api/v1/users/<id>/entry"
    url = domain + "/api/v1/users/" +str(id_) + "/entry/" 
    print "[*] test url" + url
    print "[*]Output:"
    res=urllib2.urlopen(url)
    b=res.read()
    print b
def test_api_v1_users_id_entry_entryid(domain,id_,entryid):
    print "[*******]Test api/v1/users/<id>/entry/<id>"
    url = domain + "/api/v1/users/" +str(id_) + "/entry/" + str(entryid) +"/"
    print "[*] test url" + url
    print "[*]Output:"
    res=urllib2.urlopen(url)
    b=res.read()
    print b
test_api_v1_users_id_create(1,"Hello world","Test the create")
test_api_v1_users("http://127.0.0.1:8000")
test_api_v1_users_id("http://127.0.0.1:8000",1)
test_api_v1_users_id_entry("http://127.0.0.1:8000",1)
test_api_v1_users_id_entry_entryid("http://127.0.0.1:8000",1,4)
