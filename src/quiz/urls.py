from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "quiz"

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('quiz',views.quiz, name="q"),
    path('results',views.results, name="results"),
    path('partners',views.partners, name="partners"),
    path('thankyou',views.thankyou, name="thankyou"),

]
