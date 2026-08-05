# ANN Diabetes Prediction

## Overview

This project predicts whether a patient is diabetic or non-diabetic using an Artificial Neural Network (ANN). The model is built with TensorFlow/Keras and trained on a diabetes dataset after preprocessing and feature engineering.

## Features

* Data preprocessing and feature encoding
* Feature scaling using StandardScaler
* Artificial Neural Network (ANN) for binary classification
* Hyperparameter tuning using Optuna
* Early Stopping to prevent overfitting
* Model evaluation using Accuracy, Precision, Recall, F1-Score, ROC-AUC, and Confusion Matrix

## Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Scikit-learn
* TensorFlow / Keras
* Optuna

## Dataset

* Total Records: **100,000**
* Target Variable: **Diabetes**

  * 0 → Non-Diabetic
  * 1 → Diabetic

## Project Workflow

1. Data Loading
2. Data Preprocessing
3. Feature Encoding
4. Feature Scaling
5. Train-Test Split
6. ANN Model Development
7. Hyperparameter Tuning
8. Model Evaluation
9. Performance Comparison

## Model Architecture

* Input Layer
* Hidden Dense Layers (ReLU)
* Dropout
* Output Layer (Sigmoid)

## Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1-Score
* ROC-AUC Score
* Confusion Matrix

## Results

The trained ANN model achieved strong performance in predicting diabetes and was evaluated using multiple classification metrics along with ROC-AUC and Confusion Matrix.

## Installation
git clone https://github.com/your-username/ANN-Diabetes-Prediction.git
cd ANN-Diabetes-Prediction
pip install -r requirements.txt


## Run

Open the Jupyter Notebook and execute all cells.

## Project Structure

text
ANN-Diabetes-Prediction/
│── ANN_Diabetes_Prediction.ipynb
│── requirements.txt
│── README.md
│── images/

## Future Scope
* Experiment with SMOTE/ADASYN
* Compare ANN with XGBoost and Random Forest
* Perform explainability using SHAP/LIME
