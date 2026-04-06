# 🎓 Student Placement Prediction

## Overview
A Machine Learning web application built to predict a student's probability of securing a campus placement. The model evaluates academic and extracurricular metrics to provide actionable, tiered feedback rather than a simple binary output.

## Tech Stack
* **Language:** Python
* **Frontend:** Streamlit
* **Machine Learning:** Scikit-Learn (Random Forest Classifier)
* **Data Manipulation:** Pandas, NumPy

## How to Run Locally
1. Clone this repository.
2. Create a virtual environment and activate it.
3. Install dependencies: `pip install pandas scikit-learn streamlit`
4. Generate the dataset and train the model:
   ```bash
   python create_data.py
   python train_model.py