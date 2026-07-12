import shap
import joblib
import numpy as np
import streamlit as st



@st.cache_resource
def load_explainer():

    model = joblib.load(
        "background_data.pkl"
    )



def create_explainer(model, background):

    return shap.KernelExplainer(
        model.predict,
        background
    )



def shap_explanation(
        explainer,
        processed,
        preprocessor):


    shap_values = explainer.shap_values(
        processed
    )


    feature_names = (
        preprocessor
        .get_feature_names_out()
    )


    importance = np.abs(
        shap_values[0]
    ).flatten()


    top_idx = np.argsort(
        importance
    )[::-1][:5]


    factors=[]


    for i in top_idx:

        factors.append(
            f"{feature_names[i]} : {importance[i]:.4f}"
        )


    return factors



def get_reasons(user_data):

    reasons=[]


    if user_data["Credit_History"]==0:
        reasons.append(
            "Weak Credit History"
        )


    if user_data["ApplicantIncome"] <3000:
        reasons.append(
            "Low Applicant Income"
        )


    if user_data["LoanAmount"]>200:
        reasons.append(
            "High Loan Amount"
        )


    if user_data["CoapplicantIncome"]==0:
        reasons.append(
            "No Co Applicant Income"
        )


    return reasons