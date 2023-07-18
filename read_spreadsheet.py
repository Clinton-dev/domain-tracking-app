import pandas as pd


def read_spreadsheet(file_path):
    """Read the spreadsheet file into a pandas DataFrame.

    Args:
        file_path (str): The path to the spreadsheet file.

    Returns:
        pd.DataFrame: The DataFrame containing the spreadsheet data.
    """
    df = pd.read_excel(file_path, skiprows=[0, 1])
    return df
