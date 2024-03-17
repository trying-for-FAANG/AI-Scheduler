from openai import OpenAI 
client = OpenAI(api_key = "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")
prompt = input("User : ") 

chat_completion = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "You are a Penn State Engineering Advisor."},
        {"role": "system", "content": dict_name},
        {"role": "system", "content": "This is a list of all Penn State Computer Science courses and prerequisites."},
        {"role": "user", "content": prompt}
    ],
    model = "gpt-3.5-turbo"
)

print(chat_completion.choices[0].message.content)