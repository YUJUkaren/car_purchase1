import streamlit as st
import pickle
import pandas as pd

# 設定標題
st.title('Car Purchase Prediction')
st.write('This web app predicts the **Car Price**')

# 讀取模型
model = pickle.load(open('model_car.pkl', 'rb'))

# 用戶輸入
gender = st.selectbox('Select Gender', ['Male', 'Female'])
age = st.number_input('Enter Age', min_value=18, max_value=100, step=1)
annual_salary = st.number_input('Enter Annual Salary', min_value=0, step=1000)

# One-Hot Encoding for Gender
gender_female = 1 if gender == "Female" else 0
gender_male = 1 if gender == "Male" else 0

# 建立 DataFrame，確保欄位與模型一致
user_data = pd.DataFrame({
    'Age': [age],
    'AnnualSalary': [annual_salary],
    'Gender_Female': [gender_female],
    'Gender_Male': [gender_male]
})

# 預測按鈕
if st.button('Predict'):
    prediction = model.predict(user_data)
    st.write(f'The predicted car price is: ${prediction[0]:,.2f}')
