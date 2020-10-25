# Let we have a dictionary D which contain roll number of students as key and its values
# shall be a list. The list has tuples as its item. Each tuple represents the name of the subject
# and gpa of that subject. You can visualize the data structure as of following:


import itertools
students = {
    "2016-CS-700": [("DSA", 3), ("Algo", 2.5), ("AI", 2.1)],
    "2016-CS-701": [("LA", 3), ("AI", 3.5), ("PF", 2.8)],
    "2016-CS-710": [("DSA", 2.5), ("DB", 3.5), ("AI", 2.4)]
}

# a) Write a program which shall print GPA of all students. Assume all subject have 3 credit
# hours. (with and without using for loop)

# With Loop
for student in students:
    gpa = 0
    for (sub, i) in students[student]:
        gpa += i

    print("(With Loop) Total GPA of Student:", student, "is", gpa,
          "and average is", gpa / (len(students[student])))

# Withouy Loop
gpa_list_student = list(map(lambda item: str(
    sum(list(map(lambda sub: sub[1], students[item])))), students))

student_list = list(map(lambda gpa: gpa, students))
st_number = [0]


def print_gpa(gpa):
    print("(Without Loop) Total GPA of Student",
          student_list[st_number[0]], "is", gpa)
    st_number.append(1)
    st_number.append(sum(st_number))
    st_number.pop(0)
    st_number.pop(0)


gpa_list_student = list(
    map(lambda gpa: print_gpa(gpa), gpa_list_student))


# b) Write a program that print the highest number obtained in DSA (with and without using
# for loop)

# With Lopp
subjects = []
for student in students:
    subjects = [*subjects, *students[student]]
dsa = 0
for subject in subjects:
    if subject[0] == 'DSA' and subject[1] > dsa:
        dsa = subject[1]

print("(With Loop) Highest Number Obtained in DSA:", dsa)

# Without Loop
subjects = []
list(map(lambda item: list(
    map(lambda sub: subjects.append(sub), students[item])), students))

dsa2 = []


def hig(sub):
    if sub[0] == 'DSA':
        dsa2.append(sub[1])


list(map(lambda sub: hig(sub), subjects))
print("(Without Loop) Highest Number Obtained in DSA:", max(dsa2))


# c) Write a program that print the total number of students those have less than 2.5 GPA in
# AI? (with and without using for loop)

# With Loop
subjects = []
for student in students:
    subjects = [*subjects, *students[student]]

numebrOfStudents = 0
for subject in subjects:
    if subject[0] == 'AI' and subject[1] < 2.5:
        numebrOfStudents += 1

print("(With Loop) Total number of students those have less than 2.5 GPA in AI:", numebrOfStudents)

# Without Loop
subjects = []
list(map(lambda item: list(
    map(lambda sub: subjects.append(sub), students[item])), students))

totalStudents = []


def total_student(sub):
    if sub[0] == 'AI' and sub[1] < 2.5:
        totalStudents.append(1)


list(map(lambda sub: total_student(sub), subjects))
print("(Without Loop) Total number of students those have less than 2.5 GPA in AI:",
      sum(totalStudents))
