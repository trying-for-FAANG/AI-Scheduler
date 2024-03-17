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
  #  "NATURAL SCIENCE ELECTIVE (GN)": [],  # Natural Science Elective
 #  "FOREIGN LANGUAGE Level 2 Proficiency": [],  # Second level proficiency in a foreign language
  #  "COMPUTER SCIENCE ELECTIVE": [],  # Elective courses in Computer Science
  #  "CMPSC / CMPEN 4XX": [],  # Advanced-level Computer Science / Computer Engineering courses
  #  "DEPARTMENT LIST ELECTIVE": []  # Elective courses listed by the department
}

four_credit = ["MATH 140", 'MATH 141', 'PHYS 211', 'MATH 230', 'CMPEN 270', 'PHYS 212', 'Foreign Language']

priorty = ['CMPSC 131', 'CMPSC 132', 'MATH 140', 'MATH 141', 'PHYS 211', 'ENG 015']

general_education = {
            'GWS': 9,
            'GA': 3,
            'GHW': 3,
            'GH': 3,
            'GS': 3,
            'GN': 9,
            'Inter-Domain': 6,
            'World-Language': 6,
            'Non-CMPSC 400': 6,
            'Department (Engineering) Electives': 10,
            'CMPSC_Electives': 6
        }

CMPSC_Electives = {
    'CMPEN 362': {'Description': "Communication Networks", 'Prereq': ['CMPEN 270', 'STAT 318-c']},
    'CMPEN 431': {'Description': 'Introduction to Computer Architecture', 'Prereq': ['CMPEN 331']},
    'CMPEN 454': {'Description': 'Fundamentals of Computer Vision', 'Prereq': ['MATH 230', 'MATH 220']},
    'CMPSC 442': {'Description': 'Artificial Intelligence', 'Prereq': ['CMPSC 221', 'CMPSC 465-c']},
    'CMPSC 443': {'Description': 'Introduction to Computer and Network Security', 'Prereq': ['CMPEN 362', 'CMPSC 473-c']},
    'CMPSC 444': {'Description': 'Secure Programming', 'Prereq': ['CMPSC 221']},
    'CMPSC 450': {'Description': 'Concurrent Scientific Programming', 'Prereq': ['CMPSC 131', 'MATH 220', 'MATH 230']},
    'CMPSC 451': {'Description': 'Numeric Computations', 'Prereq': ['CMPSC 131, MATH 230']},
    'CMPSC 455': {'Description': 'Introduction to Numerical Analysis I', 'Prereq': ['CMPSC 131', 'MATH 220', 'MATH 230']},
    'CMPSC 456': {'Description': 'Introduction to Nuneriacal Analysis II', 'Prereq': ['MATH 455']},
    'CMPSC 458': {'Description': 'Fundamentals of Computer Graphics', 'Prereq': ['CMPSC 311', 'MATH 220', 'MATH 230']},
    'CMPSC 467': {'Description': 'Factorization and Primality Testing', 'Prereq': ['CMPSC 360']},
    'CMPSC 471': {'Description': 'Introductions to Compiler Construction', 'Prereq': ['CMPSC 461']},
    'CMPSC 475': {'Description': 'Applications Programming', 'Prereq': ['CMPSC 221', 'CMPSC 311', 'CMPSC 465']},
    'EE 456': {'Description': 'Introduction to Neural Networks', 'Prereq': ['CMPSC 131', 'MATH 220']},
}



gened_cred = '45'
major_cred = '82'
