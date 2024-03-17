from openai import OpenAI
import os
from dotenv import load_dotenv
import Flowchart
import json

load_dotenv()
OPENAI_API_KEY = os.getenv('MY_API_KEY')
client = OpenAI(api_key = OPENAI_API_KEY)


semester = '0'
taken_courses = 'CMPSC 131'
preferences = 'None'
courses_str = json.dumps(Flowchart.cmpsc_courses, indent=2)
gen_ed_str = json.dumps(Flowchart.general_education, indent=2)
cmpsc_electives_str = json.dumps(Flowchart.CMPSC_Electives, indent=2)
four_credit_str = json.dumps(Flowchart.four_credit, indent=4)
priority_str = json.dumps(Flowchart.priority, indent=4)

prompt_one = f'You are a Penn State Engineering Advisor, specifically for Computer Science. Your goal is to create an academic schedule that meets graduation requirenets based off the given content. \
Attached is a dictonary: {courses_str} , with the keys as required courses needed to graduate. Lets call the key, key course. The values is a dictionary. \
In that dictionary, there are concurrent courses which can be taken with the key course, then pre-requisite courses that must be taken BEFORE the key course. \
Another dictionary: {priority_str} , is a list of courses that you are going to prioritize to take as soon as possible.'

prompt_two = f'In addition, there is a dictionary: {gen_ed_str} , with all of the general education credits. Each key is treated as a course and the value refers to the total credits needed to fulfill the general education requirement. Add enough general educuation courses to fulfill its specific credit requirement. \
In the general education dictionary, there is a key named CMPSC Electives. This is a special case. There is another dictionary named preferences: {preferences}. Based off the preferences, choose courses in the CMPSPC Electives dictionary: {cmpsc_electives_str}. Take enough credits of the classes provided to fulfill the cmpsc electives general education requirement.\
NOTE: The CMPSC electives are DIFFERENT than the department (engineering) electives. For the credit values, here is a list: {four_credit_str}, with all courses that have 4 credits. CMPSC 111 has 1 credit. Assume all other courses are 3 credits. \
Given that the student has already taken: {semester}, in the schedule create the remaining semesters so the total semesters adds up to 8. For example, if someone has already taken 3 semesters, create 5.'

prompt_three = f'This string: {taken_courses}, has all the courses already taken. Do not add these courses in the string to the schedule. These also fulfill the prequisite requirements. For example, if you have already taken MATH 140, you can take MATH 141. \
If the user has taken 0 semesters, these are the UNIQUE requirements for the first two semesters: must take CMPSC 111, ENG 015, CMPSC 131 and most of the other classes in priority dictionary mentioned before \
These are the requirements for each semesters, including the first two: 15-19 credits, 1-2 general education courses \
These are the requirements for the entire schedule: 8 semesters max, 45 general education credits, 82 major credits\
Output the schedule in the form of a dictionary. Do not include credits in the schedule. Include type of general education credit. A sample output looks like: \
    Semester 1: \
        CMPSC 131 \
        MATH 140 \
        ENGL 015 \
        GN General Education \
    ... \
    Semester 7: \
        CMPSC 450 \
        CMPSC 483W or CMPSC 431W \
        Department (Engineering) Elective \
    In addition, \'Department (Engineering) Elective\' is added, treat it as a 3 credit course. Therefore you will need to add it three times. Implement this into a dictionary.'


chat_completion = client.chat.completions.create(
    messages=[

        {"role": "system", "content": prompt_one},
        {"role": "system", "content": prompt_two},
        {"role": "system", "content": prompt_three}

    ],
    model = "gpt-3.5-turbo"
)

schedule = chat_completion.choices[0].message.content


schedule_dict = json.loads(schedule)
print(schedule_dict)
