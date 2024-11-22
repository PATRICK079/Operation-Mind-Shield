# 🧠 Operation Mind Shield: Decoding Alzheimer's


<img width="1047" alt="alzheimer image" src="https://github.com/user-attachments/assets/c7233ec6-4bcf-440e-ad09-f97e7bb4ec0e">


# Problem statement
The goal is to develop a predictive solution that can help healthcare providers identify individuals at risk of Alzheimer's Disease at an earlier stage. Such a solution could assist doctors in making informed decisions regarding further diagnostic evaluations, treatment plans, and interventions, leading to improved patient quality of life.


## Dataset Dictionary

- **PatientID:** A unique identifier assigned to each patient (4751 to 6900).
- **Age:** The age of the patients ranges from 60 to 90 years.
- **Gender:** Gender of the patients, where 0 represents Male and 1 represents Female.
- **Ethnicity:** The ethnicity of the patients, coded as follows:
    - 0: Caucasian
    - 1: African American
    - 2: Asian
    - 3: Other
- **EducationLevel:** The education level of the patients, coded as follows:
    - 0: None
    - 1: High School
    - 2: Bachelor's
    - 3: Higher
- **BMI:** Body Mass Index of the patients, ranging from 15 to 40.
- **Smoking:** Smoking status, where 0 indicates No and 1 indicates Yes.
- **AlcoholConsumption:** Weekly alcohol consumption in units, ranging from 0 to 20.
- **PhysicalActivity:** Weekly physical activity in hours, ranging from 0 to 10.
- **DietQuality:** Diet quality score, ranging from 0 to 10.
- **SleepQuality:** Sleep quality score, ranging from 4 to 10.
- **FamilyHistoryAlzheimers:** Family history of Alzheimer's Disease, where 0 indicates No and 1 indicates Yes.
- **CardiovascularDisease:** Presence of cardiovascular disease, where 0 indicates No and 1 indicates Yes.
- **Diabetes:** Presence of diabetes, where 0 indicates No and 1 indicates Yes.
- **Depression:** Presence of depression, where 0 indicates No and 1 indicates Yes.
- **HeadInjury:** History of head injury, where 0 indicates No and 1 indicates Yes.
- **Hypertension:** Presence of hypertension, where 0 indicates No and 1 indicates Yes.
- **SystolicBP:** Systolic blood pressure, ranging from 90 to 180 mmHg.
- **DiastolicBP:** Diastolic blood pressure, ranging from 60 to 120 mmHg.
- **CholesterolTotal:** Total cholesterol levels, ranging from 150 to 300 mg/dL.
- **CholesterolLDL:** Low-density lipoprotein cholesterol levels, ranging from 50 to 200 mg/dL.
- **CholesterolHDL:** High-density lipoprotein cholesterol levels, ranging from 20 to 100 mg/dL.
- **CholesterolTriglycerides:** Triglycerides levels, ranging from 50 to 400 mg/dL.
- **MMSE:** Mini-Mental State Examination score, ranging from 0 to 30. Lower scores indicate cognitive impairment.
- **FunctionalAssessment:** Functional assessment score, ranging from 0 to 10. Lower scores indicate greater impairment.
- **MemoryComplaints:** Presence of memory complaints, where 0 indicates No and 1 indicates Yes.
- **BehavioralProblems:** Presence of behavioral problems, where 0 indicates No and 1 indicates Yes.
- **ADL:** Activities of Daily Living score, ranging from 0 to 10. Lower scores indicate greater impairment.
- **Confusion:** Presence of confusion, where 0 indicates No and 1 indicates Yes.
- **Disorientation:** Presence of disorientation, where 0 indicates No and 1 indicates Yes.
- **PersonalityChanges:** Presence of personality changes, where 0 indicates No and 1 indicates Yes.
- **DifficultyCompletingTasks:** Presence of difficulty completing tasks, where 0 indicates No and 1 indicates Yes.
- **Forgetfulness:** Presence of forgetfulness, where 0 indicates No and 1 indicates Yes.
- **Diagnosis:** Diagnosis status for Alzheimer's Disease, where 0 indicates No and 1 indicates Yes.
- **DoctorInCharge:** This column contains confidential information about the doctor in charge, with "XXXConfid" as the value for all patients.


# Tools Used
● Python

● Streamlit

● Scikit-learn

# How It Works

The prediction model is a CatBoost Classifier. After performing feature importance analysis with SelectKbest and correlation matrix, the following 5 features were identified as the most predictors out of 32 predictors:

Functional Assessment Score (FA): Between 0 and 10. Lower scores indicate greater impairment.
Activities of Daily Living (ADL) Score: Between 0 and 10. Lower scores indicate greater impairment.
Mini-Mental State Examination (MMSE) Score: Between 0 and 30. Lower scores indicate cognitive impairment.
Memory Complaints: Indicates if the patient reports memory issues (Yes/No).
Behavioral Problems: Indicates if the patient has behavioral issues (Yes/No).
The model was trained using only these 5 key features and fine-tuned thoroughly to match expectation, achieving a mean accuracy of 95.81%, validated through k-fold cross-validation.

# Application Workflow

1. ### Enter Patient Data:

Enter values for the 5 key features.

Click "Predict" to analyze the input data.


2. ###  Get Prediction:

The app uses the trained CatBoost model to evaluate the input features.

It returns a prediction whether a patient is likely to be diagnosed with Alzheimer's Disease.


You can check out the Streamlit app here: https://operation-mind-shield-mjz3fvpkbgn5bphhsb2ymj.streamlit.app/

You can access the Flask API deployment here:

Flask API Docker Deployment
AWS Elastic Beanstalk Deployment:
http://alzhimer-detection.eu-west-1.elasticbeanstalk.com

# 🧠 How It Works:

The API accepts diagnostic data (such as scores from the Mini-Mental State Exam (MMSE) and Activities of Daily Living (ADL)) and returns a prediction of Alzheimer’s disease risk.
Below is a sample Python request that sends data to the API for prediction:

API CALL = alzheimers_dectection

import requests

url ='http://alzheimer-detection-dev.eu-west-1.elasticbeanstalk.com/alzheimers_dectection'



     data = [{

    "Functional Assessment Score (0-10)": 3,
    
    "Activities of Daily Living (ADL) Score (0-10)": 7,
    
    "Mini-Mental State Exam (MMSE) Score (0-30)": 8,
    
    "Memory Complaints(Yes=1 No=0)": 1,
    
    "Behavioral Problems(Yes=1 No=0)": 1    
    
    }]
    headers = {'Content-Type': 'application/json'}

      response = requests.post(url, json=data, headers=headers)

      print(response.json())








