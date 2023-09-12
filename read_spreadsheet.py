import pandas as pd


def read_spreadsheet(file_path, sheet_name="active-sites"):
    """Read the spreadsheet data from the specified file.

    Args:
        file_path (str): The path of the Excel file.
        sheet_name (str, optional): The name of the sheet to read. Defaults to "active-sites".

    Returns:
        pd.DataFrame: The data from the specified sheet.
    """
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    print("Columns available in the spreadsheet:")
    print(df.columns.tolist())  # Print the column names
    return df
