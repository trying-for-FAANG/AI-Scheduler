from openai import OpenAI
import os
from dotenv import load_dotenv
import Flowchart
import json

load_dotenv()
OPENAI_API_KEY = os.getenv('MY_API_KEY')
client = OpenAI(api_key = OPENAI_API_KEY)


semester = '0'
taken_courses = ''
taken_courses = taken_courses.split(',')
preferences = 'None'
courses_str = json.dumps(Flowchart.cmpsc_courses, indent=2)
gen_ed_str = json.dumps(Flowchart.general_education, indent=2)
cmpsc_electives_str = json.dumps(Flowchart.CMPSC_Electives, indent=2)
four_credit_str = json.dumps(Flowchart.four_credit, indent=4)
priority_str = json.dumps(Flowchart.priority, indent=4)
difficulties = "1 for easy, 2 for medium, and 3 for hard"



prompt = f"""\
#HACKPSU AI Schedule Advisor\n\
\n\
The goal is to create an academic schedule for a computer science student at Penn State University, taking into account the {preferences}. \
Here's a summary of the data structures available for creating the schedule:\n\
\n\
- **CMPSC Courses**: {courses_str}\n\
This dictionary contains computer science courses along with their concurrent courses, prerequisites, and a difficulty level.\n\
\n\
- **Taken Courses**: {taken_courses}\n\
A list of courses that have already been taken\n\
- **Semesters**: {semester}\n\
The number of semesters already taken.
- **Four Credit Courses**: {four_credit_str}\n\
A list of courses that are worth 4 credits each.\n\
\n\
- **Priority Courses**: {priority_str}\n\
A list of courses that should be prioritized in the student's schedule.\n\
\n\
- **General Education Requirements**: {gen_ed_str}\n\
A dictionary outlining the credits required for general education categories.\n\
\n\
-**Preferences**: {preferences}\n\
Prefences that should be considered when choosing electives or additional courses.\n\
- **CMPSC elective courses**: {cmpsc_electives_str}\n\
A detailed list of CMPSC elective courses including descriptions and prerequisites. The courses chosen should align with the preferences.'\n\
Given the student's preferences and the need to fulfill the CMPSC elective requirement, select electives that complement the core curriculum and enhance the student's skills in areas of interest such as software engineering, data science, or cybersecurity. For example, if focusing on cybersecurity, include 'CMPSC 443: Introduction to Computer and Network Security' among the elective courses.\n\
\n\
Given the constraints of 45 general education credits and 82 major credits to graduate, create a balanced academic schedule that:\n\
- Do not add courses that have already been taken in the Taken Courses list\n\
- Ensures that prerequisites and concurrent courses are satisfied.\n\
- Incorporates priority courses early in the academic career.\n\
- Fulfills both general education and major requirements.\n\
- If the course in not General Education, include the specific course\n\
- Considers the difficulty of courses to balance the workload each semester, aiming for a mix that manages the student's stress and academic success.\n\
- Aims for a total of 8 semesters, with previous semesters taken into account. Each semester including 4-6 courses, balancing between 1-2 general education courses and major courses.\n\
\n\
Please format the schedule as a dictionary, with each key representing a semester and its value being a list of courses to be taken that semester.\n\
The next prompt is a sample output. Do not copy the courses course by course.\
"""

schedule_sample_output = "{\n\
    \"Semester X\": [\n\
        \"COURSE XXX\",\n\
        \"COURSE XXX\",\n\
        \"COURSE XXX\",\n\
        \"COURSE XXX\"\n\
    ],\n\
    }"



chat_completion = client.chat.completions.create(
    messages=[

        {"role": "system", "content": prompt},
        {"role": "system", "content": schedule_sample_output}

    ],
    model = "gpt-3.5-turbo"
)

schedule = chat_completion.choices[0].message.content


schedule_dict = json.loads(schedule)
print(schedule_dict)
