import streamlit as st
import pickle
import numpy as np

# Load the model and columns
model = pickle.load(open('laptop_price_model.pkl', 'rb'))
model_columns = pickle.load(open('model_columns.pkl', 'rb'))

st.title("💻 Laptop Price Predictor")

# Realistic options extracted from your dataset
brand_options = ["--Select Brand--"] + [
    'Acer', 'Apple', 'Asus', 'Chuwi', 'Dell', 'Fujitsu', 'Google', 'HP', 'Huawei',
    'LG', 'Lenovo', 'MSI', 'Mediacom', 'Microsoft', 'Razer', 'Samsung', 'Toshiba', 'Vero', 'Xiaomi'
]

cpu_options = ["--Select CPU--"] + ['AMD', 'Intel', 'Samsung']

os_options = ["--Select OS--"] + [
    'macOS', 'Windows 10', 'Linux']

# Sidebar inputs
brand = st.selectbox('Brand', brand_options)
cpu_brand = st.selectbox('CPU Brand', cpu_options)
os = st.selectbox('Operating System', os_options)

ram = st.number_input('RAM (GB)', min_value=2, max_value=64, value=8)
weight = st.number_input('Weight (kg)', min_value=0.8, max_value=5.0, value=2.5)
ppi = st.number_input('Pixels Per Inch (PPI)', min_value=50, max_value=600, value=150)
ssd = st.number_input('SSD Storage (GB)', min_value=0, max_value=2000, value=256)
hdd = st.number_input('HDD Storage (GB)', min_value=0, max_value=2000, value=0)

# Prediction logic
if st.button('Predict Price'):
    if brand.startswith('--') or cpu_brand.startswith('--') or os.startswith('--'):
        st.error("Please select all required options.")
    else:
        input_data = np.zeros(len(model_columns))

        # Construct input feature dictionary
        input_dict = {
            'Brand_' + brand: 1,
            'Cpu_brand_' + cpu_brand: 1,
            'OpSys_' + os: 1,
            'Ram': ram,
            'Weight': weight,
            'PPI': ppi,
            'SSD': ssd,
            'HDD': hdd
        }

        for i, col in enumerate(model_columns):
            if col in input_dict:
                input_data[i] = input_dict[col]

        prediction = model.predict([input_data])[0]
        st.success(f"💰 Estimated Laptop Price: ₹{round(prediction):,}")
