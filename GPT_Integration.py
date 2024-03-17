from openai import OpenAI
import os
from dotenv import load_dotenv
import Flowchart
import json

load_dotenv()
My_API_KEY = os.getenv('MY_API_KEY')
client = OpenAI(api_key = My_API_KEY)


semester = '0'
taken_courses = ''
preferences = 'None'
courses_str = json.dumps(Flowchart.cmpsc_courses, indent=2)
gen_ed_str = cmpsc_courses_str = json.dumps(Flowchart.general_education, indent=2)
cmpsc_electives_str = json.dumps(Flowchart.CMPSC_Electives, indent=2)
four_credit_str = json.dumps(Flowchart.four_credit, indent=4)
priorty_str = json.dumps(Flowchart.priorty, indent=4)

introduction = "You are a Penn State Engineering Advisor, specifically for Computer Science. Your goal is to create an academic schedule based off the given content."
explain_main_courses = f"Here is a dictionary with all the keys as required courses to take as a Computer Science Major. These courses NEED to be in the schedule. Also, CMPSC 111 needs to be taken in semester 1 or 2 since it is a first-year-seminar class.\
           You must ensure that the student takes another CMPSC course in the same semester as CMPSC 111, additionally, ENGL 015 should be prioritized to be taken in semester 1 or 2.\
           Prioritize taking the courses in {priorty_str} because these are the core classes you need to get started in the Computer Science track \
           An element can be a equivalent course you can take if there is a dash (-) in front of it. \
           If the characters -c are attached to the end of a course, this signifies that the course is a concurrent requirement for the key course.\
           Every other element is a pre-requisite (prereq) course. Pre-requisite courses MUST be taken before the course that it is a pre-requisite for. Every course (key) within this dictionary should be considered a major course."
explain_general_education = "Here is a dictionary with all of the general education credits. \
           Each key can be treated as a course. \
           Each key's value refers to the total credits that are needed for that specific course.\
           General education credit courses can be displayed as their key values (type of general education credit - not actual specific course) when put into a schedule.\
           Within a single semester in the schedule, you must include 1-2 general education courses. \
           When adding the general education courses to the schedule, add each course 3 credits as each course."
explain_CMPSC_electives = f"Within the dictionary of all the general education credits, there is a key that is labeled \"CMPSC Electives\"\
           Here is an additional dictionary named CMPSC_Electives. Based on the user's preferences being: {preferences}, choose 6 credits worth of courses.  \
           The courses in the CMPSC_Electives will fulfull the CMPSC Electives general education requirement"
explain_credit_values = "Here is a list of all the courses with a credit value of 4.\
           CMPSC 111 is 1 credit. If a course is not within this list and is not CMPSC 111, it can be assumed that the course is worth 3 credits."
explain_courses_taken = "Here is a list of all of the credits that the student has already taken. \
            Add all of these credits to the total credits needed for the student's degree. These courses have already been taken so do not include them into the schedule."
explain_major_credits = "This number is the total required major credits, that is, the total number of credits from courses that are not considered general education credits needed for a student to obtain their Computer Science degree."
create = f"Given that the student has already taken {semester} semesters, create a schedule for the student's remaining semesters that satisfies the major credits that are still needed and the general education credits that are still needed.\
           Attempt to satisfy the student's CMPSC_electives courses preferences but do not prioritize those preferences.\
           Keep the total credits that a student takes within a semester between 15 and 19. Do not display credit values at all. Format the schedule as a dictionary "


chat_completion = client.chat.completions.create(
    messages=[
        {"role": "system", "content": ""},
        {"role": "system", "content": explain_main_courses},  # Explain main courses
        {"role": "system", "content": Flowchart.cmpsc_courses},
        {"role": "system", "content": explain_general_education}, # Explain gen eds
        {"role": "system", "content": Flowchart.general_education},
        {"role": "system", "content": explain_CMPSC_electives}, # Explain CMPSC Electives (preferences)
        {"role": "system", "content": Flowchart.CMPSC_Electives},
        {"role": "system", "content": explain_credit_values}, # Explain credit values
        {"role": "system", "content": Flowchart.four_credit},
        {"role": "system", "content": explain_courses_taken}, # Explain courses taken
        {"role": "system", "content": taken_courses},
        {"role": "system", "content": explain_major_credits}, # Explain major credits
        {"role": "system", "content": Flowchart.major_cred},
        {"role": "system", "content": create}, # Create the schedule
    ],
    model = "gpt-3.5-turbo"
)

print(chat_completion.choices[0].message.content)
