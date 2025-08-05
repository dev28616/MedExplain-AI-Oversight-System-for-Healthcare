import matplotlib.pyplot as plt
import seaborn as sns

def run_bias_audit(df):
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.countplot(x="Gender", hue="Outcome", data=df, ax=ax)
    ax.set_title("Outcome Distribution by Gender")
    return fig