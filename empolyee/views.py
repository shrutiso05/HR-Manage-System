from django.shortcuts import render
from django.http import HttpResponse

from django.http import JsonResponse
from .models import Employee
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

@csrf_exempt
def list_employees(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        data = {'employees': list(employees.values())}
        return JsonResponse(data)

