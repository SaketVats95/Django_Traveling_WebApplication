from django.urls import path,re_path

from . import views

urlpatterns = [
    path('Msg/<articleID>/',views.ShowMessage),
    path('Msg/',views.ShowMessage),
    path('showAdd', views.showAdd, name='hello'),
    path('', views.Hello, name='hello'),
    re_path(r'a$',views.Hello)
    
]