from django.contrib import admin
from .models import Quize

@admin.register(Quize)
class Quize(admin.ModelAdmin):
    list_display = ('timestamp','gender','age')
    list_filter = ('timestamp','gender','age', 'time', 'money', 'height')

# Register your models here.
