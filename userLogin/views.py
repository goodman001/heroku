# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from userLogin.models import Userlist
from userLogin.models import Journal
from userLogin.functions import findall,findallif,finddata,savedata,updatedata
import datetime
import logging
import json
import collections
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    return render(request, 'userLogin/index.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['firstname']
        username2 = request.POST['lastname']
        email = request.POST['email']
        pwd = request.POST['password']
        data = {"email": email}
        if username == '' or username2 =='' or email == "" or pwd == "" :
             return HttpResponse('<html><script type="text/javascript">alert("Content has empty value!Register failure"); window.location="/"</script></html>')
        nowtime =datetime.datetime.now()
        res = finddata(Userlist,data)
        if res ==None:
            data2={"firstname":username,"lastname":username2,"email":email,"passwd":pwd,"reg_time":nowtime}
            res2 = savedata(Userlist,data2)
            if res2 == 1:
                datalist = {"firstname":username,"lastname":username2,"email":email,"login_time":nowtime}
                return render(request, 'userLogin/userinfo.html',{'infolist':datalist})
            else:
                return HttpResponse('<html><script type="text/javascript">alert("Sorry!Registration failed"); window.location="/"</script></html>')
        else:
            return HttpResponse('<html><script type="text/javascript">alert("Sorry!This email address is already registered,please login"); window.location="/"</script></html>')
            return HttpResponse(data2['reg_time'])
         
        return HttpResponse(username + email)
    else:
        return HttpResponse("failure!")
def api(request):
    res = findall(Userlist)
    userlist = []
    for cell in res:
        tmp = cell.firstname + " " + cell.lastname
        userlist.append(tmp)
    s = json.dumps(userlist)
    #logging.debug(res)
    return HttpResponse(s)
def api1(request,uid):
    id_ = int(uid)
    res = finddata(Userlist,{"id":id_})
    if res != None:
        info = collections.OrderedDict()
        info["id"] = id_
        info["firstname"] = res.firstname
        info["lastname"] = res.lastname
        info["email"] = res.email
        info["passwd"] = res.passwd
        info["reg_time"] = str(res.reg_time)
        info["login_time"] = str(res.login_time) 
        s = json.dumps(info)
        return HttpResponse(s)
    else:
        return HttpResponse("Not existed the user: ")
def api2(request,uid,entry):
    id_ = int(uid)
    res = finddata(Userlist,{"id":id_})
    if res != None:
        data = {"uid":id_}
        res =findallif(Journal,data)
        if res == None:
            return HttpResponse("[*]uid " + str(id_) +" no write entry!")
        titlelist = []
        for cell in res:
            info = collections.OrderedDict()
            info["Title"] = cell.Title
            info["Content"] = cell.Content
            info["Createtime"] = str(cell.Createtime)
            titlelist.append(info)
        s = json.dumps(titlelist)
        return HttpResponse(s)
    else:
        return HttpResponse("[*]uid "+str(id_) + " no exist!")
def api3(request,uid,entry,entry_id):
    id_ = int(uid)
    id_en = int(entry_id)
    res = finddata(Userlist,{"id":id_})
    if res != None:
        data = {"uid":id_,"id":id_en}
        res =findallif(Journal,data)
        if len(res) == 0:
            return HttpResponse("[*]uid " + str(id_) +" no write entry " + str(id_en) + "!")
        titlelist = []
        for cell in res:
            info = collections.OrderedDict()
            info["Title"] = cell.Title
            info["Content"] = cell.Content
            info["Createtime"] = str(cell.Createtime)
            titlelist.append(info)
        s = json.dumps(titlelist)
        return HttpResponse(s)
    else:
        return HttpResponse("[*]uid "+str(id_) + " no exist!")
@csrf_exempt
def api4(request,uid,create):
    id_ = int(uid)
    res = finddata(Userlist,{"id":id_})
    if res == None:
       return HttpResponse("[*]Failure: create a journal entry failure!Because there is no exit the uid!")
    if request.method == 'POST':
         body_unicode = request.body.decode('utf-8')
         body = json.loads(body_unicode)
         Title = body['Title']
         Content = body['Content']
         data = { "uid":id_,"Title":Title,"Content":Content}
         res1 = savedata(Journal,data)
         if res1 == 1:
            return HttpResponse("[*]uid " + str(id_) + " create entry("+ Title+") successfully!")
         return HttpResponse(s1) 
    return HttpResponse(uid)

