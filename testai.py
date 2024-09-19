
import os
from openai import AzureOpenAI

client = AzureOpenAI(
  api_key = "1130d99fb30545d8957a9fa8bf91c0c7",  
  api_version = "2024-02-01",
  azure_endpoint = "https://fhcopilot.openai.azure.com"
)

response = client.chat.completions.create(
    model="gpt-35-turbo", # model = "deployment_name".
    messages=[
        {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
        {"role": "user", "content": "How to create visio diagram?"}
    ]
)

print(response.choices[0].message.content)