import streamlit as st
import numpy as np
import pandas as pd
import sklearn
import pickle
pickle_in = open("strokepredictor.pkl", "rb")
dtree = pickle.load(pickle_in)
def welcome():
    return "Welcome All"
def predict_note_authentication(age, bmi, avg_glucose):
    prediction = dtree.predict([[age, bmi, avg_glucose]])
    print(prediction)
    return prediction

def main():
    st.title("Stroke Prediction System")
    st.title("Predict the possibility of stroke in you by entering the below details")
    html_temp = """
    <div style="background-color:lightgreen;padding:10px>
    <h2 style ="color:white; text-align:center;">Stroke Predictor</h2>
    </div>
    """

    st.markdown(html_temp, unsafe_allow_html=True)
    st.image('https://images.pexels.com/photos/139398/thermometer-headache-pain-pills-139398.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1')
    age = st.text_input("Age" , "")
    bmi = st.text_input("BMI", "")
    avg_glucose = st.text_input("Avg_Glucose Level", "")
    st.text(
        "By entering the details of a patient, this system can predict whether a person\n can have stroke of not. 0 corresponds to no chance of stroke and \n1 corresponds to chance of stroke")

    result = ""
    chance = ""
    if st.button("Predict"):
        result = predict_note_authentication(age, bmi, avg_glucose)
        if result == 1:
            chance = "high"
        else:
            chance = "low"
    st.success("the probability of stroke is "+ chance)
    if st.button("Credits"):

        st.text("Created by Shreeya")


if __name__ == '__main__':
    main()




