from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth
from selenium.webdriver.chrome.service import Service
import undetected_chromedriver as uc
from selenium.webdriver.common.action_chains import ActionChains
from dotenv import load_dotenv
import time
import os
from prompt import prompt
import glob 
from datetime import datetime
import requests
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import mimetypes
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

# Example usage



# options.add_argument("--headless")  # Enable headless mode

# options.add_argument("--headless")
driver = uc.Chrome(version_main=128)
driver.get("https://ai.invideo.io/")
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')

#click log in button
login_button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[1]/button'))).click()
main_window = driver.current_window_handle

# Switch to the new Google Sign-In window
for handle in driver.window_handles:
    if handle != main_window:
        driver.switch_to.window(handle)
        break

#type in email and click next
#for headless
# login_input = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/form/div/div/div/div/div/input[1]"))).send_keys(email)

#for non headless mode
login_input = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email']"))).send_keys(email)


next_button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'identifierNext'))).click()


#type password and click next
#for headless
# password_input = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/form/div/div/input"))).send_keys(password)
#non headless
password_input = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.NAME, 'Passwd'))).send_keys(password)

next_button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'passwordNext'))).click()
#go back to login page while it continues to load
try:
    driver.switch_to.window(main_window)
    print("Switched back to the main window successfully.")
except Exception as e:
    print(f"Error: {e} - Main window is not available.")

#enter prompt and send it
prompt_input = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,'brief'))).send_keys(prompt)
generate_button = driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()
#class c-cBOcTo

#once continue buttons pops up, click it. Later on we can randomly select a few options.
continue_button = WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div[1]/div[3]/div/div[1]/div/div/div/div[2]/div/div[2]/div/button'))).click()

#wait for video to generate and click on download button
download_button = WebDriverWait(driver,500).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div[1]/div[3]/div/div[1]/div/div/div/div[4]/div/div[1]/div[2]/button[2]'))).click()
#if on paid plan then just continue would be fine (remove watermarks) but for now we need to select free options before continue
#10 buttons. Click first 3rd and last (free selectors and continue button)
#wait for modal to load
WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'//*[@id="radix-:r9b:"]/div')))
#/html/body/div[3]/div/div[5]/div[2]/button
print('button clicked')



# selector1 = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="radix-:r9b:"]/div/div[3]/div/div[1]/div[1]/button[1]'))).click()
# selector2 = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="radix-:r9b:"]/div/div[3]/div/div[2]/div[1]/button[1]'))).click()
finish_button = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="radix-:r9b:"]/div/div[5]/div[2]/button'))).click()


#wait for video to download then get most recent file, which will be this video. Then upload to dropbox
time.sleep(60)


downloads_dir = os.path.expanduser('~/Downloads')
# files = glob.glob(os.path.join(downloads_dir, '*')
files = glob.glob(os.path.join(downloads_dir, '*'))
most_recent_file = max(files, key=os.path.getmtime)
#gets most recent file (os.path.getmtime checks all dates from jan 1st 1970 and gets the max, whcih is the newest file)
# most_recent_file = max(files, key=os.path.getmtime)
now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#upload to dropbox
# file_name= os.path.basename(most_recent_file)

upload_file(most_recent_file)
print('uploaded!!')
time.sleep(10)
os.remove(most_recent_file)






driver.quit()


