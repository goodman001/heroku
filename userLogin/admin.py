from django.contrib import admin

# Register your models here.
from .models import Userlist
# Register your models here.
class UserlistAdmin(admin.ModelAdmin):
    list_display = ('id','firstname','lastname','email','reg_time','login_time')

admin.site.register(Userlist,UserlistAdmin)

