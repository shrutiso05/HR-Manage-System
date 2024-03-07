# HRMS (Human Resource Management System) Project

This project is a Human Resource Management System (HRMS) developed using Django.

## Setup Instructions

1. Clone the repository to your local machine:

git clone <repository_url>

css
Copy code

2. Navigate to the project directory:

cd hrms_project

markdown
Copy code

3. Install the required dependencies:

pip install -r requirements.txt

css
Copy code

4. Apply migrations to create the database schema:

python manage.py migrate

css
Copy code

5. Create a superuser account to access the admin panel:

python manage.py createsuperuser

markdown
Copy code

6. Run the development server:

python manage.py runserver

markdown
Copy code

7. Access the application in your web browser at http://127.0.0.1:8000/.

## Usage

- Use the admin panel to manage employee data, attendance records, and department reports.
- Access the employee portal to view attendance records, mark attendance, and generate department reports.

## Features

- User authentication and authorization system.
- CRUD operations for managing employee data and attendance records.
- Department-wise employee count reports.
- Responsive user interface for optimal user experience.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository on GitHub.
2. Clone your forked repository to your local machine.
3. Create a new branch to work on your feature or bug fix.
4. Commit your changes and push your branch to your forked repository.
5. Submit a pull request to the main repository's master branch for review.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for detail






#Database Schema
The HRMS project utilizes a relational database schema to manage employee data, attendance records, and department information. The primary entities in the database schema are:

#Employee
name: CharField - The name of the employee.
designation: CharField - The designation of the employee.
department: CharField - The department of the employee.
date_of_joining: DateField - The date when the employee joined the company.
attendance_date: DateField (optional) - The date of attendance for the employee.
is_present: BooleanField - Indicates whether the employee is present on the attendance date.

#Attendance
employee: ForeignKey - The associated employee.
date: DateField - The date of attendance.
status: CharField - The status of the attendance ('Present' or 'Absent').


#Design Decisions
#Separation of Concerns
The project adheres to the MVC (Model-View-Controller) architecture, separating data models from views and controllers. This separation ensures better maintainability and scalability of the application.
#Django ORM
The project leverages Django's built-in Object-Relational Mapping (ORM) to interact with the database. The ORM provides an abstraction layer that simplifies database operations and enhances code readability.
#User Authentication and Authorization
Django's authentication system is used to authenticate users and manage user permissions. Only authorized users can access sensitive functionalities such as adding employees, marking attendance, and generating department reports.
#RESTful APIs
The project exposes RESTful APIs for managing employee data and attendance records. This allows external applications to integrate with the HRMS system and perform CRUD operations on employee-related data.
#Responsive UI
The user interface is designed to be responsive and accessible across various devices and screen sizes. Responsive design ensures a consistent user experience across desktops, tablets, and mobile devices.
#Scalability
The database schema is designed to accommodate future enhancements and scalability requirements. As the organization grows and evolves, the HRMS system can adapt to new business needs and accommodate additional functionalities.
#Documentation and Comments
Proper documentation and comments are included throughout the codebase to facilitate code understanding and maintenance. Docstrings, comments, and coding best practices are followed to enhance code readability and maintainability.
By adhering to these design decisions and database schema, the HRMS project aims to provide an efficient and scalable solution for managing human resources within the organization.





