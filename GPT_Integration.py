from openai import OpenAI 
import os
import Flowchart as fc
client = OpenAI(api_key = "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")
print(fc.cmpsc_courses)
prompt = input("User : ") 

chat_completion = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "You are a Penn State Engineering Advisor."},
        {"role": "system", "content": fc.cmpsc_courses},
        {"role": "system", "content": "This is a list of all Penn State Computer Science courses and prerequisites."},
        {"role": "user", "content": prompt}
    ],
    model = "gpt-3.5-turbo"
)

print(chat_completion.choices[0].message.content)