## Assignment 5: Full Django + Tests

### Main Changes Made
#### 1. Integrated Celery/Redis for asynchronous task processing
#### 2. Extended the API with custom endpoints beyond CRUD
#### 3. Wrote unit tests using Django's built-in testing framework
<hr>

#### Celery Setup
* Celery was configured in the project folder 'vital' as vital/celery.py and contains a separate worker process
* A new tasks.py file was added to handle background jobs.

<hr>

### Custom Task Endpoints
* /start_task/
  - returns a task ID
  - initiates a background task to simulate a long-running operation
* /check_task_status/<task_id>/
  - checks the current status of a background task by task ID
  - Returns "PENDING", "STARTED", "SUCCESS"
### Example:
<b>POST /start_task/</b><br>
Response: <br>
{<br>
    "task_id": "fd6a9796-c5be-458b-8389-0af6696e974a"<br>
}<br><br>
<b>GET /check_task_status/fd6a9796-c5be-458b-8389-0af6696e974a/</b><br>
Response: <br>
{ <br>
"status": "SUCCESS", <br>
"result": "Task complete!" <br>
}<br>

### Unit Testing
Tests were written using Django's TestCase class to verify:
1. start_task returns a valid task ID
2. check_task_status correctly handles responses<br><br>
<i>Test File: vitals/tests.py</i>

