from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
import humanize  # for human-readable time format
from read_spreadsheet import read_spreadsheet
from check_domain_status import check_domain_status
from save_to_excel import save_domain_status_to_excel
from datetime import datetime


def main():
    file_path = "files\DomainTracking.xlsx"

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

        end_time = datetime.now()
        total_time = end_time - start_time
        formatted_time = humanize.precisedelta(total_time, minimum_unit="seconds")

        print(f"\nDomain status data saved to '{output_file_path}'.")
        print(f"Total time taken: {formatted_time}")
        print(f"Number of threads used: {executor._max_workers}")

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
