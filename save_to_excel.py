import os
import pandas as pd
from datetime import datetime


def save_domain_status_to_excel(domain_status_list, spreadsheet_data):
    """Save the domain status data to an Excel file.

    Args:
        domain_status_list (list): A list of tuples containing domain status data.
        spreadsheet_data (DataFrame): The DataFrame read from the spreadsheet.

    Returns:
        str: The path of the saved Excel file.
    """
    columns = ["STATUS", "DOMAIN", "REGISTERING COMPANY \n", "REGISTRATION\n DATE",
               "WEBSITE \nHOST", "DEVELOPER \nHANDLING", "SERVER HANDLING", "PAID BY \n(COMPANY)"]

    # Create a DataFrame from the domain_status_list
    domain_status_df = pd.DataFrame(domain_status_list, columns=["DOMAIN", "STATUS"])

    # Merge the domain_status_df with the relevant columns from spreadsheet_data
    relevant_data = spreadsheet_data[columns[1:]]  # Exclude "STATUS" column from spreadsheet_data
    merged_df = pd.concat([domain_status_df, relevant_data], axis=1)

    # Filter sites with "Up and running"
    filtered_df = merged_df[merged_df["STATUS"] != "Up and running"]

    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d_%H-%M-%S")
    output_file_name = f"DomainStatus_{current_time}.xlsx"

    if not os.path.exists("previous-runs"):
        os.makedirs("previous-runs")

    output_file_path = os.path.join("previous-runs", output_file_name)
    filtered_df.to_excel(output_file_path, index=False)

    return output_file_path
