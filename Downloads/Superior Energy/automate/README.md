To run:
1) cd /Automate-AI-Invideo
2) Create virtual environment:  python -m venv virtual
3) Connect to virtual environment:
    (Mac/ Linux): source venv/bin/activate
    (Windows) : venv\Scripts\activate
4) Install requirements.   pip install -r requirements.txt
5) Create a .env with EMAIL and PASSWORD
6) Run code


The way this will work
1) On an EC2 instance a scheduler will have 5 videos created from script.py a day, one after the other. Those will end up in to_be_approved_folder. Client would approve them by moving them manually to approved folder.
2) to upload the video it is neccessary to have it in current working directory. When ready to upload video  is downloaded from download_video.py. download_video.py also deletes the video from the google drive
4) Immediately afterwards upload_video.py is ran to upload it to youtube. This command will take several arguments, among them the name of the video, which will be in cwd.
5) Remove the video from cwd 


keep in mind the above commands will be ran every day on the EC2 instance. Once early in the morning to get 5 videos in the pre approval process. Then 3 times throughout the day to upload the video.



