from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from datetime import datetime
from django.http import JsonResponse
from .models import Employee , Attendance
from django.views.decorators.csrf import csrf_exempt
import json
from django.urls import reverse
from django.db.models import Count


def home(request):
    employees = Employee.objects.all()
    return render(request, 'home.html', {'employees': employees})
    
@csrf_exempt
def add_employee(request):
    if request.method == 'POST':
    
        name = request.POST.get('name')
        designation = request.POST.get('designation')
        department = request.POST.get('department')
        date_of_joining = request.POST.get('date_of_joining')

    
        employee = Employee.objects.create(
            name=name,
            designation=designation,
            department=department,
            date_of_joining=date_of_joining
        )
        return HttpResponseRedirect('/')  
    return render(request, 'add_employee.html')

def list_employees(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        data = {'employees': list(employees.values())}
        return JsonResponse(data)


def retrieve_attendance(request, employee_id):
    if request.method == 'GET':
        employee = Employee.objects.get(pk=employee_id)
        attendance_records = Attendance.objects.filter(employee=employee)
        data = {
            'employee_name': employee.name,
            'attendance': [{
                'date': record.date,
                'status': record.status
            } for record in attendance_records]
        }
        return JsonResponse(data)
    
def employee_detail(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    attendance_records = Attendance.objects.filter(employee=employee)
    return render(request, 'employee_detail.html', {'employee': employee, 'attendance_records': attendance_records})

@csrf_exempt

def mark_attendance(request, employee_id):
    if request.method == 'POST':
        data = request.POST  
        employee = Employee.objects.get(pk=employee_id)
        attendance_date = datetime.strptime(data['date'], '%Y-%m-%d').date() 
        status = data['status']

        # Create or update attendance record
        attendance, created = Attendance.objects.update_or_create(
            employee=employee,
            date=attendance_date,
            defaults={'status': status}
        )

         
    else:
        employee = Employee.objects.get(pk=employee_id)
        return render(request, 'mark_attendance.html', {'employee': employee, 'employee_id': employee_id})
    



def employee_department_report(request):
    departments = Employee.objects.values('department').annotate(count=Count('department'))
    return render(request, 'employee_department_report.html', {'departments': departments})
