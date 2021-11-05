import gspread # pip install gspread

gc = gspread.service_account(filename="credentials.json")

# Key of google sheets - found in the URL of the sheet
sh = gc.open_by_key('1s_C1pAwxejfEr0Nyt9FlPXQPZ6aTNM_oUDS_AFr0ut8')

worksheet = sh.sheet1

# res = worksheet.get_all_records()

# res = worksheet.get_all_values()

# res = worksheet.row_values(1)

# res = worksheet.col_values(1)

# range
res = worksheet.get("A2:C2")
print(res)

# Adds at the starting of the sheet
user = ["Susan", 25, "Sydney"]

# Appends at 3rd of the sheet
# worksheet.insert_row(user)
# worksheet.insert_row(user,3)

# (row, column, value)
worksheet.update_cell(6,2,28)

worksheet.delete_rows(1)