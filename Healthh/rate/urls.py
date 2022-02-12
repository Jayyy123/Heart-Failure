from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.home, name ="home"),
    path('forms/', views.forms, name ="forms"),
    path('result/<str:pk>/', views.result, name ="result"),
    path('multi/<str:pk>/', views.multi, name ="multi"),
    path('mode/', views.mode, name ="mode"),
    path('database/', views.database, name ="database"),
    path('about/', views.about, name ="about"),
    path('predict/', views.forms, name ="predict"),
    path('deletebase/<str:pk>/', views.deletebase, name = 'deletebase'),
    path('loginpage/', views.loginuser, name = 'loginpage'),
    path("logoutuser/", views.logoutuser, name="logoutuser"),
]