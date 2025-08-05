import streamlit as st
import pandas as pd

def review_ui(df):
    for idx, row in df.head(5).iterrows():
        st.subheader(f"Case #{idx}")
        st.json(row.to_dict())
        decision = st.radio(f"Approve prediction for case #{idx}?", ["Approve", "Reject"], key=str(idx))
        if st.button(f"Submit Review #{idx}", key="submit_"+str(idx)):
            st.success(f"You marked this case as {decision}")