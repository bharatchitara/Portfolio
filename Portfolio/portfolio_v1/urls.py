from django.urls import path, re_path

from portfolio_v1 import views

urlpatterns = [ 
            path("",views.base,name = "base" )
               
               ]

