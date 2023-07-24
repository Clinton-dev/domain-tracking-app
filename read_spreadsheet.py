import pandas as pd


def read_spreadsheet(file_path):
    """Read the spreadsheet file into a pandas DataFrame.

    Args:
        file_path (str): The path to the spreadsheet file.

    Returns:
        pd.DataFrame: The DataFrame containing the spreadsheet data.
    """
    df = pd.read_excel(file_path, sheet_name="active-sites")

    # available_columns = df.columns.tolist()

    # print("Available columns:")
    # print(available_columns)

    # Find the correct column name for "DOMAIN" (case-insensitive)
    domain_column = next(
        (column for column in df.columns if column.lower() == "domain"), None
    )

    if not domain_column:
        raise ValueError("Column 'DOMAIN' not found in the 'active-sites' sheet.")
    return df
