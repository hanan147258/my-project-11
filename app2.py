# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

loaded_model=pickle.load(open('C:/Users/User/Downloads/SVC_i_model (2).sav','rb'))

def diabetes (input_data):
    
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    
    return(prediction)
    
    if (prediction[0] == 0):
      return('The person is not diabetic')
    else:
      return('The person is diabetic')
def main():



    st.title('Diabetes Prediction Web App')

    Pregnancies = st.text_input('Enter the number of pregnancies: ')
    Glucose = st.text_input('Enter the glucose level: ')
    BloodPressure = st.text_input('Enter the blood pressure: ')
    SkinThickness = st.text_input('Enter the skin thickness: ')
    Insulin = st.text_input('Enter the insulin level: ')
    BMI = st.text_input('Enter the BMI: ')
    DiabetesPedigreeFunction = st.text_input('Enter the diabetes pedigree function: ')
    Age = st.text_input('Enter the age: ')



    dignosis = ''
    # creating a button for perdiction
    if st.button('Diabetes test Result'):
        dignosis = diabetes([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])


    st.success(dignosis)

if __name__ =='__main__':
    main()