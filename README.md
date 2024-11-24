## Project Overview
This project demonstrates the creation of a data lakehouse solution to process sensor and mobile app data collected from the STEDI Step Trainer. The system is designed to enable advanced machine learning models to detect steps accurately while prioritizing data privacy. Using AWS Glue and Spark, the project involves data extraction, transformation, and curation to prepare high-quality datasets for analytical and machine learning purposes.

The solution integrates data from motion sensors embedded in the STEDI Step Trainer and companion mobile apps, showcasing a comprehensive end-to-end data engineering pipeline on AWS. 

## Key Objectives
- Extract sensor data from the STEDI Step Trainer and user data from the mobile application.
- Transform the raw data into trusted and curated datasets while filtering sensitive information.
- Create a centralized, queryable data repository to support machine learning model training.

## STEDI Step Trainer Details
The STEDI Step Trainer combines hardware and software innovations:
- **Balance Exercise Training**: Guides users in performing balance exercises.
- **Motion Sensors**: Capture step data using distance detection.
- **Mobile Application**: Leverages accelerometer data to detect motion in X, Y, and Z directions.

This project focuses on leveraging shared customer data to refine the machine learning model for accurate real-time step detection.

---

## Data Engineering Workflow

### 1. Landing Zone
The landing zone stores raw, unprocessed data ingested from various sources.

#### Artifacts:
- Glue Tables:
  - **Customer Landing Table**: [customer_landing.sql](./scripts/customer_landing.sql)
  - **Accelerometer Landing Table**: [accelerometer_landing.sql](./scripts/accelerometer_landing.sql)
  - **Step Trainer Landing Table**: [step_tranier_landing.sql](./scripts/step_tranier_landing.sql)

#### Example Queries:
Screenshots show sample queries executed in Athena:
- **Customer Landing Table**:  
  <img src="./images/customer_landing.png">

- **Accelerometer Landing Table**:  
  <img src="./images/accelerometer_landing.png">

- **Step Trainer Landing Table**:  
  <img src="./images/step_tranier_landing.png">

### 2. Trusted Zone
Data in the trusted zone is processed to ensure privacy compliance and enhanced quality for analytical purposes.

#### Data Transformation:
- **Scripts**:
  - [customer_landing_to_trusted.py](./scripts/customer_landing_to_trusted.py): Filters sensitive PII data.
  - [accelerometer_landing_to_trusted.py](./scripts/accelerometer_landing_to_trusted.py): Joins privacy-compliant data.
  - [step_trainer_landing_to_trusted.py](./scripts/step_trainer_landing_to_trusted.py): Populates the `step_trainer_trusted` table with records from users who have consented to data sharing.

#### Querying Trusted Data:
- **Customer Trusted Table**:  
  <img src="./images/customer_trusted.png">
- **Accelerometer Trusted Table**:  
  <img src="./images/accelerometer_trusted.png">
- **Step Trainer Trusted Table**:  
  <img src="./images/step_trainer_trusted.png">  

### 3. Curated Zone
The curated zone contains aggregated and integrated data ready for advanced analytics and machine learning applications.

#### Data Curation:
- **Scripts**:
  - [customer_trusted_to_curated.py](./scripts/customer_trusted_to_curated.py)
  - [machine_learning_curated.py](./scripts/machine_learning_curated.py): Generates the `machine_learning_curated` table, aggregating Step Trainer and accelerometer data for research-ready datasets.

#### Querying Curated Data:
- **Customer Curated Table**:  
  <img src="./images/customer_curated.png">
- **Step Trainer Curated Table**:  
  <img src="./images/machine_learning_curated.png">  
