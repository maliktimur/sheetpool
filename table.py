import requests
from sheetfu import SpreadsheetApp

LINK = 'https://slushpool.com/accounts/profile/json/btc'
KEY = 'SlushPool-Auth-Token'
VALUE = 'akyITWhHPwVuemvc'
SPREADSHEETID = '1U_psV52hdOTkgcUIACrOlRn9kVRB37tfW_Drn7t_Ang'
SHEET = 'RealData'

r = requests.post(LINK, headers = {KEY:VALUE})
obj = r.json()
keys = []
values = []

for key, value in obj.items():
    keys.append(key)
    values.append(value)
    # print(key, value)


for key, value in values[1].items():
    keys.append(key)
    values.append(value)
    # print(key, value)
del(values[1])
# print(keys)
# print(values)
keys[1] = 'coin'

excel_data = [
 values
]

sa = SpreadsheetApp('secret.json')
spreadsheet = sa.open_by_id(SPREADSHEETID)
sheet = spreadsheet.get_sheet_by_name(SHEET)

data = sheet.get_data_range()
inside = data.get_values()
# print(inside)

data_range = sheet.get_range(
    row=len(inside)+1, 
    column=1,
    number_of_column=len(values)
)
data_range.set_values(excel_data)

