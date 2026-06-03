# 🎮 Video Game Global Sales Prediction

## 📌 Project Overview

This project predicts the **Global Sales** of video games using Machine Learning.

A **Random Forest Regressor** model is trained on video game sales data and deployed using **Streamlit**.

---

## 📊 Dataset Features

The model uses the following features:

* Rank
* Year
* NA_Sales
* EU_Sales
* JP_Sales
* Other_Sales
* Name Frequency
* Platform Frequency
* Genre Frequency
* Publisher Frequency

### Target Variable

* Global_Sales

---

## 🔧 Data Preprocessing

* Missing Value Handling
* Frequency Encoding
* Train-Test Split
* Feature Engineering

---

## 🤖 Machine Learning Model

**Algorithm Used:**

* Random Forest Regressor

---

## 📈 Model Evaluation

Evaluation Metrics:

* R² Score
* Mean Squared Error (MSE)

---

## 🚀 Streamlit Application

The Streamlit application allows users to:

* Enter game information
* Predict Global Sales instantly
* Interact with the trained machine learning model

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Joblib
* Streamlit

---

## 📂 Project Structure

VideoGame/

├── app.py

├── vgsales_model.pkl

├── requirements.txt

└── README.md

---

## ▶️ Run Locally

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py

---

## 👨‍💻 Author

Farooq Khan

Aspiring Machine Learning Engineer




