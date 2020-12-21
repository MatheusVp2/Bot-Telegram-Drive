from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()



gauth = GoogleAuth()
# Try to load saved client credentials
gauth.LoadCredentialsFile("creds.txt")
if gauth.credentials is None:
    # Authenticate if they're not there
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()
else:
    # Initialize the saved creds
    gauth.Authorize()
# Save the current credentials to a file
gauth.SaveCredentialsFile("creds.txt")
# gauth = GoogleAuth()
# gauth.LocalWebserverAuth()


drive = GoogleDrive(gauth)
file_path = filedialog.askopenfilename()
if file_path:
    print(file_path)
    pass
    # file1 = drive.CreateFile()
    # file1.SetContentFile(file_path)
    # file1.Upload()