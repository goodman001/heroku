# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from userLogin.models import Userlist
from userLogin.functions import findall,finddata,savedata,updatedata
import datetime
# Create your views here.
def index(request):
    return render(request, 'userLogin/index.html')
'''
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pwd = request.POST['password']
        data = {"username": username,"passwd":pwd}
        res = finddata(Userlist,data)
        if res == None:
            return HttpResponse('<html><script type="text/javascript">alert("Sorry!Username or password is wrong!"); window.location="/"</script></html>')
        else:
            data_2 ={"login_time":datetime.datetime.now()}
            updatedata(Userlist,data,data_2)
            datalist = {"username":res.username,"email":res.email,"reg_time":res.reg_time,"login_time":res.login_time}
            response= render_to_response('userLogin/userinfo.html', {'infolist':datalist}) 
            #response.set_cookie('username',username,3600)
            return response
           
def logoff(request):
    return HttpResponse('<html><script type="text/javascript">alert("Goodbye!"); window.location="/"</script></html>')     
'''   
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
