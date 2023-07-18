import os
import pandas as pd
from datetime import datetime


def save_domain_status_to_excel(domain_status_list):
    """Save the domain status data to an Excel file.

    Args:
        domain_status_list (list): A list of tuples containing domain status data.

    Returns:
        str: The path of the saved Excel file.
    """
    columns = ["Domain", "Status"]
    domain_status_df = pd.DataFrame(domain_status_list, columns=columns)

    # Filter sites with "Up and running"
    filtered_df = domain_status_df[domain_status_df["Status"] != "Up and running"]

    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d_%H-%M-%S")
    output_file_name = f"DomainStatus_{current_time}.xlsx"

    if not os.path.exists("previous-runs"):
        os.makedirs("previous-runs")

    output_file_path = os.path.join("previous-runs", output_file_name)
    filtered_df.to_excel(output_file_path, index=False)

    return output_file_path
