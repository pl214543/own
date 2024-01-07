# required libraries
import gspread
from google.oauth2.service_account import Credentials
import time

# sets up the API for gspread and google sheets
scopes = \
    ["https://spreadsheets.google.com/feeds",
     "https://www.googleapis.com/auth/drive"]
# credentials for service account made using google cloud
credentials = Credentials.from_service_account_file(
    "C:/Users/alexe/Downloads/pwpwinterservice.json",
    scopes=scopes)
authorize = gspread.authorize(credentials)

# function that opens the spreadsheet and updates the cells
def insertion(spreadsheet, sheetNumber, column, nameList):
    namesSheet = authorize.open(spreadsheet).get_worksheet(sheetNumber)
    row = 1
    for name in nameList:
        namesSheet.update_cell(row, column, name)
        # so that the cells keep updating down the column and not overlapping
        row += 1
        # google api has a quota that will not allow anything quicker
        time.sleep(1)
