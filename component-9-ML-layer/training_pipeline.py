import os
from feature_engineering import extract_features_from_k6_metrics
from dataset_aggregation import aggregate_datasets
from baseline_model import train_baseline_model

def automate_training_pipeline(metrics_folder, aggregated_dataset_path, model_output_path):
    """
    Automates the ML training pipeline.

    Args:
        metrics_folder (str): Path to the folder containing k6 metrics files.
        aggregated_dataset_path (str): Path to save the aggregated dataset.
        model_output_path (str): Path to save the trained model.
    """
    # Debugging: Check if the metrics folder exists
    if not os.path.exists(metrics_folder):
        print(f"Error: Metrics folder does not exist: {metrics_folder}")
        return
    print(f"Using metrics folder: {metrics_folder}")

    # Step 1: Aggregate datasets
    aggregated_data = aggregate_datasets(metrics_folder)
    aggregated_data.to_csv(aggregated_dataset_path, index=False)

    # Debugging: Check if the aggregated dataset is valid
    if aggregated_data.empty:
        print("Error: Aggregated dataset is empty. Check the input files.")
        return
    print("Aggregated dataset preview:")
    print(aggregated_data.head())

    # Step 2: Train baseline model
    model = train_baseline_model(aggregated_dataset_path)

    # Step 3: Save trained model
    import joblib
    joblib.dump(model, model_output_path)

    # Save feature names used during training
    feature_names_file = "feature_names.txt"
    with open(feature_names_file, "w") as f:
        f.write("\n".join(model.feature_names_in_))
    print(f"Feature names saved to {feature_names_file}")

    print(f"Pipeline completed. Model saved to {model_output_path}")

if __name__ == "__main__":
    # Example usage
    metrics_folder_path = "../component-7-load-testing/results/"
    aggregated_dataset_file = "aggregated_dataset.csv"
    model_file = "trained_model.pkl"

    automate_training_pipeline(metrics_folder_path, aggregated_dataset_file, model_file)