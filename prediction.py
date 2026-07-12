import streamlit as st
import joblib
import pandas as pd
from tensorflow.keras.models import load_model


@st.cache_resource
def load_files():

    model = load_model(
        "best_model.keras"
    )

    preprocessor = joblib.load(
        "preprocessor.pkl"
    )

    return model, preprocessor



def predict_loan(user_data):

    model, preprocessor = load_files()


    input_df = pd.DataFrame(
        [user_data]
    )


    processed = preprocessor.transform(
        input_df
    )


    prediction = model.predict(
        processed,
        verbose=0
    )[0][0]


    if prediction >= 0.5:

        result = "Loan Approved"
        confidence = prediction * 100

    else:

        result = "Loan Rejected"
        confidence = (1-prediction)*100


    return (
        result,
        confidence,
        processed,
        preprocessor
    )