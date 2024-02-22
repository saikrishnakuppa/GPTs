secret_key = ''

from openai import OpenAI

client = OpenAI(api_key=secret_key)

output = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)

print(output)