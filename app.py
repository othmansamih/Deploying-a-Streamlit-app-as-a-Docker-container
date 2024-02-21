import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# set page configuration
st.set_page_config(page_title="Health assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# Getting the directory of the main.py file
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models
diabetes_model = pickle.load(open(f"{working_dir}/saved_models/diabetes_model.sav", "rb"))
heart_disease_model = pickle.load(open(f"{working_dir}/saved_models/heart_disease_model.sav", "rb"))
parkinsons_model = pickle.load(open(f"{working_dir}/saved_models/parkinsons_model.sav", "rb"))

# sidebar for navigation
with st.sidebar:
    selected = option_menu(menu_title="Multiple disease prediction system",
                           options=[
                               "Diabetes prediction",
                               "Heart disease prediction",
                               "Parkinson disease prediction"
                           ])

# diabetes prediction page
if selected == "Diabetes prediction":
    st.title("Diabetes Prediction using ML")
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input("Pregnancies")
    with col2:
        Glucose = st.text_input("Glucose")
    with col3:
        BloodPressure = st.text_input("BloodPressure")

    with col1:
        SkinThickness = st.text_input("SkinThickness")
    with col2:
        Insulin = st.text_input("Insulin")
    with col3:
        BMI = st.text_input("BMI")

    with col1:
        DiabetesPedigreeFunction = st.text_input("DiabetesPedigreeFunction")
    with col2:
        Age = st.text_input("Age")

    # code for prediction
    diabetes_diagnosis = ""

    if st.button("Diabetes test result"):
        input_data = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        input_data = [float(x) for x in input_data]
        result = diabetes_model.predict([input_data])
        if result[0] == 0:
            diabetes_diagnosis = "This person is not diabetic!"
        else:
            diabetes_diagnosis = "This person is diabetic!"

        st.success(diabetes_diagnosis)

# heart disease prediction page
if selected == "Heart disease prediction":
    st.title("Heart disease prediction using ML")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        age = st.text_input("age")
    with col2:
        sex = st.text_input("sex")
    with col3:
        cp = st.text_input("cp")
    with col4:
        trestbps = st.text_input("trestbps")

    with col1:
        chol = st.text_input("chol")
    with col2:
        fbs = st.text_input("fbs")
    with col3:
        restecg = st.text_input("restecg")
    with col4:
        thalach = st.text_input("thalach")

    with col1:
        exang = st.text_input("exang")
    with col2:
        oldpeak = st.text_input("oldpeak")
    with col3:
        slope = st.text_input("slope")
    with col4:
        ca = st.text_input("ca")

    with col1:
        thal = st.text_input("thal")

    # code for prediction
    heart_disease_diagnosis = ""

    if st.button("Heart disease test result"):
        input_data = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        input_data = [float(x) for x in input_data]
        result = heart_disease_model.predict([input_data])
        if result[0] == 0:
            heart_disease_diagnosis = "This person hasn't heart disease!"
        else:
            heart_disease_diagnosis = "This person has a heart disease!"

        st.success(heart_disease_diagnosis)

# parkinson disease prediction page
if selected == "Parkinson disease prediction":
    st.title("Parkinson disease Prediction using ML")
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input("MDVP:Fo(Hz)")
    with col2:
        fhi = st.text_input("MDVP:Fhi(Hz)")
    with col3:
        flo = st.text_input("MDVP:Flo(Hz)")
    with col4:
        jitter = st.text_input("MDVP:Jitter(%)")
    with col5:
        jitterabs = st.text_input("MDVP:Jitter(Abs)")

    with col1:
        rap = st.text_input("MDVP:RAP")
    with col2:
        ppq = st.text_input("MDVP:PPQ")
    with col3:
        ddp = st.text_input("Jitter:DDP")
    with col4:
        shimmer = st.text_input("MDVP:Shimmer")
    with col5:
        shimmerdb = st.text_input("MDVP:Shimmer(dB)")

    with col1:
        apq3 = st.text_input("Shimmer:APQ3")
    with col2:
        apq5 = st.text_input("Shimmer:APQ5")
    with col3:
        apq = st.text_input("MDVP:APQ")
    with col4:
        dda = st.text_input("Shimmer:DDA")
    with col5:
        nhr = st.text_input("NHR")

    with col1:
        hnr = st.text_input("HNR")
    with col2:
        rpde = st.text_input("RPDE")
    with col3:
        dfa = st.text_input("DFA")
    with col4:
        spread1 = st.text_input("spread1")
    with col5:
        spread2 = st.text_input("spread2")

    with col1:
        d2 = st.text_input("D2")
    with col2:
        ppe = st.text_input("PPE")


    # code for prediction
    parkinson_disease_diagnosis = ""

    if st.button("Parkinson test result"):
        input_data = [fo, fhi, flo, jitter, jitterabs, rap, ppq, ddp, shimmer, shimmerdb, apq3, apq5, apq, dda, nhr, hnr, rpde, dfa, spread1, spread2, d2, ppe]
        input_data = [float(x) for x in input_data]
        result = parkinsons_model.predict([input_data])
        if result[0] == 0:
            parkinson_disease_diagnosis = "This person hasn't parkinson!"
        else:
            parkinson_disease_diagnosis = "This person has parkison!"

        st.success(parkinson_disease_diagnosis)
