# TASK 3
# Create a new directory named grade_weight_mapping.

student = {"name": "mohamed",}
grade_weight_mapping = {"A":4, "B":3, "C":2, "D":1, "E":0}

student["units"] = [{"name": "Java", "credits" :2 ,"grade": "A"},
                    {"name": "CSS", "credits" :4 ,"grade": "C"},
                    {"name": "Javascrip", "credits" :7 ,"grade": "D"}
                    ]

student["total_credits"] = sum(list(map(lambda element: element["credits"], student["units"] )))
Coef_Note = list(map(lambda element: grade_weight_mapping[element["grade"]] * element["credits"], student["units"] ))     # on obtient une liste contenant le produit des notes par leurs coeff

student["gpa"] = sum(Coef_Note) / student["total_credits"]

print(student["total_credits"])
print(student["gpa"])

