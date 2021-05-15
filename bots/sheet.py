import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials


class Sheet_Controller:
    def __init__(self):
        self.scope = ['https://spreadsheets.google.com/feeds', 
                    'https://www.googleapis.com/auth/drive']
        self.creds = {
            "type": "service_account",
            "project_id": os.environ['SHEET_PROJECT_ID'],
            "private_key_id": os.environ['SHEET_PRIVATE_KEY_ID'],
            "private_key": os.environ['SHEET_PRIVATE_KEY'],
            "client_email": os.environ['SHEET_CLIENT_EMAIL'],
            "client_id": os.environ['SHEET_CLIENT_ID'],
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": os.environ['SHEET_CLIENT_X509_CERT_URL']
        }
        self.client = None
        self.sheets_list = []

        self.creds['private_key'] = self.creds['private_key'].replace('\\n', '\n')

    def authorize_access(self):
        credentials = ServiceAccountCredentials.from_json_keyfile_dict(self.creds, self.scope)
        self.client = gspread.authorize(credentials)
    
    # for this project, will use sheet_num 0 and 1
    def open_sheet(self, sheet_name, sheet_num):
        sheet = self.client.open(sheet_name).get_worksheet(sheet_num)
        self.sheets_list.append(sheet)
    
    def get_value(self):
        first_sheet = self.sheets_list[0]
        second_sheet = self.sheets_list[1]

        used_tweet = first_sheet.row_values(2)
        first_sheet.delete_rows(2)
        second_sheet.insert_row(used_tweet, 2)
        
        # only returning index 0 since only using one value from each row for this project
        return used_tweet[0]


# def main():
#     sheet = Sheet_Controller()
#     # print(sheet.creds)

# if __name__ == '__main__':
#     main()