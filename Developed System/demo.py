# create a streamlit app that will take input for the model in te hackathon.ipynb file
# and display the output

import streamlit as st
import pandas as pd
import numpy as np
import pickle

#load the model from the pickle file
model = pickle.load(open('droped_model.pkl','rb'))


# create a function that will take the inputs from the user
def predict_default(Type,age,gender):
    
    # Pre-processing user input    
    if Type == "New tool":
        Type = 0
    else:
        Type = 1

    if age =='under 1':
        age = 0
    elif age == 'under 10':
            age  = 1
    elif age == 'under 15':
            age  = 2
    elif age == 'over 15':
            age  = 3
    elif age == 'under 20':
            age  = 4
    elif age == 'under 20':
            age  = 5
    elif age == 'over 25':
            age  = 6
    else:
        age = 8

    if gender == "male":
        gender= 0
    elif  gender == 'female':
        gender = 1
    else:
        gender = 2

 
    # Making predictions 
    prediction = model.predict( 
        [[Type,age,gender]])

    # set prediction whole number integer
    prediction = int(prediction)

    return prediction

# main function
def main():
    st.title('''NACSCOP Tool Recommendation :hospital:''')
    Type= st.selectbox("choose the appropriae type",("New tool","Old tool"))
    age = st.selectbox('age',('under 1','under 10','over 15','under 15','under 20','under 25','over 25'))
    if age == 'under 1'or age == 'under 10' or age == 'under 15' :
       gender = st.selectbox('Select the Gender',('undefined',))
    else:
         gender = st.selectbox('Select the Gender',('male','female','undefined'))
    button = st.button('classify')
    if button:
        prediction = predict_default(Type,age,gender)
        st.success('The tool recommends {}'.format(prediction))

if __name__ == '__main__':
    main()