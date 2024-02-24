import os
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key="b0ee2656ed2841018d5842c37c9ab801",
    api_version="0613", #"2023-12-01-preview",
    azure_endpoint="https://wpptech-dalle.openai.azure.com/openai/deployments/gpt-4/chat/completions?api-version=2023-07-01-preview0"
)

deployment_name = 'gpt-4'  # This will correspond to the custom name you chose for your deployment when you deployed a model. Use a gpt-35-turbo-instruct deployment.

# Send a completion call to generate an answer
print('Sending a test completion job')
start_phrase = 'Write a tagline for an ice cream shop. '
response = client.completions.create(model=deployment_name, prompt=start_phrase, max_tokens=10)
print(start_phrase + response.choices[0].text)