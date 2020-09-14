# shop/urls.py
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.home),   
    url(r'^register/',views.register),
    url(r'^login/',views.User_login),
    url(r'^personal/',views.personal),
    url(r'^logout/',views.User_logout),
    url(r'^reset',views.reset_password),   
    url(r'^coursestart/',views.coursestart),
    url(r'^class1/',views.class1), 
    url(r'^htmlcss/',views.htmlcss),
    #留言板


]

