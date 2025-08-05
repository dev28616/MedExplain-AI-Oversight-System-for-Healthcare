import streamlit as st
from modules.explainability import explain_prediction
from modules.bias_audit import run_bias_audit
from modules.human_review import review_ui
from modules.logger import log_event, initialize_logger
from utils.data_loader import get_sample_data


initialize_logger()


st.set_page_config(page_title="MedExplain", layout="wide")
st.title("🛡️ MedExplain - AI Oversight System")
st.markdown("""
MedExplain adds **explainability, fairness, auditability**, and **human validation** to healthcare AI workflows.
""")

st.sidebar.title("🔍 Modules")
choice = st.sidebar.radio("Select Module", ["Explainability", "Bias Audit", "Human Review"])

data = get_sample_data()

if choice == "Explainability":
    st.header("🔎 Model Explainability with SHAP")
    instance = st.selectbox("Select patient index", data.index)
    shap_fig = explain_prediction(data.loc[instance])
    st.pyplot(shap_fig)
    log_event("explainability", str(instance))

elif choice == "Bias Audit":
    st.header("⚖️ Bias & Fairness Audit")
    audit_fig = run_bias_audit(data)
    st.pyplot(audit_fig)
    log_event("bias_audit", "full_dataset")

elif choice == "Human Review":
    st.header("👨‍⚕️ Human-in-the-loop Review System")
    review_ui(data)
    log_event("human_review", "triggered")