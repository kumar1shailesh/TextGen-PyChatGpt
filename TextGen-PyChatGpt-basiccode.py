import os
import openai


openai.api_key = "sk-UbuY8SXXXXXX-youropenai-key"


response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "As a advance seo blog writer "
    },
    {
      "role": "user",
      "content": "write on blog chatgpt"
    },
    {
      "role": "assistant",
      "content": ""
    }
  ],
  temperature=1,
  max_tokens=4000,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response["choices"][0]["message"]["content"])
