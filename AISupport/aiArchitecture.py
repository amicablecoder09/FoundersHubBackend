
import ast
import os
from openai import AzureOpenAI

client = AzureOpenAI(
  api_key = "1130d99fb30545d8957a9fa8bf91c0c7",  
  api_version = "2024-02-01",
  azure_endpoint = "https://fhcopilot.openai.azure.com"
)

sys_prompt = "Your will be provided with the startup details along with it's functional and non-functional requirements. You are supposed to return the mermaid diagram. If asked for frontend then only frontend and if asked for backend then return the backend. Don't return any extra text. Just return the mermaid code in json as a string without code tags. key is 'mermaid_code' and value will have only it's code. return code will be parsed using ast.literal_eval. make sure it is parsable. "

def getAIArchitecture(startup_data, prompt):
    print(startup_data)
    response = client.chat.completions.create(
        model="gpt-35-turbo", # model = "deployment_name".
        messages=[
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": "start details: \n" + str(startup_data) + " " + prompt}
        ]
    )
    message = response.choices[0].message
    result = ast.literal_eval(message.content)
    print(result)
    return result