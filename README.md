# 📊 Clinical Nutrition Data Pipeline & Automated Reporting

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Gemini AI](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=google&logoColor=white)

## 📌 Project Overview
This project is an end-to-end **Data Engineering and Automation Pipeline** designed for clinical nutrition studies. It replaces manual spreadsheet data entry and subjective analysis with an automated Python-based workflow. 

The system ingests raw patient data, utilizes **Generative AI (LLMs)** to extract quantitative nutritional metrics from unstructured dietary recall texts, performs statistical health classifications (BMI/WHO standards), and automatically generates a final, reader-friendly PDF report for healthcare professionals.

## 🏗️ Architecture & Tech Stack
The project follows a robust ETL (Extract, Transform, Load) architecture:

* **Data Extraction & Mocking:** `pandas`, `openpyxl`, `faker`
* **AI Transformation (LLM):** `google-genai` (Gemini 2.5 Flash API)
* **Data Analysis & Visualization:** `matplotlib`, `seaborn`
* **Automated Reporting:** `fpdf2`

## ✨ Key Features
1. **Unstructured Data Parsing (AI Integration):** Translates messy, free-text 24-hour dietary recalls (e.g., "rice, beans, and steak") into structured JSON data (Calories, Proteins, Carbs, Fats) using the Google Gemini API.
2. **Automated Clinical Calculations:** Computes Body Mass Index (BMI) and categorizes patients based on official World Health Organization (WHO) reference values.
3. **Data Visualization:** Generates distribution charts and histograms to summarize the sample's nutritional status.
4. **PDF Report Generation:** Compiles findings, charts, and automated descriptive statistics into a standardized PDF document.

## 🚀 How to Run the Project

### 1. Clone the repository and set up the environment
```bash
git clone [https://github.com/YourUsername/clinical-nutrition-pipeline.git](https://github.com/YourUsername/clinical-nutrition-pipeline.git)
cd clinical-nutrition-pipeline
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
