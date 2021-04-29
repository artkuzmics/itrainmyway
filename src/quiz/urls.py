from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "quiz"

urlpatterns = [
    path('', views.homepage),
    path('quiz',views.quiz)
]
