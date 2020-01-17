from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add',views.add,name = 'add'),
    path('MasterAdminLogin',views.MasterAdminLogin,name = 'MasterAdminLogin'),
    path('getUserDetails',views.getUserDetails,name = 'getUserDetails')
]