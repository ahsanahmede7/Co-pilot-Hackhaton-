from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv()


client = OpenAI(

    api_key=os.getenv(
        "GROQ_API_KEY"
    ),

    base_url=
    "https://api.groq.com/openai/v1"

)



def generate_report(
        result,
        confidence,
        reasons):


    prompt=f"""

You are a banking AI assistant.

Prediction:
{result}

Confidence:
{confidence:.2f}%

Reasons:
{reasons}


Write professional loan assessment summary.

Do not add new information.

"""


    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )


    return response.choices[0].message.content