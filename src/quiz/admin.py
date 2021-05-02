from django.contrib import admin
from .models import Quize

@admin.register(Quize)
class Quize(admin.ModelAdmin):
    list_display = ('timestamp','gender','age','time','money','contactsport','how','fitnesslevel','height','alone','group','family','flexibility','focus','lower_body','balance','endurance')
    list_filter = ('timestamp','gender','age', 'time', 'money', 'contactsport','how','fitnesslevel','height')

# Register your models here.
