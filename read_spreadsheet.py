import os
import pandas as pd
import requests
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from tqdm import tqdm
import humanize  # Import humanize library for human-readable time format

def read_spreadsheet(file_path):
    # Read the spreadsheet file into a pandas DataFrame, skip the first two rows
    df = pd.read_excel(file_path, skiprows=[0, 1])

    return df

def check_domain_status(domain_url):
    full_url = 'https://' + domain_url

    try:
        response = requests.get(full_url)
        if response.status_code != 200:
            return (domain_url, f"Down with status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        return (domain_url, f"Down with an error: {e}")

    return (domain_url, "Up and running")

def main():
    file_path = 'files\DomainTracking.xlsx'

    try:
        # Record the start time before the main execution starts
        start_time = datetime.now()

        spreadsheet_data = read_spreadsheet(file_path)

        # Extract the 'Domain' column from the DataFrame as a list
        domain_list = spreadsheet_data['DOMAIN'].dropna().tolist()

        # Use ThreadPoolExecutor to check domain status using multiple threads
        with ThreadPoolExecutor() as executor:
            # Get the number of workers (threads) in the executor
            num_threads = executor._max_workers

            # Use tqdm to create a progress bar for the domain status checks
            with tqdm(total=len(domain_list), desc="Checking domains", unit="domain") as pbar:
                # Submit the check_domain_status function for each domain in the list
                results = executor.map(check_domain_status, domain_list)

                # Update the progress bar for each completed domain status check
                for _ in results:
                    pbar.update(1)

        # Collect the results into a list
        domain_status_list = list(results)

        # Create a DataFrame for the domain status data
        columns = ['Domain', 'Status']
        domain_status_df = pd.DataFrame(domain_status_list, columns=columns)

        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d_%H-%M-%S")
        output_file_name = f"DomainStatus_{current_time}.xlsx"

        if not os.path.exists('previous-runs'):
            os.makedirs('previous-runs')

        # Save the domain status data to the 'previous-runs' folder
        output_file_path = os.path.join('previous-runs', output_file_name)
        domain_status_df.to_excel(output_file_path, index=False)

        # Calculate and display the total time taken and the number of threads used
        end_time = datetime.now()
        total_time = end_time - start_time

        # Format the total time to be human-readable
        formatted_time = humanize.precisedelta(total_time, minimum_unit='seconds')

        print(f"\nDomain status data saved to '{output_file_path}'.")
        print(f"Total time taken: {formatted_time}")
        print(f"Number of threads used: {num_threads}")

    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except pd.errors.EmptyDataError:
        print("The spreadsheet file is empty.")
    except pd.errors.ParserError:
        print("Error parsing the spreadsheet file. Please ensure it's in a valid format.")

if __name__ == "__main__":
    main()
