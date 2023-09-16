# High Score
# A program that calculates the highest score from a List of scores

# Creates an array to store the values of each student's scores
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0
# compares the scores together to determine which one is the highest
for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"The highest score in the class is: {highest_score}")
