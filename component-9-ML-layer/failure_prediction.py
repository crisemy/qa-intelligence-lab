import pandas as pd
from sklearn.externals import joblib

def predict_failures(model_path, features_path):
    """
    Predicts failures using a trained model and feature data.

    Args:
        model_path (str): Path to the trained model file.
        features_path (str): Path to the feature data CSV file.

    Returns:
        pd.DataFrame: DataFrame with predictions.
    """
    # Load model
    model = joblib.load(model_path)

    # Load features
    features = pd.read_csv(features_path)

    # Predict failures
    predictions = model.predict(features)
    features['predicted_failure'] = predictions

    return features

if __name__ == "__main__":
    # Example usage
    model_file_path = "trained_model.pkl"
    features_file_path = "../component-7-load-testing/config/results/features.csv"
    predictions = predict_failures(model_file_path, features_file_path)
    print(predictions.head())