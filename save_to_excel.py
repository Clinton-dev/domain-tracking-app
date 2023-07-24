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
    columns = [
        "No.",
        "DOMAIN",
        "REGISTERING COMPANY",
        "WEBSITE STATUS",
        "REGISTRATION DATE",
        "WEBSITE HOST",
        "DEVELOPER HANDLING",
        "SERVER HANDLING",
        "TODAY",
        "NEXT DUE DATE",
        "DAYS TO DUE DATE",
        "AMOUNT +VAT (Ksh.)",
        "PAID BY (COMPANY)",
    ]
    domain_status_df = pd.DataFrame(domain_status_list, columns=columns)

    now = datetime.now()
    today = now.strftime("%d-%b-%Y")

    # Update the "TODAY" column with the current date
    domain_status_df["TODAY"] = today

    if not os.path.exists("previous-runs"):
        os.makedirs("previous-runs")

    output_file_name = f"DomainStatus_{now.strftime('%Y-%m-%d_%H-%M-%S')}.xlsx"
    output_file_path = os.path.join("previous-runs", output_file_name)
    domain_status_df.to_excel(output_file_path, index=False)

    return output_file_path
