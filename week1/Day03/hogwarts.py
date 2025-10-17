# hogwarts exercise using dictionaries
'''
hogwarts_residents = {
    "Harry Potter": "Gryffindor",
    "Hermione Granger": "Gryffindor",
    "Cedric Diggory": "Hufflepuff",
    "Luna Lovegood": "Ravenclaw",
    "Draco Malfoy": "Slytherin"
}

# print(hogwarts_residents["Draco Malfoy"])

for resident in hogwarts_residents:
    print(resident, hogwarts_residents[resident], sep=" ---> ")

'''

# Dictionary with multiple key value pairs as a list.

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=" - ")
