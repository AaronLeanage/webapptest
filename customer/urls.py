from django.urls import path
from customer import views

urlpatterns = [
    path("", views.home, name="home"),
    path("cusAdd", views.cusAdd, name="cusAdd"),
    path("cusAll", views.cusAll, name="cusAll"),
    path("cusJson", views.cusJson, name="cusJson"),
    path("cusJson/<i>", views.recordAsJSON, name="showJson"),
    path("log/", views.cusAdd, name="log"),
    path("cusDelete/<cusid>", views.cusDelete, name="cusDelete"),
    path("search/<q>", views.searchAjax, name="search"),
]