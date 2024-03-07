from django.shortcuts import render
from django.http import HttpResponseRedirect
from datetime import datetime
from django.http import JsonResponse
from .models import Employee , Attendance
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.db.models import Count


def home(request):
    """
    Renders the home page with a list of all employees.

    Returns:
    - Rendered HTML template displaying the home page with employees' information.
    """
    employees = Employee.objects.all()
    return render(request, 'home.html', {'employees': employees})
    
@csrf_exempt
def add_employee(request):
    """
    Adds a new employee to the database.

    Returns:
    - Redirects to the home page after adding the employee.
    """
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
    """
    Retrieves a list of all employees in JSON format.

    Returns:
    - JSON response containing a list of all employees.
    """
    if request.method == 'GET':
        employees = Employee.objects.all()
        data = {'employees': list(employees.values())}
        return JsonResponse(data)


def retrieve_attendance(request, employee_id):
    """
    Retrieves attendance records of a specific employee.

    Returns:
    - JSON response containing the attendance records of the specified employee.
    """
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
    """
    Renders the employee detail page with attendance records.

    Returns:
    - Rendered HTML template displaying the employee detail page.
    """
    employee = Employee.objects.get(pk=employee_id)
    attendance_records = Attendance.objects.filter(employee=employee)
    return render(request, 'employee_detail.html', {'employee': employee, 'attendance_records': attendance_records})

@csrf_exempt

def mark_attendance(request, employee_id):
    """
    Marks attendance for a specific employee.

    Returns:
    - Rendered HTML template for marking attendance.
    """
    if request.method == 'POST':
        data = request.POST  
        employee = Employee.objects.get(pk=employee_id)
        attendance_date = datetime.strptime(data['date'], '%Y-%m-%d').date() 
        status = data['status']

        
        attendance, created = Attendance.objects.update_or_create(
            employee=employee,
            date=attendance_date,
            defaults={'status': status}
        )
     
    else:
        employee = Employee.objects.get(pk=employee_id)
    return render(request, 'mark_attendance.html', {'employee': employee, 'employee_id': employee_id})
    



def employee_department_report(request):
    """
    Generates a report of employee counts per department.

    Returns:
    - Rendered HTML template displaying the department-wise employee count report.
    """
    departments = Employee.objects.values('department').annotate(count=Count('department'))
    return render(request, 'employee_department_report.html', {'departments': departments})
