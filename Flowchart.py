#HACKPSU AI Schedule Advisor
cmpsc_courses = {

    # format
    # course: optional equivalent course, prerequisites, semester

    "CMPSC 131": ["MATH 140-c"],  # Introduction to Programming with Python
    "CMPSC 132": ["CMPSC 131"],  # Advanced Programming with Python
    "CAS 100 A/B": [],  # Effective Speech
    "ENGL 015": [],  # Rhetoric and Composition
    "MATH 140": [],  # Calculus With Analytic Geometry I
    "CMPSC 111": [],  # Introductory Seminar in Computer Science
    "MATH 141": ["MATH 140"],  # Calculus With Analytic Geometry II
    "CMPSC 221": ["CMPSC 132"],  # Object Oriented Programming with Web-Based Applications
    "MATH 220": ["MATH 140"],  # Matrices
    "CMPSC 311": ["CMPSC 221"],  # Introduction to Systems Programming
    "CMPSC 465": ["CMPSC 360"],  # Data Structures and Algorithms
    "CMPSC 360": ["CMPSC 132"],  # Discrete Mathematics for Computer Science
    "STAT 318": ["MATH 141"],  # Elementary Probability
    "ENGL 202C": ["ENGL 015", "4"],  # Technical Writing
    "STAT 319": ["STAT 318"],  # Elementary Statistics
    "PHYS 211": ["MATH 140-c"],  # General Physics: Mechanics
    "MATH 230": ["MATH 141"],  # Calculus and Vector Analysis
    "CMPSC 461": ["CMPSC 360", "CMPSC 360"],  # Programming Language Concepts
    "CMPSC 464": ["CMPSC 465"],  # Introduction to the Theory of Computation
    "PHYS 212": ["PHYS 211", "MATH 141-c"],  # General Physics: Electricity and Magnetism
    "CMPEN 270": ["PHYS 212-c"],  # Digital Design: Theory and Practice
    "CMPEN 331": ["CMPEN 270", "CMPSC 131"],  # Computer Organization and Design
    "CMPSC 473": ["CMPSC 311", "CMPEN 331"],  # Operating Systems Design and Construction
    "CMPSC 483W": ["-CMPSC 431W","CMPSC 465"],  # Software Design
    "CMPSC 431W": ["-CMPSC 483W","CMPSC 221", "ENGL 202C"], # Database Management Systems
    "NATURAL SCIENCE ELECTIVE (GN)": [],  # Natural Science Elective
    "FOREIGN LANGUAGE Level 2 Proficiency": [],  # Second level proficiency in a foreign language
    "COMPUTER SCIENCE ELECTIVE": [],  # Elective courses in Computer Science
    "CMPSC / CMPEN 4XX": [],  # Advanced-level Computer Science / Computer Engineering courses
    "DEPARTMENT LIST ELECTIVE": [],  # Elective courses listed by the department
    "SUPPORTING COURSE": [],  # Courses that support the major
    "GHW": [],  # General Health and Wellness
}

class GeneralEducation:

    def __init__(self):
        self.dictionary = {
            'GQ': [0, 6],
            'GWS': [0, 9],
            'GA': [0, 3],
            'GHW': [0, 3],
            'GH': [0, 3],
            'GS': [0, 3],
            'GN': [0, 6],
            'Inter-Domain': [0, 6],
            'World-Language': [0, 6]
        }

class ComputerScienceDegree:

    def __init__(self):
        self.gened_cred = 45
        self.major_cred = 106
        self.required = []
        for key in cmpsc_courses:
            self.required.append(key)
        print(self.required)

if __name__ == '__main__':
    c = ComputerScienceDegree()