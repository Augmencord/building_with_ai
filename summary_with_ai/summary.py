#how python reads a CSV file

import pandas as pd

df = pd.read_csv('datafile.txt')

head  = df.head()

Stats = df.describe()

prompt = f'''

I have a pandas dataframe with the information of the data stored in{df}.

I have the statical analysis of that data stored in {Stats}

Print a short summary pof the data. Explain it in easy conversational manner for a non technical person to understand

'''

"""
from google import genai

client = genai.Client(api_key="UseGoogleAIStudioToGetTheKey")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents = prompt
)

print(response.text)

"""