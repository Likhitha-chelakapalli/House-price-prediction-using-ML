import streamlit as st
import numpy as np
import pandas as pd
import joblib
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("house_prices_dataset.csv")

# Prepare data
X = df[['Square_Feet', 'Bedrooms', 'Age']]
y = df['Price']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model for later use
joblib.dump(model, "house_price_model.pkl")

# Load trained model
model = joblib.load("house_price_model.pkl")

# Streamlit UI
st.title("🏠 House Price Prediction..")

st.write("Enter the details below to predict the house price.")

# Input fields for user
square_feet = st.number_input("Square Feet", min_value=500, max_value=10000, value=2000, step=100)
bedrooms = st.number_input("Bedrooms", min_value=1, max_value=6, value=3, step=1)
age = st.number_input("House Age", min_value=1, max_value=50, value=10, step=1)

# Prediction button
if st.button("Predict Price"):
    input_features = np.array([[square_feet, bedrooms, age]])
    predicted_price = model.predict(input_features)
    st.subheader(f"Predicted House Price: Rs: {predicted_price[0]:,.2f}")