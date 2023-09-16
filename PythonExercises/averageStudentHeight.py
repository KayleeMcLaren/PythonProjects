# Average Height Calculator
# Program that calculates the average student height from a List of heights

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])  # array stores the heights values

total_height = 0
# adds all the heights together
for height in student_heights:
    total_height += height
print(f"total height = {total_height}")  

number_of_students = 0
# adds the number of students together
for student in student_heights:
    number_of_students += 1
print(f"number of students = {number_of_students}")

# calculates the average height
average_height = round(total_height / number_of_students)
print(average_height)
