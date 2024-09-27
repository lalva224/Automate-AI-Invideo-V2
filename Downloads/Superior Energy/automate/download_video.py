import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import io
from dotenv import load_dotenv
load_dotenv()

# Define constants

SERVICE_ACCOUNT_FILE = 'client_secret\superiorenergy-de5b56bef19d.json'

# Define the scopes required
SCOPES = ['https://www.googleapis.com/auth/drive.file']

# Create a credentials object
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

FOLDER_ID = os.getenv('GOOGLE_DRIVE_APPROVED_FOLDER_ID')
print(FOLDER_ID)
# Create a Google Drive API client
service = build('drive', 'v3', credentials=credentials)

#get File ID
results = service.files().list(
    q=f"'{FOLDER_ID}' in parents",  # Necessary to specify that you want files from a specific folder
    fields="nextPageToken, files(id, name)",  # Specify which fields to return
    pageSize=100  # Adjust if you want more files
).execute()
print(results)
items = results.get('files', [])
FILE_ID = items[0]['id']
print(FILE_ID)
# Create a request to download the file
#to make sure audio is included
file_metadata = service.files().get(fileId=FILE_ID, fields='mimeType').execute()
mime_type = file_metadata.get('mimeType')
file_name = file_metadata.get('name')
print(f"File Name: {file_name}")
print(f"Original MIME type: {mime_type}")

request = service.files().get_media(fileId=FILE_ID)
file_handle = io.BytesIO()

# Download the file
downloader = MediaIoBaseDownload(file_handle, request)
done = False
while done is False:
    status, done = downloader.next_chunk()
    print(f"Download {int(status.progress() * 100)}%.")

# Save the downloaded file to disk
file_handle.seek(0)  # Move to the beginning of the BytesIO object
with open('downloaded_video.mp4', 'wb') as f:
    f.write(file_handle.read())

print("Video downloaded successfully.")

service.files().delete(fileId=FILE_ID).execute()
print('File deleted successfully')
