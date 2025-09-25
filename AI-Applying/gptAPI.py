import os
from openai import OpenAI

os.environ["OPENAI-API-KEY"] = ("Sua OpenAI API KEY")
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    max_tokens = 200,
    temperature = 0.1,
    messages = [
        {"role": "system", "content": "Você é um experiente progarmador. Retorne somente codigos limpos e de qualidade"},
        {
            "role": "user",
            "content": "Escrava um codigo de Hello Word em Python."
        }
    ]
)

print(response.choices[0].message.content)
