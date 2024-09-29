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
1) On an windows vps a scheduler will have 5 videos created from script.py a day, one after the other. Those will end up in to_be_approved_folder. Client would approve them by moving them manually to approved folder. 
Command: python script.py  (5 times)

2) to upload the video it is neccessary to have it in current working directory. When ready to upload video  is downloaded from download_video.py. download_video.py also deletes the video from the google drive
Commands:
python downloaded_video.py
(wait 30 seconds)

4) Immediately afterwards upload_video.py is ran to upload it to youtube. This command will take several arguments, among them the name of the video, which will be in cwd. It's deleted from cwd right afterwards.

5) . Bat file:
file 1 
.script.py (5 times one of the other every morning)

file 2
.download_video.py
.upload_video.py

scheduled 3 times a day, need to find the best times to do so




possible tags:
People & Blogs (Category ID: 21): This category can encompass personal stories, experiences, and informative content related to home improvement, which aligns well with roofing and windows services.

Howto & Style (Category ID: 24): If your ad includes tips, DIY advice, or informative content about roofing and window services, this category is a great fit.

Science & Technology (Category ID: 26): If your ad emphasizes eco-friendly materials or innovative techniques used in roofing and window installations, this category could also be relevant.

Education (Category ID: 25): If your ad focuses on educating viewers about the benefits of energy-efficient windows or storm recovery solutions, this category could work well.