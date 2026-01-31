import streamlit as st
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, roc_auc_score, precision_score, recall_score, f1_score, matthews_corrcoef, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
import matplotlib.pyplot as plt

st.title("ML Assignment 2 – Classification Models")

# Dummy dataset generation
np.random.seed(42)
X = np.random.randn(600, 12)
y = np.random.randint(0, 2, 600)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model_name = st.selectbox(
    "Select Model",
    ["Logistic Regression", "Decision Tree", "KNN", "Naive Bayes", "Random Forest", "XGBoost"]
)

models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Decision Tree": DecisionTreeClassifier(),
    "KNN": KNeighborsClassifier(n_neighbors=5),
    "Naive Bayes": GaussianNB(),
    "Random Forest": RandomForestClassifier(n_estimators=100),
    "XGBoost": XGBClassifier(use_label_encoder=False, eval_metric="logloss")
}

model = models[model_name]
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

st.subheader("Evaluation Metrics")
st.write("Accuracy:", accuracy_score(y_test, y_pred))
st.write("AUC:", roc_auc_score(y_test, y_prob))
st.write("Precision:", precision_score(y_test, y_pred))
st.write("Recall:", recall_score(y_test, y_pred))
st.write("F1 Score:", f1_score(y_test, y_pred))
st.write("MCC:", matthews_corrcoef(y_test, y_pred))

st.subheader("Confusion Matrix")
cm = confusion_matrix(y_test, y_pred)
fig, ax = plt.subplots()
ax.imshow(cm)
ax.set_xlabel("Predicted")
ax.set_ylabel("Actual")
st.pyplot(fig)
