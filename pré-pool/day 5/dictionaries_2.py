# TASK 2
# In your student dictionary, add a units key.
# The value associated to units is an array of 3 elements.
# Each element of this array is a dictionary of 3 keys: name, credits, grade:

student = {"name": "mohamed", "academic_year": 3}

student["units"] = [{"name": "Java", "credits" :2 ,"grade": "A"},
                    {"name": "CSS", "credits" :4 ,"grade": "C"},
                    {"name": "Javascrip", "credits" :7 ,"grade": "D"}
                    ]

print(student)