import time
import os
import glob 
from datetime import datetime
import requests
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import mimetypes
from dotenv import load_dotenv

load_dotenv()

SERVICE_ACCOUNT_FILE = 'client_secret\superiorenergy-de5b56bef19d.json'

# Define the scopes required
SCOPES = ['https://www.googleapis.com/auth/drive.file']

# Create a credentials object
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

FOLDER_ID = os.getenv('GOOGLE_DRIVE_TO_BE_APPROVED_FOLDER_ID')
# Create a Google Drive API client
service = build('drive', 'v3', credentials=credentials)

def upload_file(file_path):
    print('uploading...')
    # Get the MIME type of the file
    mime_type, _ = mimetypes.guess_type(file_path)
    
    # Define the file metadata
    file_metadata = {
        'name': os.path.basename(file_path),
        'parents': [FOLDER_ID]
        }
    media = MediaFileUpload(file_path, mimetype=mime_type)
    
    # Upload the file
    request = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    )
    
    response = request.execute()
    print('File ID:', response.get('id'))


def get_file():
    base_directory = os.path.expanduser('~/Downloads')
    #middle * is meant for sub directories
    file_pattern = os.path.join(base_directory, "invideo-ai*.mp4")  # Match any subdirectory and files starting with 'invideo-ai' and ending with '.mp4'
    #get the matching file
    files = glob.glob(file_pattern)
    not_good = ['C:\\Users\\alvar\\Downloads\\invideo-ai-1080 Eco-Friendly Roofing & Windows in Florid 2024-09-17 (5) (1).mp4','C:\\Users\\alvar\\Downloads\\invideo-ai-1080 Eco-Friendly Roofing & Windows in Florid 2024-09-30.mp4']
    if not files or files in not_good:
        return None
    
    # Sort files by modification time and return the most recent one
    most_recent_file = max(files, key=os.path.getmtime)
    return most_recent_file

def wait_for_file():

    last_seen_file = None
    while True:
        print('im waiting...')
        ai_file = get_file()
        print(ai_file)
        # If a new file appears or if the most recent file has changed, print it
        if  ai_file:
            return ai_file
            
        time.sleep(10)  # Poll every 10 seconds

def main():
    ai_file = wait_for_file()
    upload_file(ai_file)

if __name__ == '__main__':
    main()