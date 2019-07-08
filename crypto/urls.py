from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("prices/",views.prices,name="prices"),
    path("contact/",views.contact,name="contact"),
    path("about/",views.about,name="about"),
    path("news/",views.news,name="news"),
]
