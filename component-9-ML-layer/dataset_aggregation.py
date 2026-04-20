import pandas as pd
import glob
import os
import json

def aggregate_datasets(data_folder):
    """
    Aggregates datasets from multiple load test runs.

    Args:
        data_folder (str): Path to the folder containing multiple JSON result files.

    Returns:
        pd.DataFrame: Aggregated dataset.
    """
    all_files = glob.glob(os.path.join(data_folder, "*.json"))
    aggregated_data = pd.DataFrame()

    # Debugging: Print the list of files being processed
    print(f"Files found for aggregation: {all_files}")

    for file in all_files:
        print(f"Processing file: {file}")
        with open(file, 'r') as f:
            lines = f.readlines()
            print(f"Raw content of file {file}: {lines}")
            for line in lines:
                record = json.loads(line)
                # Debugging: Print each parsed record
                print(f"Parsed record: {record}")

                if record['type'] == 'Point' and 'metric' in record:
                    metric_name = record['metric']
                    data_point = record['data']

                    # Debugging: Print extracted data point
                    print(f"Extracted data point: {data_point}")

                    row = {
                        'metric': metric_name,
                        'time': data_point['time'],
                        'value': data_point['value'],
                        **data_point.get('tags', {})
                    }

                    # Debugging: Print row before adding failure column
                    print(f"Row before adding failure column: {row}")

                    if metric_name == 'http_req_failed':
                        row['failure'] = 1 if data_point['value'] > 0 else 0
                    elif metric_name == 'http_req_duration':
                        row['failure'] = 1 if data_point['value'] > 2000 else 0
                    else:
                        row['failure'] = 0

                    # Debugging: Print row after adding failure column
                    print(f"Row with failure column: {row}")

                    aggregated_data = pd.concat([aggregated_data, pd.DataFrame([row])], ignore_index=True)

    return aggregated_data

if __name__ == "__main__":
    # Example usage
    data_folder_path = "../component-7-load-testing/config/results/"
    aggregated_dataset = aggregate_datasets(data_folder_path)
    print(aggregated_dataset.head())