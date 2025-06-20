# 💻 Laptop Price Predictor

A machine learning-powered web app built using **Streamlit** that predicts the price of a laptop based on key specifications such as brand, processor, RAM, display, storage, and more. The project includes model training, feature engineering, and deployment with an intuitive UI for real-time prediction.

## 🚀 Project Overview

Laptop prices vary significantly depending on several factors like brand, RAM, CPU, storage type, and display features. This project uses a **regression-based machine learning model** to estimate laptop prices accurately based on such specifications.

This project showcases the **end-to-end machine learning pipeline**:

- 📊 Data preprocessing and feature engineering  
- 🧠 Model training and serialization  
- 🌐 Building an interactive frontend with Streamlit  
- ☁️ Hosting and running the model locally or on the cloud  

---

### 📊 Model Performance Metrics

| Metric                     | Value               |
|----------------------------|---------------------|
| 🔹 R² Score                | 0.91 (91%)          |
| 🔸 Mean Absolute Error (MAE) | ~3.5 kcal          |
| ⚙️ Model Used              | RandomForestRegressor |

### 📁 Project Structure

| File/Folder                | Description                                |
|----------------------------|--------------------------------------------|
| `laptop_price.csv`         | Cleaned dataset used for training          |
| `laptop_price.ipynb`       | Jupyter Notebook for data processing and model training |
| `model_columns.pkl`        | Pickled list of columns used during training |
| `laptop_price_model.pkl`   | Trained machine learning model             |
| `streamlit_app.py`         | Streamlit web application code             |

## 🧠 ML Model Details

- **Algorithm Used**: Linear Regression  
  *(Can be upgraded to Random Forest, XGBoost, etc.)*
- **Target Variable**: `Price` (in INR)

### 📌 Features Used

- Brand
- CPU Brand
- Operating System
- RAM (GB)
- Weight (kg)
- Display PPI (Pixels Per Inch)
- SSD Storage (GB)
- HDD Storage (GB)

### 🔍 Data Encoding & Evaluation

- **Encoding**: One-hot encoding for categorical variables  
- **Evaluation Metric**: Root Mean Squared Error (RMSE)

## 🛠️ Technologies Used

- 🐍 Python 3.10+
- 🌐 Streamlit – for frontend UI
- 📦 scikit-learn – model building
- 📊 pandas, numpy – data processing
- 📁 pickle – for saving/loading the model and column structure
