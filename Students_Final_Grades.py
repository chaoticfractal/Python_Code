"""
This a little script that will take 3 dictonaries of Students name that contain lists of
objects like homework scores, tests scores etc. that are then taken by funcitons to calculate final grade and 
averages. 
"""



lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}


#This function gets the "numbers" from each list and performs an average fuction
def average(numbers):
    total = float(sum(numbers))
    return total/len(numbers)
    
#This fuction takes in the dictonaries of each student and calc. the average
#of each of the lists
def get_average(student):
    homework = float(average(student["homework"])) * 0.1
    quizzes = float(average(student["quizzes"])) * 0.3
    tests = float(average(student["tests"])) * 0.6
    return homework + quizzes + tests
    
#This function returns the final average of each student
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print get_letter_grade(get_average(lloyd))
print get_letter_grade(get_average(alice))
print get_letter_grade(get_average(tyler))

students=[lloyd, alice, tyler]

#This functions gets the entire class average
#It takes in the new list that contains the average grade of each student and 
#Calc. the total average of the 3
def get_class_average(students):
    results=[]
    for student in students:
        results.append(get_average(student))
    return average(results)
    
print get_class_average(students)
print get_letter_grade(get_class_average(students))
    