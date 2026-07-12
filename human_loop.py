import streamlit as st


def human_decision():


    decision = st.radio(

        "Review AI Recommendation",

        [
            "Approve",
            "Reject",
            "Modify"
        ]

    )


    if st.button(
        "Submit Final Decision"
    ):

        st.success(
            f"Human Decision Recorded: {decision}"
        )


    return decision