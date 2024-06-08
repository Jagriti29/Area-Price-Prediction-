# myapp.py
import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('area_price_model.pkl', 'rb') as f:
    model = pickle.load(f)

def myf1():
    st.title("Area Price Prediction")
    #user input area
    area=st.number_input("Enter the area (in square feet)",min_value=0.0, step=0.1)
    #prediction button
    if st.button("Predict Price"):
        price=model.predict(np.array([[area]]))[0]
        st.write(f"The predicted price for an area of {area} sq ft is ${price:.2f}")

myf1()

    


     

    