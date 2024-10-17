import streamlit as st
import pickle
import pandas as pd

# Load the trained model
with open('model_gbm.pkl', 'rb') as file:
    model = pickle.load(file)

# Define the prediction function
def predict_churn(features):
    prediction = model.predict_proba([features])
    return prediction[0][1]  # Probability of churn

# Streamlit app
st.title("Customer Churn Prediction")

# Create input fields for each feature in the specified order
features = []

# Group features in threes based on the specified order
feature_groups = [
    # Group 1
    [
        ('Gender', ['Male', 'Female'], lambda x: 1 if x == 'Male' else 0),
        ('Tenure Months', ['0-24', '25-48', '49-72'], lambda x: {"0-24": 0, "25-48": 1, "49-72": 2}[x]),
        ('Phone Service', ['Yes', 'No'], lambda x: 1 if x == 'Yes' else 0)
    ],
    # Group 2
    [
        ('Multiple Lines', ['No', 'Yes', 'No phone service'], lambda x: {'No': 0, 'Yes': 2, 'No phone service': 1}[x]),
        ('Internet Service', ['DSL', 'Fiber optic', 'No'], lambda x: {'DSL': 0, 'Fiber optic': 1, 'No': 2}[x]),
        ('Online Security', ['Yes', 'No', 'No internet service'], lambda x: {'Yes': 2, 'No': 0, 'No internet service': 1}[x])
    ],
    # Group 3
    [
        ('Online Backup', ['Yes', 'No', 'No internet service'], lambda x: {'Yes': 2, 'No': 0, 'No internet service': 1}[x]),
        ('Device Protection', ['Yes', 'No', 'No internet service'], lambda x: {'Yes': 2, 'No': 0, 'No internet service': 1}[x]),
        ('Tech Support', ['Yes', 'No', 'No internet service'], lambda x: {'Yes': 2, 'No': 0, 'No internet service': 1}[x])
    ],
    # Group 4
    [
        ('Streaming TV', ['Yes', 'No', 'No internet service'], lambda x: {'Yes': 2, 'No': 0, 'No internet service': 1}[x]),
        ('Streaming Movies', ['Yes', 'No', 'No internet service'], lambda x: {'Yes': 2, 'No': 0, 'No internet service': 1}[x]),
        ('Contract', ['Month-to-month', 'One year', 'Two year'], lambda x: {'Month-to-month': 0, 'One year': 1, 'Two year': 2}[x])
    ],
    # Group 5
    [
        ('Total Charges', ["0-4351", "4352-9000"], lambda x: {"0-4351": 0, "4352-9000": 1}[x]),
        ('CLTV', ["0-3502", "3503-5001", "5002-6500"], lambda x: {"0-3502": 0, "3503-5001": 1, "5002-6500": 2}[x])
    ],
    # Group 6
    [
        ('Age', ["0-17", "18-44", "45-64", "65+"], lambda x: {"0-17": 0, "18-44": 1, "45-64": 2, "65+": 3}[x]),
        ('Married', ['Yes', 'No'], lambda x: 1 if x == 'Yes' else 0),
        ('Number of Dependents', ['0', '1', '2', '3+'], lambda x: {"0": 0, "1": 1, "2": 2, "3+": 3}[x])
    ],
    # Group 7
    [
        ('Referred a Friend', ['Yes', 'No'], lambda x: 1 if x == 'Yes' else 0),
        ('Offer', ['None', 'Offer A', 'Offer B', 'Offer C', 'Offer D', 'Offer E'], 
         lambda x: {'None': 0, 'Offer A': 1, 'Offer B': 2, 'Offer C': 3, 'Offer D': 4, 'Offer E': 5}[x]),
        ('Avg Monthly GB Download', ["0-28", "29-56", "57-100"], lambda x: {"0-28": 0, "29-56": 1, "57-100": 2}[x])
    ],
    # Group 8
    [
        ('Streaming Music', ['Yes', 'No'], lambda x: 1 if x == 'Yes' else 0),
        ('Unlimited Data', ['Yes', 'No'], lambda x: 1 if x == 'Yes' else 0),
        ('Monthly Charge', ["0-51", "52-85", "86-120"], lambda x: {"0-51": 0, "52-85": 1, "86-120": 2}[x])
    ],
    # Group 9
    [
        ('Total Refunds', ["0-16", "17-33", "34-50"], lambda x: {"0-16": 0, "17-33": 1, "34-50": 2}[x]),
        ('Total Extra Data Charges', ["0-50", "51-100", "101-150"], lambda x: {"0-50": 0, "51-100": 1, "101-150": 2}[x]),
        ('Total Long Distance Charges', ["0-1188", "1199-2376", "2377-3565"], lambda x: {"0-1188": 0, "1199-2376": 1, "2377-3565": 2}[x]),
    ],
    # Group 10
    [
        ('Total Revenue', ["0-4007", "4008-7993", "7994-12000"], lambda x: {"0-4007": 0, "4008-7993": 1, "7994-12000": 2}[x]),
        ('Satisfaction Score', ['1', '2', '3', '4', '5'], lambda x: int(x)),
    ]
]

# Loop through the feature groups and create input fields
for group in feature_groups:
    cols = st.columns(len(group))  # Create columns for the current group
    for col, (label, options, encoding) in zip(cols, group):
        with col:
            value = st.selectbox(label, options)
            encoded_value = encoding(value)
            features.append(encoded_value)

# Predict button
if st.button("Predict"):
    if len(features) == 28:  # Ensure we have the correct number of features
        probability = predict_churn(features)
        st.success(f"The probability of customer churn is: {probability:.2f}")
        # st.success(f"The probability of customer churn is: {features}")
    else:
        st.error("There was an error with the input features. Please check the inputs.")
