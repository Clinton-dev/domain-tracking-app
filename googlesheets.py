import gspread
from oauth2client.service_account import ServiceAccountCredentials
import traceback


def authenticate_google_sheets_api(credentials_file):
    # Function to authenticate and get access to the Google Sheets API
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)
    return gspread.authorize(creds)

def list_all_titles(client):
    spreadsheets = client.openall()
    for spreadsheet in spreadsheets:
        print(spreadsheet.title)

def main():
    credentials_file = 'credentials2.json'

    try:
        client = authenticate_google_sheets_api(credentials_file)
        # client = gspread.service_account(filename=credentials_file)

        print(client.open('domainTrackingCopy'))

    except Exception as e:
        print("Error:")
        traceback.print_exc()

if __name__ == "__main__":
    main()








# mysheet = client.open('Copy of Domain Tracking').sheet1

# print(mysheet)
