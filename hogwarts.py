# students = ["Hermione","Harry","Ron"]

# print(students[0])
# print(students[1])
# print(students[2])

 ### for loops ###
# for student in students :
#     print(student)

###  len() ###
# for i in range(len(students)):
#     print(i+1, students[i])
    
# houses = ["Gryffindor","Gryffindor","Gryffindor""Slytherin"]
students = {"Hermione":"Gryffindor",
            "Harry":"Gryffindor",
            "Ron":"Gryffindor",
            "Draco":"Slytherin"}

# print(students["Hermione"])
# print(students["Harry"])

### for loops 
# for student in students:
#     print(student, students[student],sep=", ")

students = [
    {"name":"Hermione:","house":"Gryffindor","patronus":"otter"},
    {"name":"Harry","house":"Gryffindor","patronus":"Stag"},
    {"name":"Ron","house":"Gryffindor","patronus":"Jack Russell terrier"},
    {"name":"Draco","house":"Slytherin","patronus":None}
]

for student in students:
    # print(student["name"],student["house"],student["patronus"],sep=",")