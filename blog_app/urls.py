from django.urls import path
from .views import details,about_me,content_list,index
from django.conf.urls import url

urlpatterns = [
    path('', index ,name='index'),
    path('details/<int:id>',details,name='details'),
    #url(r'^(?P<id>\d+)/$', views.details, name='detail'),
    path('about_me/',about_me,name='about_me'),
    path('content_list/',content_list,name='content_list'),
    

]