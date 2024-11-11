import streamlit as st
import numpy as np
import pickle

model = pickle.load(open('siddheshproject1.pkl','rb'))

# let's create web app
st.title("House Cost Prediction ")
bedrooms = st.text_input('Enter Bedrooms')
bathrooms = st.text_input("Enter Bathrooms")
sqft_living = st.text_input("Enter sqft_living")
sqft_lot = st.text_input("Enter sqft_lot")
floors = st.text_input("Enter floors")
waterfront = st.text_input("Enter waterfront")
view = st.text_input("Enter view")
condition = st.text_input("Enter condition")
grade = st.text_input("Enter grade")
sqft_above = st.text_input("Enter sqft_above")
sqft_basement = st.text_input("Enter sqft_basement")
yr_built = st.text_input("Enter yr_built")
yr_renovated = st.text_input("Enter yr_renovated")
zipcode = st.text_input("Enter zipcode")
lat= st.text_input("Enter lat")
long = st.text_input("Enter long")
sqft_living15 = st.text_input("Enter sqft_living15")
sqft_lot15 = st.text_input("Enter sqft_lot15")

if st.button("predict"):
    features = np.array([[bedrooms,bathrooms,sqft_living,sqft_lot,floors,waterfront,view,condition,grade,sqft_above,sqft_basement,yr_built,yr_renovated,zipcode,lat,long,sqft_living15,sqft_lot15]], dtype=np.float64)
    results = model.predict(features).reshape(1,-1)
    st.write("Predicted sale::::", results[0])