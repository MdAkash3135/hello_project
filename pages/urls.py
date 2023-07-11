from django.urls import path
from .views import ki_khobor
urlpatterns=[
    path("",ki_khobor,name= "home")
]