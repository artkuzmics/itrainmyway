from django.contrib import admin
from .models import Quize, Enquirie

@admin.register(Quize)
class Quize(admin.ModelAdmin):
    list_display = ('timestamp','gender','age','time','money','contactsport','how','fitnesslevel','height','alone','group','family','flexibility','focus','lower_body','balance','endurance','selected','likely_to_recommend')
    list_filter = ('timestamp','gender','age', 'time', 'money', 'contactsport','how','fitnesslevel','height')

@admin.register(Enquirie)
class Enquirie(admin.ModelAdmin):
    list_display = ('name','timestamp','email','company_name','website','comment')
    list_filter = ('name','timestamp')


# Register your models here.
