import shap
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

_model = None
_explainer = None


def train_model():
    global _model, _explainer
    df = pd.read_csv("utils/sample_data.csv")

    # Encode all non-numeric columns
    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = LabelEncoder().fit_transform(df[col])

    X = df.drop("Outcome", axis=1)
    y = df["Outcome"]

    _model = RandomForestClassifier().fit(X, y)
    _explainer = shap.Explainer(_model, X)

train_model()

def explain_prediction(instance):
    import numpy as np

    df = pd.read_csv("utils/sample_data.csv")

    # Encode categorical columns
    encoders = {}
    for col in df.select_dtypes(include=["object"]).columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        encoders[col] = le

    X = df.drop("Outcome", axis=1)
    y = df["Outcome"]

    # Retrain model & explainer if needed
    global _model, _explainer
    _model = RandomForestClassifier().fit(X, y)
    _explainer = shap.Explainer(_model, X)

    # Encode instance
    for col, le in encoders.items():
        instance[col] = le.transform([instance[col]])[0]

    instance_df = pd.DataFrame([instance], columns=X.columns)

    shap_values = _explainer(instance_df)

    # ✅ Handle multi-output safely (e.g., shape (1, features, classes))
    if isinstance(shap_values.values, np.ndarray) and len(shap_values.values.shape) == 3:
        single_shap = shap_values[:, :, 1][0]  # Take class 1
        features = shap_values.data[0]
        base_value = shap_values.base_values[:, 1][0]
        shap_explanation = shap.Explanation(values=single_shap, base_values=base_value, data=features, feature_names=X.columns)
        fig = shap.plots.waterfall(shap_explanation, show=False)
    else:
        fig = shap.plots.waterfall(shap_values[0], show=False)

    return plt.gcf()



