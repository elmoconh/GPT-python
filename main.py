import openai
import config
from rich import print 
#from rich.table import table

openai.api_key = config.api_key
print("💬 [bold green]ChatGPT API en Python[/bold green]")


content = input("¿sobre que quieres hablar?")

response =openai.ChatCompletion.create(model="gpt-3.5-turbo-0301", 
                            messages=[{"role":"user","content": content}])

print(response.choices[0].message.content)



