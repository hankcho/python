class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

students = [Student("Joe", 0.46), Student("Hank", 0.72), Student("Mark", 0.88)]

student_results = []
for student in students:
    # if student.score >= 0.7:
    #     student_results.append(f"{student.name} passed")
    # else: 
    #     student_results.append(f"{student.name} failed")

   student_results.append(f"{student.name} passed") if student.score >= 0.7 else student_results.append(f"{student.name} failed")     


map_results = list(map(lambda student: f"{student.name} Passed" if student.score >= 0.7 else f"{student.name} Failed", students))

# print (student_results)
print(map_results)


# Challenge
# Use map to mulltiply all these numbers by 2

numbers = [1,2,3,4,5]

