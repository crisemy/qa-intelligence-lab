import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

def train_baseline_model(dataset_path):
    """
    Trains a baseline classification model.

    Args:
        dataset_path (str): Path to the aggregated dataset CSV file.

    Returns:
        RandomForestClassifier: Trained model.
    """
    # Load dataset
    data = pd.read_csv(dataset_path)

    # Select only numeric columns for features
    X = data.select_dtypes(include=['number']).drop(columns=['failure'])  # Features

    # Debugging: Print the columns being used for training
    print(f"Columns used for training: {X.columns.tolist()}")

    # Target
    y = data['failure']  # Target

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Evaluate model
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))

    return model

if __name__ == "__main__":
    # Example usage
    dataset_path = "../component-7-load-testing/config/results/aggregated_dataset.csv"
    model = train_baseline_model(dataset_path)