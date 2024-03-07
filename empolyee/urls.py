from django.urls import path
from . import views

urlpatterns = [
    #home page
    path('', views.home, name='home'),

    #add new employee
    path('add_employee/', views.add_employee, name='add_employee'),

    #list all the employees in JSON format
    path('list_employees/', views.list_employees, name='list_employees'),

    #Mark attendance for a specific employee
    path('mark_attendance/<int:employee_id>/', views.mark_attendance, name='mark_attendance'),

    #Retrive attendance records for a specific employee
    path('retrieve_attendance/<int:employee_id>/', views.retrieve_attendance, name='retrieve_attendance'),

    #Employee detail page with attendance records
    path('employee/<int:employee_id>/', views.employee_detail, name='employee_detail'),

    #Employee department report
    path('employee_department_report/', views.employee_department_report, name='employee_department_report'),

]