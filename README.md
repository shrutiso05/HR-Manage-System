# HRMS Django Application

This is a Human Resource Management System (HRMS) built using Django. It provides functionalities for employee management, attendance tracking, and basic reporting.

## Project Overview

The HRMS Django application consists of the following features:

- Employee management: Add new employees and retrieve a list of all employees.
- Attendance tracking:
- Basic reporting:

## Getting Started

Follow the steps below to set up and run the HRMS Django application:

### Prerequisites

Make sure you have Python and Django installed on your system. You can install Django using pip:

pip install django

### Installation

1. Clone the repository:

git clone <repository_url>

css
Copy code

2. Navigate to the project directory:

cd hrms_django_app

markdown
Copy code

3. Install dependencies:

pip install -r requirements.txt

mathematica
Copy code

### Setting Up the Database

Run the following commands to apply migrations and create the database tables:

python manage.py makemigrations
python manage.py migrate

bash
Copy code

### Running the Development Server

Start the Django development server by running the following command:

python manage.py runserver

bash
Copy code

The HRMS application will be accessible at http://localhost:8000/.

## Usage

### Adding a New Employee

To add a new employee, you can use the API endpoint `/add_employee/`. Send a POST request with the employee details in JSON format.

Example:

POST /add_employee/
{
"name": "John Doe",
"designation": "Software Engineer",
"department": "Engineering",
"date_of_joining": "2024-03-06"
}

r
Copy code

### Retrieving the List of Employees

You can retrieve the list of all employees using the API endpoint `/list_employees/`. Send a GET request to this endpoint.

Example:

GET /list_employees/
