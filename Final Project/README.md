### Final Project: <i>Vital Signs Management System</i>
#### Problem Domain
In healthcare, tracking and recording vital signs accurately is critical for patient care. It determines how well you can help them as a caregiver and how their doctors can better assist them. Traditionally, paper documentation can be disorganized, prone to errors, and cause delays. This system digitizes the recording, storage, and retrieval of patient vital signs to address these issues. It provides a simple, secure, and efficient way for healthcare providers (CNAs, Nurses, etc.) to record patient vital signs, view health trends, and for case managers to oversee data for supervision. 
#### Users
* <b>Certified Nursing Assistants (CNAs)/ Nurses:</b>
  1. Record vital signs for patients
  2. View historical vital signs
  3. Analyze individualized patient trends in the form of graphs
* <b>Case Managers:</b>
  1. Oversee patients
  2. Monitor patient progress based on recorded vital signs
* <b>Key Entities:</b>
  1. Patients: Individuals receiving healthcare services
  2. Vital Signs: A set of measurements recorded during patient visits (blood pressure, heart rate, oxygen saturation, temperature, respiratory rate, and weight)
  3. Healthcare Providers: CNAs or Nurses recording vital signs
  4. Case Managers: Supervisors overseeing patient care and outcomes
#### Solution Summary:
The system uses a Django-based backend, powered by the Django REST Framework (DRF), to provide a fully RESTful API for managing patients, vital signs, and healthcare providers. It supports CRUD operations, ensuring efficient and structured handling. <br>
<br>
<b>Key Features:</b>
* Secure Data Storage: using Django's ORM and implementing best practices
* Data Validation: prevents entry errors and maintains integrity
* Simple Data Entry: workflows designed for fast use by CNAs and Nurses
* Visualization Tool: included trend graph to help monitor patient progress
