import numpy as np
import pickle
import streamlit as st

load_model = pickle.load(open('water_model.sav','rb'))


def water_prediction(input_values):

    # Convert input values to float
    input_values = [float(val) if val.strip() != '' else 0.0 for val in input_values]

    input_data_as_numpy_array = np.asarray(input_values)

    # Reshape the array
    input_data_reshape = input_data_as_numpy_array.reshape(1, -1)

    # Now you can make predictions
    prediction = load_model.predict(input_data_reshape)
    print(prediction)

    if prediction[0] == 1:
        return "The water is drinkable"
    else:
        return "The water is not drinkable"

def main():

    #Title of the web page
    st.title("Water Prediction Web App")

    #getting the input data from the user
    # ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity
    ph = st.text_input("Enter the Ph value")
    Hardness = st.text_input("Enter the Hardness value")
    Solids = st.text_input("Enter the Solids value")
    Chloramines = st.text_input("Enter the Chloramines value")
    Sulfate = st.text_input("Enter the Sulfate value")
    Conductivity = st.text_input("Enter the Conductivity value")
    Organic_carbon = st.text_input("Enter the Organic Carbon value")
    Trihalomethanes = st.text_input("Enter the Trihalomethanes value")
    Turbidity = st.text_input("Enter the Turbidity value")

    #code for prediction
    water = ''
    
    #creating a buttom for prediction
    if st.button("Water Quality Result"):
        water = water_prediction([ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity])

    st.success(water)

if __name__ == '__main__':
    main()