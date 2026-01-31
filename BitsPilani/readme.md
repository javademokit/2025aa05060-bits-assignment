# ML Assignment 2 – Classification Models & Streamlit Deployment

## a. Problem Statement
The objective of this assignment is to implement multiple machine learning
classification models on a single dataset, evaluate their performance using
standard metrics, and deploy the models using an interactive Streamlit web
application.

## b. Dataset Description
- Dataset Type: Dummy Classification Dataset (synthetically generated)
- Number of Instances: 600
- Number of Features: 12 (numerical)
- Target Variable: Binary class (0 / 1)
- Dataset is generated programmatically to ensure originality and avoid plagiarism.

## c. Models Used and Evaluation Metrics

The following machine learning models were implemented on the same dataset:

1. Logistic Regression  
2. Decision Tree Classifier  
3. K-Nearest Neighbors  
4. Naive Bayes (Gaussian)  
5. Random Forest (Ensemble)  
6. XGBoost (Ensemble)

### Comparison Table

| ML Model | Accuracy | AUC | Precision | Recall | F1 Score | MCC |
|--------|---------|-----|-----------|--------|----------|-----|
| Logistic Regression | 0.52 | 0.51 | 0.53 | 0.50 | 0.51 | 0.03 |
| Decision Tree | 0.49 | 0.48 | 0.49 | 0.49 | 0.49 | -0.01 |
| KNN | 0.51 | 0.50 | 0.52 | 0.51 | 0.51 | 0.02 |
| Naive Bayes | 0.50 | 0.50 | 0.50 | 0.50 | 0.50 | 0.00 |
| Random Forest | 0.53 | 0.52 | 0.54 | 0.53 | 0.53 | 0.05 |
| XGBoost | 0.54 | 0.53 | 0.55 | 0.54 | 0.54 | 0.06 |

## d. Model Performance Observations

| Model | Observation |
|------|------------|
| Logistic Regression | Performs moderately on linear patterns |
| Decision Tree | Tends to overfit on random data |
| KNN | Sensitive to feature scaling |
| Naive Bayes | Assumes feature independence |
| Random Forest | More stable due to ensemble learning |
| XGBoost | Best overall performance on dummy data |

## e. Streamlit Deployment
The Streamlit application includes:
- CSV dataset upload option
- Model selection dropdown
- Display of evaluation metrics
- Confusion matrix visualization

The app is deployed using Streamlit Community Cloud.
