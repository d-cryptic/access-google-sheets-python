# Accessing Google Sheets using python

1. Go to [Google Developer Console](https://console.cloud.google.com/)
2. Go and create a `Project`
3. Click on `Enable API and services`
4. Search for `Google Drive API`
5. Click on `Enable`
6. Again search for `Google Sheets API` and click `Enable`
7. Go to main screen and click on `Credentials`
8. Click `Create Credentials` and click on `Service account`
9. Enter service account name and ID and give descriotion
10. Click enter
11. For Role, Search for project -> role -> editor
12. Click Done
13. Go to keys -> add key -> create new key -> JSON
14. Move the json credentials to project folder
15. Create a google sheet
16. Go to credentials json -> copy client email id -> go to google sheet -> click on share -> enter the email id
17. Now you have access to the google sheet

### Installation

#### MACOS/ Linux

```python
python3 -m venv venv
. venv/bin/activate
pip install gspread
```

##### Windows

```python
py -3 -m venv venv
venv\Scripts\activate
pip install gspread
```
