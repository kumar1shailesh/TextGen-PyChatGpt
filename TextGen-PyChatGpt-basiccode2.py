import openai

openai.api_key = 'sk-UbuY8SpGpqXXXXX'

# instead of text-davinci-003 you can use latest gpt-3.5-turbo Learn More https://www.youtube.com/@AIMLDLNLP-TECH/
response = openai.Completion.create(
  engine="text-davinci-003",
  prompt="What dinosaurs lived in the cretaceous period?",
  max_tokens=60
)

print(response.choices[0].text.strip())
