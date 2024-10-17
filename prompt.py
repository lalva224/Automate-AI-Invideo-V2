prompt = """
make a tiktok ad for Superior Roofing and Windows, an eco friendly contractor focused on replacing roofs and windows. They provide outstanding roofing services across Central Florida, Tampa Bay, and the Florida East Coast and their surrounding areas. 
Here is how they do business 
1)Residential roofing with flexible financing
2) After storms. We take insurance to help cover costs

Some selling points:
Windows - energy efficient windows 
Pay nothing out of pocket

At the end of the video mention going to the  link in bio to visit web page
also please do not make up fake statistics

Settings:
Use a male clear American voice for the Narrator.
Add clean subtitles with outline.
Use Superior Roofing and windows as watermark text.
Use fewer iStock
Use the best audio available

"""

description_prompt = """"
I am going to give you a prompt that will be used to create a video on the AI. Invideo platform. What I need you to do is to create a title and description for my youtube video. Please be unique every time i send you this:
based off of it:
make a tiktok ad for Superior Roofing and Windows, an eco friendly contractor focused on replacing roofs and windows. They provide outstanding roofing services across Central Florida, Tampa Bay, and the Florida East Coast and their surrounding areas. 
Here is how they do business 
1)Residential roofing with flexible financing
2) After storms. We take insurance to help cover costs

Some selling points:
Windows - energy efficient windows 
Pay nothing out of pocket

At the end of the video mention going to the  link in bio to visit web page
also please do not make up fake statistics


give me this in json format text like this:

{
'title': 'Title',
'description': 'description'
}
"""