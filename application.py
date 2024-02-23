# Import necessary libraries
import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the trained model
model_filename ='./prod.pkl'
with open(model_filename, 'rb') as file:
    model = pickle.load(file)

# Streamlit App
st.title('Diabetes Prediction App')

# Sidebar with user input
st.sidebar.header('User Input Features')

# Function to get user input
try:
    def get_user_input():
        
        pregnancies = st.sidebar.slider('Pregnancies', 0, 17, 3)
        glucose = st.sidebar.slider('Glucose Level', 44, 199, 117)
        blood_pressure = st.sidebar.slider('Blood Pressure', 24, 122, 72)
        skin_thickness = st.sidebar.slider('Skin Thickness', 7, 99, 23)
        insulin = st.sidebar.slider('Insulin', 14, 846, 30)
        bmi = st.sidebar.slider('BMI', 18.0, 67.1, 32.0)
        DiabetesPedigreeFunction = st.sidebar.slider('DiabetesPedigreeFunction', 0.078000,1.02, 2.42)
        age = st.sidebar.slider('Age', 21, 81, 29)

        # Store user input in a dictionary
        user_data = {
            'Pregnancies': pregnancies,
            'Glucose': glucose,
            'BloodPressure': blood_pressure,
            'SkinThickness': skin_thickness,
            'Insulin': insulin,
            'BMI': bmi,
            'DiabetesPedigreeFunction':DiabetesPedigreeFunction,
            'Age': age
        }
        return user_data
        # Get user input
    user_input = get_user_input()

    # Convert user input to dataframe
    input_df = pd.DataFrame([user_input])

    # Predict the outcome
    prediction=None

    # Display the prediction
    

    # Display the user input data
    st.subheader('User Input Data')
    st.write(user_input)
    if st.button('predict'):
        st.subheader('Prediction')
        if(prediction==1):
            st.warning('The person is likely to have diabetes.')
        else:
            st.success("The person Does not have diabetes")
except:
    st.warning("Internal Servor Error")


    
