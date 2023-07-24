from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
import humanize  # for human-readable time format
from read_spreadsheet import read_spreadsheet
from check_domain_status import check_domain_status
from save_to_excel import save_domain_status_to_excel
from datetime import datetime
from terminaltables import SingleTable
import pandas as pd


def main():
    file_path = "files\Domain Tracking.xlsx"

    try:
        start_time = datetime.now()

        spreadsheet_data = read_spreadsheet(file_path)
        domain_list = spreadsheet_data["DOMAIN"].dropna().tolist()

        with ThreadPoolExecutor() as executor:
            with tqdm(
                total=len(domain_list), desc="Checking domains", unit="domain"
            ) as pbar:
                futures = [
                    executor.submit(check_domain_status, domain)
                    for domain in domain_list
                ]
                for future in as_completed(futures):
                    pbar.update(1)

        domain_status_list = [future.result() for future in futures]

        output_file_path = save_domain_status_to_excel(domain_status_list)

        num_up_sites = sum(
            1 for _, status, *_ in domain_status_list if status == "Active"
        )
        num_down_sites = sum(
            1 for _, status, *_ in domain_status_list if status != "Active"
        )

        end_time = datetime.now()
        total_time = end_time - start_time
        formatted_time = humanize.precisedelta(total_time, minimum_unit="seconds")

        print("\n" + "=" * 40)  # Top border
        print("Domain status data saved to 'previous-runs'")
        print("=" * 40)  # Middle border

        # Prepare the data for the table
        table_data = [
            ["Total time taken", formatted_time],
            ["Number of threads used", executor._max_workers],
            ["Number of sites that are up", num_up_sites],
            ["Number of sites that are down", num_down_sites],
        ]

        # Create a SingleTable instance and set the title
        table_instance = SingleTable(table_data, title="Execution Summary")

        # Modify the border style to use dotted lines
        table_instance.inner_heading_row_border = False
        table_instance.inner_row_border = False
        table_instance.outer_border = False
        table_instance.junction_char = "."

        # Render the table and print it
        print(table_instance.table)

        print("=" * 40)  # Bottom border

    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except pd.errors.EmptyDataError:
        print("The spreadsheet file is empty.")
    except pd.errors.ParserError:
        print(
            "Error parsing the spreadsheet file. Please ensure it's in a valid format."
        )


if __name__ == "__main__":
    main()
