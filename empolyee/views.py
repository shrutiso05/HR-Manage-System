from django.shortcuts import render
from django.http import HttpResponse

from django.http import JsonResponse
from .models import Employee , Attendance
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
    employees = Employee.objects.all()
    return render(request, 'home.html', {'employees': employees})
    

@csrf_exempt
def add_employee(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        employee = Employee.objects.create(
            name=data['name'],
            designation=data['designation'],
            department=data['department'],
            date_of_joining=data['date_of_joining']
        )
        return JsonResponse({'message': 'Employee added successfully!'})


def list_employees(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        data = {'employees': list(employees.values())}
        return JsonResponse(data)

def mark_attendance(request, employee_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        employee = Employee.objects.get(pk=employee_id)
        attendance_date = data['attendance_date']
        is_present = data['is_present']
        # Create or update attendance record
        attendance, created = Attendance.objects.update_or_create(
            employee=employee,
            date=attendance_date,
            defaults={'status': 'Present' if is_present else 'Absent'}
        )
        return JsonResponse({'message': 'Attendance marked successfully!'})


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
