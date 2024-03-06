from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('list_employees/', views.list_employees, name='list_employees'),
]