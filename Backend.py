from openai import OpenAI 

OpenAI.my_api_key = 'YOUR_API_KEY'
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What are some famous astronomical observatories?"}
  ]
)