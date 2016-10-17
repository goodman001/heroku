from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Userlist(models.Model):
    firstname = models.CharField(max_length = 20 ,blank = False)
    lastname = models.CharField(max_length = 20 ,blank = True)
    passwd = models.CharField(max_length = 200,blank = True)
    email = models.CharField(max_length = 100,blank = True)
    reg_time = models.DateTimeField(auto_now_add = False)
    login_time = models.DateTimeField(auto_now_add = True)
    def __unicode__(self):
      return self.firstname
    class Meta:
      ordering = ['-login_time']
class Journal(models.Model):
    uid = models.IntegerField(default = 1)
    Title = models.CharField(max_length = 1024 ,blank = False)
    Content = models.CharField(max_length = 2048 ,blank = False)
    Createtime = models.DateTimeField(auto_now_add = True)
    def __unicode__(self):
      return self.uid
    class Meta:
      ordering = ['-Createtime']
