from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('list_employees/', views.list_employees, name='list_employees'),
    path('mark_attendance/<int:employee_id>/', views.mark_attendance, name='mark_attendance'),
    path('retrieve_attendance/<int:employee_id>/', views.retrieve_attendance, name='retrieve_attendance'),
    path('employee/<int:employee_id>/', views.employee_detail, name='employee_detail'),
   

]