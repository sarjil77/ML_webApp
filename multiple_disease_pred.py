# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 22:58:31 2024

@author: asfaq
"""

import pickle 
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models
# diabetes model

diabetes_model = pickle.load(open('trained_diabetes_pred.sav','rb'))

# heart model

heart_model = pickle.load(open('trained_heart_disease_.sav','rb'))


# creating the sidebar for navigation

with st.sidebar:
    
    selected = option_menu('Multiple disease prediction system using ML',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction'],
                           
                           icons = ['activity','heart'],
                           
                            default_index = 0)
    
# Diabetes Prediction Page

if (selected == 'Diabetes Prediction'):
    
    # page title 
    st.title('Diabetes Prediction Using ML')
    
    #example of input data 
    st.subheader("Example of Diabetes Input Data:")
    st.write("For person having Diabetes")
    st.write("Pregnancies: 6, Glucose: 148, BloodPressure: 72, SkinThickness: 35, Insulin: 0, BMI: 33.6, DiabetesPedigreeFunction: 0.627, Age: 50")
    
    # getting the input data from the user
    # colunms for input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of pregnancies')
    
    with col2:
        Glucose = st.text_input('Glucose level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
        
    with col2:
        Insulin = st.text_input('Insulin level')
    
    with col3:
        BMI = st.text_input('BMI')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction')
    
    with col2:
        Age = st.text_input('Age of the person')
    
    
    # code for prediction
    diab_diagnosis = ''
    
    # creating a button for prediction
    if st.button('Diabetes Test Result'):
        diab_diagnosis = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
        if (diab_diagnosis[0] == 1):
            diab_diagnosis = 'The person have Diabetes'
            
        else:
            diab_diagnosis = 'The person does not have Diabetes'
    
    st.success(diab_diagnosis)
    
    
# Heart Disease page
if (selected == 'Heart Disease Prediction'):
    # Display default example data as a reference for users
    st.subheader("Example Input Data:")
    st.write("For person does not have Heart Disease")
    st.write("Age: 52, Sex: 1, CP: 0, Trestbps: 125, Chol: 212, Fbs: 0, Restecg: 1, Thalach: 168, Exang: 0, Oldpeak: 1, Slope: 2, CA: 2, Thal: 3")
    st.write("For person having Heart Disease")
    st.write("Age: 71, Sex: 0, CP: 0, Trestbps: 112, Chol: 149, Fbs: 0, Restecg: 1, Thalach: 125, Exang: 0, Oldpeak: 1.6, Slope: 1, CA: 0, Thal: 2")
    # page title 
    st.title('Heart Disease Prediction Using ML')

    # getting the input data from the user
    # colunms for input fields
    col1, col2, col3 = st.columns(3)
    
    
    with col1:
        age = st.text_input('Age of the person')
        
    with col2:
        sex = st.text_input('Enter your Gender')
     
    with col3:
        cp = st.text_input('Chest pain type (0-3)')
         
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
         
    with col2:
        chol = st.text_input('serum cholestoral in mg/dl')
    
    with col3:
        fbs = st.text_input('fasting blood sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('resting electrocardiographic results (values 0,1,2)')
          
    with col2:
        thalach = st.text_input('maximum heart rate achieved')
     
    with col3:
        exang = st.text_input('exercise induced angina')   
    
    with col1:
        oldpeak = st.text_input('oldpeak = ST depression induced by exercise relative to rest')
          
    with col2:
        slope = st.text_input('the slope of the peak exercise ST segment')
    
    with col3:
        ca = st.text_input('number of major vessels (0-3) colored by flourosopy')                          
    
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')        
    
       
    # code for prediction
    
    heart_diagnosis = ''
    
    # button for prediction
    # Convert input values to appropriate data types
    if age.strip() and sex.strip() and cp.strip() and trestbps.strip() and chol.strip() and fbs.strip() and restecg.strip() and thalach.strip() and exang.strip() and oldpeak.strip() and slope.strip() and ca.strip() and thal.strip():
        age = float(age)
        sex = float(sex)
        cp = float(cp)
        trestbps = float(trestbps)
        chol = float(chol)
        fbs = float(fbs)
        restecg = float(restecg)
        thalach = float(thalach)
        exang = float(exang)
        oldpeak = float(oldpeak)
        slope = float(slope)
        ca = float(ca)
        thal = float(thal)
    else:
        st.error("Please fill in all the input fields.")

# Now pass the converted values to the model for prediction
    if st.button('Heart Disease result'):
        heart_pred = heart_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
   
        
        if (heart_pred[0] == 1):
            
            heart_diagnosis = 'The Person has Heart Disease'
        else:
            heart_diagnosis = 'The Person does not have Heart Disease'
    
    st.success(heart_diagnosis)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
