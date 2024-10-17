from openai import OpenAI
from prompt import description_prompt
import os
from dotenv import load_dotenv
load_dotenv()
import json
def create_title_and_description():
    try:
        client = OpenAI(api_key=os.getenv('OPEN_AI_KEY'))
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": description_prompt}
            ],
            
        )
        data_string = completion.choices[0].message.content
        data = json.loads(data_string)
        return data
    except Exception as e:
        print(f"Error: {e}")
        return None
