## Entity Relationship Diagram

### Entities and Attributes
#### 1. Healthcare Provider (User)
  * ProviderID (Primary Key)
  * FirstName
  * LastName
  * Role - <i>CNA or Nurse</i>
  
#### 2. Patient
  * PatientID (Primary Key)
  * ManagerID (Foreign Key to Case Manager)
  * FirstName
  * LastName
  * DateOfBirth
    
#### 3. Case Manager
  * ManagerID (Primary Key)
  * FirstName
  * LastName

#### 4. Vital Signs
  * VitalID (Primary Key)
  * PatientID (Foreign Key)
  * RecordedBy (Foreign Key to ProviderID)
  * TimeStamp
  * BloodPressure
  * HeartRate
  * OxygenSaturation
  * Temperature
  * RespiratoryRate
  * Weight

### Relationships Between Entities
#### 1. Heatlhcare Provider Records Vital Signs
* One Healthcare Provider can record multiple Vital Signs, but only one Healthcare Provider records each Vital Sign entry.

<b>Healthcare Provider (ProviderID) -> (1:M) -> Vital Signs (RecordedBy)</b>
#### 2. Patient Has Multiple Vital Signs Recorded
* One Patient can have multiple Vital Sign entries, but each Vital Sign entry belongs to only one Patient.

<b>Patient (PatientID) -> (1:M) -> Vital Signs (PatientID)</b>
#### 3. Case Manager Oversees Patients
* One Case Manager can oversee multiple Patients, but each Patient has only one assigned Case Manager.

<b>Case Manager (ManagerID) -> (1:M) -> Patient (ManagerID)</b>

### Diagram: 
![ERD](images/ERD.pdf)

### API in Python Using FastAPI
Included in Project: Assignment 2/CIDM6330-Code/

### Pydantic Models 
Included in Project: Assignment 2/CIDM6330-Code/models.py

### Initial Set of CRUD Transactions
Included in Project: Assignment 2/CIDM6330-Code/routes/


