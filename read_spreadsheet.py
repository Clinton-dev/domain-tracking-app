import os
import pandas as pd
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from tqdm import tqdm
import humanize  # for human-readable time format

def read_spreadsheet(file_path):
    """Read the spreadsheet file into a pandas DataFrame.

    Args:
        file_path (str): The path to the spreadsheet file.

    Returns:
        pd.DataFrame: The DataFrame containing the spreadsheet data.
    """
    df = pd.read_excel(file_path, skiprows=[0, 1])
    return df

def check_domain_status(domain_url):
    """Check the status of a domain.

    Args:
        domain_url (str): The domain URL to check.

    Returns:
        tuple: A tuple containing the domain URL and its status.
    """
    full_url = 'https://' + domain_url

    try:
        response = requests.get(full_url)
        if response.status_code != 200:
            return (domain_url, f"Down with status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        return (domain_url, f"Down with an error: {e}")

    return (domain_url, "Up and running")

def save_domain_status_to_excel(domain_status_list):
    """Save the domain status data to an Excel file.

    Args:
        domain_status_list (list): A list of tuples containing domain status data.

    Returns:
        str: The path of the saved Excel file.
    """
    columns = ['Domain', 'Status']
    domain_status_df = pd.DataFrame(domain_status_list, columns=columns)

    # Filter sites with "Up and running"
    filtered_df = domain_status_df[domain_status_df["Status"] != "Up and running"]

    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d_%H-%M-%S")
    output_file_name = f"DomainStatus_{current_time}.xlsx"

    if not os.path.exists('previous-runs'):
        os.makedirs('previous-runs')

    output_file_path = os.path.join('previous-runs', output_file_name)
    filtered_df.to_excel(output_file_path, index=False)

    return output_file_path

def main():
    file_path = 'files\DomainTracking.xlsx'

    try:
        start_time = datetime.now()

        spreadsheet_data = read_spreadsheet(file_path)
        domain_list = spreadsheet_data['DOMAIN'].dropna().tolist()

        with ThreadPoolExecutor() as executor:
            with tqdm(total=len(domain_list), desc="Checking domains", unit="domain") as pbar:
                futures = [executor.submit(check_domain_status, domain) for domain in domain_list]
                for future in as_completed(futures):
                    pbar.update(1)

        domain_status_list = [future.result() for future in futures]

        output_file_path = save_domain_status_to_excel(domain_status_list)

        end_time = datetime.now()
        total_time = end_time - start_time
        formatted_time = humanize.precisedelta(total_time, minimum_unit='seconds')

        print(f"\nDomain status data saved to '{output_file_path}'.")
        print(f"Total time taken: {formatted_time}")
        print(f"Number of threads used: {executor._max_workers}")

    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except pd.errors.EmptyDataError:
        print("The spreadsheet file is empty.")
    except pd.errors.ParserError:
        print("Error parsing the spreadsheet file. Please ensure it's in a valid format.")

if __name__ == "__main__":
    main()
