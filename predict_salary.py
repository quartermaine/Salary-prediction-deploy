import streamlit as st
from pycaret.regression import *
import pandas as pd



def show_predict_page():
    st.title("Software Developer Salary Prediction")

    st.write("""### We need some information to predict the salary""")

    countries = (
        "United States",
        "India",
        "United Kingdom",
        "Germany",
        "Canada",
        "Brazil",
        "France",
        "Spain",
        "Australia",
        "Netherlands",
        "Poland",
        "Italy",
        "Russian Federation",
        "Sweden",
    )

    education = (
        "Less than a Bachelors",
        "Bachelor’s degree",
        "Master’s degree",
        "Post grad",
    )

    professional = (
        'proffesional',
        'non professional'
    )



    country = st.selectbox("Country", countries)
    education = st.selectbox("Education Level", education)
    proffessional = st.selectbox('Proffesional Level', professional)

    expericence = st.slider("Years of Experience", 0, 50, 3)

    ok = st.button("Calculate Salary")

    model = load_model('Final_Model')

    features ={'Country': country, 'EdLevel': education ,
           'YearsCodePro': expericence, 'MainBranch': proffessional}
 

    features_df  = pd.DataFrame([features])

    if ok:
        salary = predict_model(model, data=features_df)

        st.subheader(f"The estimated salary is ${salary['Label'][0]:.2f}")

show_predict_page()
