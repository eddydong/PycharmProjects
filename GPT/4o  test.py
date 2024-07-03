from openai import AzureOpenAI

ai_client = AzureOpenAI(
    azure_endpoint="https://for-tom-dev-australia-east.openai.azure.com/",
    azure_deployment="gpt-4",
    api_key="0f24ce3280334b2a8818ba951452b474",
    api_version="2024-02-15-preview"
)
ret = ai_client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "美国总统是谁?"}]
    )

print(ret.choices[0].message.content)
