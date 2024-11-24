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

#### Example Queries:
Screenshots show sample queries executed in Athena:
- **Customer Landing Table**:  
  <img src="./images/customer_landing.png">

- **Accelerometer Landing Table**:  
  <img src="./images/accelerometer_landing.png">

- **Record Count Verification**:  
  <img src="./images/landing_tables_record_count.png">

---

### 2. Trusted Zone
Data in the trusted zone is processed to ensure privacy compliance and enhanced quality for analytical purposes.

#### Data Transformation:
- **Scripts**:
  - [customer_landing_to_trusted.py](./scripts/customer_landing_to_trusted.py): Filters sensitive PII data.
  - [accelerometer_landing_to_trusted_zone.py](./scripts/accelerometer_landing_to_trusted_zone.py): Joins privacy-compliant data.
  - [step_trainer_landing_to_trusted.py](./scripts/step_trainer_landing_to_trusted.py): Populates the `step_trainer_trusted` table with records from users who have consented to data sharing.

#### Querying Trusted Data:
- **Customer Trusted Table**:  
  <img src="./images/customer_trusted.png">  
  <img src="./images/customer_trusted_check.png">

---

### 3. Curated Zone
The curated zone contains aggregated and integrated data ready for advanced analytics and machine learning applications.

#### Data Curation:
- **Scripts**:
  - [customer_trusted_to_curated.py](./scripts/customer_trusted_to_curated.py)
  - [trainer_trusted_to_curated.py](./scripts/trainer_trusted_to_curated.py): Generates the `machine_learning_curated` table, aggregating Step Trainer and accelerometer data for research-ready datasets.

#### Final Output:
- **Glue Tables Overview**:  
  <img src="./images/glue_tables.png" width=30% height=50%>

---

## Key Takeaways
This project highlights the importance of building a robust data pipeline to support data-driven applications in real-world scenarios. It demonstrates effective handling of privacy considerations, scalable data processing, and the creation of actionable datasets for machine learning.

---
