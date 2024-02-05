def add_total_marks(students):
    for student in students:
        total_marks = sum(student["subject_mark"].values())
        # Add total marks to the dictionary
        student["Total_mark"] = total_marks
    return students

# Input data
students = [
    {"name": "Arun", "subject_mark": {"maths": 98, "Science": 89, "Social": 79, "Tamil": 98, "English": 67}},
    {"name": "Bhuvan", "subject_mark": {"maths": 90, "Science": 97, "Social": 89, "Tamil": 78, "English": 60}},
    {"name": "Rajesh", "subject_mark": {"maths": 70, "Science": 94, "Social": 99, "Tamil": 85, "English": 80}}
]

result = add_total_marks(students)
print(result)
