## Vehicle Management System

This system is used to perform CRUD (Create - Read - Update - Delete) operations on Vehicle and User module.

Users can perform different CRUD operations based on their type.
1. SuperUser: can perform all CRUD operations on both modules.
2. Admin: can perform only read and update operations.
3. User: can performs only read operation.

Existing superuser creadentials:
```bash
username: superadminuser
email: superadminuser@gmail.com
password: 1234
```

Tried to handle XSS attack by adding validations to html form.

Added custom middleware to filter the IP addresses.
For testing you can add user ip address from which request in being process in allowed_ips which is inside middleware/ip_middleware.py file

## Prerequisites
Python, Django, HTML, Bootstrap, JavaScript

## Run project locally
- Clone the project from github using httpUrl or sshUrl into you project directory
```bash
  git clone https://github.com/RajiwadeVedanti/VehicleManagement.git or git@github.com:RajiwadeVedanti/VehicleManagement.git
```

- Go to project directory
```bash
  cd vehiclemanagement
```

- Install packages required for project
```bash
  pip install -r requirements. txt
```

- Run the server. port_number is optional, by default it will be 8000
```bash
  python manage.py runserver <port_number>
```

- If new changes are made in models.py, app_name is optional
```bash
  python manage.py makemigrations <app_name>
```

- Run migrate again to create those model tables in your database
```bash
    python manage.py migrate
```

- If you don't want to use existing superuser, you can create your superuser from terminal using command
```bash
    python manage.py createsuperuser
```

- Enter your desired username and press enter.It will ask for email address and final step will be enter password
```bash
    Username: admin
    Email address: admin@example.com
    Password: **********
    Password (again): *********
    Superuser created successfully.
```

- Again run the server and you can start using project
