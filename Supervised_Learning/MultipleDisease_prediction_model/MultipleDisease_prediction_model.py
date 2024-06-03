# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 08:26:03 2024

@author: acer
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
 
 #loading the saved model
 
diabetes_model=pickle.load(open('C:/Users/acer/Desktop/MultipleDisease_prediction_model/saved_model/diabetes_model.sav','rb'))
 
parkinsons_model=pickle.load(open('C:/Users/acer/Desktop/MultipleDisease_prediction_model/saved_model/parkinsons_model.sav','rb'))
 
heart_disease_model=pickle.load(open('C:/Users/acer/Desktop/MultipleDisease_prediction_model/saved_model/Heart_Disease_Prediction_model.sav ','rb'))
 
 #sidebar for navigator
 
with  st.sidebar:
    selected=option_menu('Multiple Disease Prediction System',['Diabetes Prediction','Heart Disease Prediction','Parkinson Prediction'],
                         icons=['activity','heart-fill','person'],
                         default_index = 0)
    
    
#diabetes Prediction page

if(selected=='Diabetes Prediction'):
    
    #page title
    st.title('Diabetes Prediction using ML')
    
    #getting the input data from the user
    
    #columns from input field
    
    col1,col2,col3=st.columns(3)
    
    with col1:
        Pregnancies=st.text_input('Number of  Pregnancies ')
    with col2:
        Glucose=st.text_input('Glucose Level')
    with col3:
        BloodPressure=st.text_input('BloodPressure value')
    with col1:
        SkinThickness=st.text_input('SkinThickness value')
    with col2:
        Insulin=st.text_input('Insulin leve  l')
    with col3:
        BMI=st.text_input('BMIs value')
    with col1:
        DiabetesPedigreeFunction=st.text_input('DiabetesPedigreeFunction value')
    with col2:
        Age=st.text_input('Age of the Person ')
          
    
    
    #code for Prediction
    diab_diagnosis=''
    
    #creating a button for prediction
    if st.button('Diabetes Test Result'):
        
        diab_prediction=diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
    
        if(diab_prediction[0]==1):
            diab_diagnosis='The person is Diabetic'
        else:
            diab_diagnosis='The person is not Diabetic'
    st.success(diab_diagnosis)


if(selected=='Heart Disease Prediction'):
    #page title
    st.title('Heart Disease Prediction using ML')
    #getting the input data from the user
    
    #columns from input field
    
    col1,col2,col3=st.columns(3)
    
    
    with col1:
        age=st.text_input('Age of the Person ')
    with col2:
        sex=st.text_input('sex')
    with col3:
        cp=st.text_input('cp value')
    with col1:
        trestbps=st.text_input('trestbps value')
    with col2:
        chol=st.text_input('chol value')
    with col3:
        fbs=st.text_input('fbs value')
    with col1:
        restecg=st.text_input('restecg value')
    with col2:
       thalach=st.text_input('thalach value')
    with col3:
        exang=st.text_input('exang value ')
    with col1:
        oldpeak=st.text_input('oldpeak value')
    with col2:
        slope=st.text_input('slope value')
    with col3:
        ca=st.text_input('ca value')
    with col1:
        thal=st.text_input('thal value')
          
    
    
    #code for Prediction
    heart_diagnosis=''
    
    #creating a button for prediction
    if st.button('Heart Disease Test Result'):
               
        heart_prediction=heart_disease_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
    
        if(heart_prediction[0]==1):
            heart_diagnosis='The person is Heart Disease'
        else:
            heart_diagnosis='The person is not having Heart Disease'
    st.success(heart_diagnosis)
    
if(selected=='Parkinson Prediction'):
    #page title
    st.title('Parkinson Prediction using ML')
    
    #columns from input field
    
    col1,col2,col3=st.columns(3)
    
    
    with col1:
        MDVP_Fo_Hz = st.text_input('MDVP:Fo(Hz)')
    with col2:
        MDVP_RAP = st.text_input('MDVP:RAP')
    with col3:
        MDVP_Fhi_Hz = st.text_input('MDVP:Fhi(Hz)')
    
    with col1:
        Jitter_DDP = st.text_input('Jitter:DDP')
    with col2:
        Shimmer_DDA = st.text_input('Shimmer:DDA')
    with col3:
        MDVP_Flo_Hz = st.text_input('MDVP:Flo(Hz)')
    
    with col1:
        D2 = st.text_input('D2')
    with col2:
        MDVP_Jitter_Percent = st.text_input('MDVP:Jitter(%)')
    with col3:
        MDVP_Shimmer = st.text_input('MDVP:Shimmer')
    
    with col1:
        Shimmer_APQ3 = st.text_input('Shimmer:APQ3')
    with col2:
        MDVP_Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    with col3:
        MDVP_Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    
    with col1:
        NHR = st.text_input('NHR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    
    with col1:
        MDVP_APQ = st.text_input('MDVP:APQ')
    with col2:
        spread1 = st.text_input('spread1')
    with col3:
        MDVP_PPQ = st.text_input('MDVP:PPQ')
    
    with col1:
        Shimmer_APQ5 = st.text_input('Shimmer:APQ5')
    with col2:
        HNR = st.text_input('HNR')
    with col3:
        spread2 = st.text_input('spread2')
    
    with col1:
        PPE = st.text_input('PPE')
             
        
    
        #code for Prediction
        parkinsons_diagnosis=''
        
        #creating a button for prediction
        if st.button('Parkinsons Disease Test Result'):
                      
                           
            parkinsons_prediction = parkinsons_model.predict([[MDVP_Fo_Hz, MDVP_Fhi_Hz, MDVP_Flo_Hz, MDVP_Jitter_Percent, MDVP_Jitter_Abs, MDVP_RAP, MDVP_PPQ, Jitter_DDP, MDVP_Shimmer, MDVP_Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])


    
            if(parkinsons_prediction[0]==1):
                heart_diagnosis='The person is Parkinsons Disease'
            else:
                heart_diagnosis='The person is not having Parkinsons Disease'
        st.success(parkinsons_diagnosis)
    
    

 