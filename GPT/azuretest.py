from openai import AzureOpenAI
from threading import Thread
import time

client = AzureOpenAI(
    azure_endpoint="https://wpptech-dalle.openai.azure.com/",
    azure_deployment="gpt35turbo1106",
    api_key="b0ee2656ed2841018d5842c37c9ab801",
    api_version="2023-07-01-preview"
)
client.model = "gpt35turbo1106"

def gpt(s):
    res = client.chat.completions.create(
    model= client.model, # "gpt35turbo1106", # "gpt-35-turbo", # model = "deployment_name".
    messages=[
        #{"role": "system", "content": "You are a helpful assistant."},
        #{"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
        #{"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
        {"role": "user", "content": s}
    ])
    echo(res.choices[0].message.content)

def echo(s):
    print(s)

theme = "'I love you so much my daughter'"
sylist = [3,3,12,3,3,12]

tl=[]
for i in range(1):
    s = ("Write lyric for a " + str(len(sylist))
       + "-line melody. The theme is about: " + theme
       + ". Ensure syllable counts in each line follow the list: "
       + str(sylist) + ". Also please try your best to rhyme.")
    print(s)
    tl.append(Thread(target=gpt, args=[s]))

start_time = time.time()

for t in tl:
    t.daemon = True
    t.start()

for t in tl:
    t.join(4)

print("time used: ", time.time()-start_time)
