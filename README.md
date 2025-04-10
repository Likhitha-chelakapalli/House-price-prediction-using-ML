# 🏠 House Price Prediction Web App
## 📌 Project Overview
- Developed a **machine learning-based regression model** to estimate house prices.
- Built an interactive web application using **Streamlit** for easy user interaction.
- Trained using a clean dataset `house_prices_dataset.csv` with attributes affecting pricing.
- Saves the trained model with **joblib** to reuse without retraining.

---

## 🎯 Key Features
- 💻 Simple and clean **Streamlit-based UI**
- 📥 Takes inputs for:
  - Square Feet
  - Bedrooms
  - House Age
- 🤖 Real-time **House Price Prediction**
- 💾 **Model persistence** using `joblib`
- 🧠 Utilizes **Linear Regression** from `scikit-learn`

---

## 📊 Technologies Used
- **Python** 🐍  
- **Pandas, NumPy** — for data handling  
- **Scikit-learn** — for machine learning  
- **Matplotlib** — for visualization (optional)  
- **Streamlit** — to deploy the interactive web app  
- **Joblib** — for model serialization


---

## 🧪 Sample Prediction

> Inputs:
- Square Feet: 2000  
- Bedrooms: 3  
- Age: 10  

> Output:
- 🎯 **Predicted House Price**: ₹ 48,00,000.00 *(example output)*
