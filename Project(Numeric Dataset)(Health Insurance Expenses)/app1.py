import joblib
import streamlit as st
import pandas as pd
Rf_Model=joblib.load('linear_regression_model.pkl')
st.title('Prediction Of Health Insurance Expenses Charges According to smoking, age & BMI')
Smoking=st.selectbox('Please Select Smoking Status',options=['Non Smoker','Smoker'])
Smoking_Num=1 if Smoking=='Smoker' else 0
Age=st.number_input('Please Enter Your Age')
BMI=st.number_input('Please Enter Your BMI')
Button=st.button('Predict Charges')
if Button:
    input_data=pd.DataFrame({'smoker':[Smoking_Num],'age':[Age],'bmi':[BMI]})
    prediction=Rf_Model.predict(input_data)
    st.success(f'Predicted Health Insurance Expenses Charges is: {prediction[0]:.2f}')


