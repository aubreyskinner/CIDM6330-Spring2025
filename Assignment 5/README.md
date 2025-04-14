## Assignment 4: Migrate to Django 

### Main Changes Made
#### 1. Migration from FastAPI to Django
#### 2. Switched from old repository pattern to Django ORM
#### 3. Utilized Django REST Framework
<hr>

* Models for CaseManager, Patient, HealthcareProvider, and VitalSigns were created in Django using Django's ORM
* Relationships between models were established

<hr>

### API Endpoints
* /api/patients/
* /api/case_managers/
* /api/healthcare_providers/
* /api/vital_signs/

<i>These endpoints represent GET and POST actions, appending {id}/ at the endpoint url will allow you to update and delete.</i>
<br>

<b>Example:</b>
<br>
* GET /api/patients/ – List all patients
* DELETE /api/patients/3/ – Delete patient with ID 3

### Admin Interface
#### The Django admin interface was enabled and a superuser was created 
* username: aubreyskinner
* password: abc123
* can be accessed at http://127.0.0.1:8000/admin/

#### A homepage was created to provide a simple landing page and serve as confirmation the Django app is working properly. 
It can be accessed at: http://127.0.0.1:8000/ 
