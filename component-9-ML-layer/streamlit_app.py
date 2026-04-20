import streamlit as st
import pandas as pd
from sklearn.metrics import classification_report
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    """Load dataset from a CSV file."""
    return pd.read_csv(file_path)

def display_classification_report(report):
    """Display classification report in Streamlit."""
    st.text("Classification Report")
    st.text(report)

def plot_classification_report(report_dict):
    """Generate bar charts for precision, recall, and F1-score."""
    metrics = ['precision', 'recall', 'f1-score']
    classes = [key for key in report_dict.keys() if key.isdigit()]

    # Prepare data for plotting
    data = []
    for metric in metrics:
        for cls in classes:
            data.append({'Class': cls, 'Metric': metric, 'Value': report_dict[cls][metric]})

    df = pd.DataFrame(data)

    # Plot
    sns.barplot(data=df, x='Class', y='Value', hue='Metric')
    plt.title('Classification Report Metrics')
    st.pyplot(plt)

def display_explanations():
    """Display explanations for classification metrics."""
    st.subheader("Metric Explanations")
    st.markdown(
        """
        - **Accuracy**: The proportion of correctly classified instances out of the total instances.
        - **Precision**: The proportion of true positives out of all predicted positives.
        - **Recall**: The proportion of true positives out of all actual positives.
        - **F1-Score**: The harmonic mean of precision and recall.
        - **Support**: The number of actual occurrences of each class in the dataset.
        - **Macro Avg**: Average of the metric across all classes, treating all classes equally.
        - **Weighted Avg**: Average of the metric across all classes, weighted by the number of instances in each class.
        """
    )

def main():
    st.title("ML Layer Results Viewer")

    # File upload
    dataset_file = st.file_uploader("Upload Aggregated Dataset", type=["csv"])
    model_file = st.file_uploader("Upload Trained Model", type=["pkl"])

    if dataset_file and model_file:
        # Load dataset
        data = load_data(dataset_file)

        # Load feature names used during training
        feature_names_file = "feature_names.txt"
        with open(feature_names_file, "r") as f:
            feature_names = f.read().splitlines()

        # Filter dataset to match training features
        X = data[feature_names]
        y = data['failure']

        # Load model
        import joblib
        model = joblib.load(model_file)

        # Predict and evaluate
        y_pred = model.predict(X)
        # Generate classification report as a dictionary
        report_dict = classification_report(y, y_pred, output_dict=True)

        # Display charts
        plot_classification_report(report_dict)

        # Display explanations
        display_explanations()

if __name__ == "__main__":
    main()