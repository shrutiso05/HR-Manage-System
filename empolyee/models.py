from django.db import models

class Employee(models.Model):

    """
    Model representing an employee.

    Attributes:
    - name (CharField): The name of the employee.
    - designation (CharField): The designation of the employee.
    - department (CharField): The department of the employee.
    - date_of_joining (DateField): The date when the employee joined the company.
    - attendance_date (DateField, optional): The date of attendance for the employee.
    - is_present (BooleanField): Indicates whether the employee is present on the attendance date.

    Methods:
    - __str__: Returns the name of the employee.
    """
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    date_of_joining = models.DateField()
    attendance_date = models.DateField(null=True, blank=True)
    is_present = models.BooleanField(default=False)


    def __str__(self):
        return self.name

class Attendance(models.Model):
    """
    Model representing the attendance of an employee.

    Attributes:
    - employee (ForeignKey): The associated employee.
    - date (DateField): The date of attendance.
    - status (CharField): The status of the attendance ('Present' or 'Absent').

    Methods:
    - __str__: Returns the name of the associated employee.
    """
    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=(('Present', 'Present'), ('Absent', 'Absent')))

    def __str__(self):
        return self.employee.name

