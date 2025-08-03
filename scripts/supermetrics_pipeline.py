# scripts/supermetrics_pipeline.py
import os
import csv
from datetime import datetime
import schedule
import time

def fetch_supermetrics_data(api_key, query_id):
    """
    Placeholder function to simulate fetching data from Supermetrics.
    In a real implementation, this would make an API call to Supermetrics.
    """
    print(f"Fetching data from Supermetrics for query ID: {query_id}")
    print(f"Using API Key: {api_key[:4]}... ")

    # Mocked CSV response data
    mock_data = [
        ["Date", "Campaign", "Ad Platform", "Impressions", "Clicks", "Cost"],
        ["2023-10-26", "Fall Sale", "Facebook Ads", "10000", "200", "50.00"],
        ["2023-10-26", "Q4 Push", "Google Ads", "12000", "350", "150.00"],
        ["2023-10-27", "Fall Sale", "Facebook Ads", "11000", "220", "55.00"],
        ["2023-10-27", "Q4 Push", "Google Ads", "13000", "380", "160.00"],
    ]
    
    print("Data fetched successfully.")
    return mock_data

def store_data(data, directory="data"):
    """
    Stores the fetched data into a CSV file with a timestamp.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(directory, f"supermetrics_data_{timestamp}.csv")
    
    try:
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(data)
        print(f"Successfully stored data in {filename}")
    except Exception as e:
        print(f"Error storing data: {e}")


def job():
    """The job to be scheduled."""
    print("--- Running Supermetrics Pipeline Job ---")
    
    # In a real app, use environment variables or a secure config service
    SUPERMETRICS_API_KEY = os.environ.get("SUPERMETRICS_API_KEY", "YOUR_API_KEY")
    SUPERMETRICS_QUERY_ID = os.environ.get("SUPERMETRICS_QUERY_ID", "YOUR_QUERY_ID")
    
    try:
        data = fetch_supermetrics_data(SUPERMETRICS_API_KEY, SUPERMETRICS_QUERY_ID)
        store_data(data)
        print("--- Supermetrics Pipeline Job Finished ---")
    except Exception as e:
        print(f"An error occurred during the job: {e}")

def main():
    """
    Main function to run the pipeline scheduler.
    This is for demonstration. In production, this would be a long-running service.
    """
    print("--- Supermetrics Data Pipeline Scheduler ---")
    print("This script will run the job once for demonstration purposes.")
    
    # Schedule the job to run every day at a specific time
    # schedule.every().day.at("01:00").do(job)
    
    # For this example, we'll just run the job once immediately.
    job()
    
    # In a real scenario, you would uncomment the following lines:
    # print("Scheduler started. Waiting for the next scheduled run...")
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)

if __name__ == "__main__":
    main() 