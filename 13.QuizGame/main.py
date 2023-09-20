from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

print("\nWelcome to the quiz game!\n")

# Creates a list of Question objects from the question_data data.
# For each question in the data, the code creates a new Question object with the question text and the correct answer.
# The new Question object is then added to the question_bank list
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Creates a new QuizBrain object, passing in the question_bank list as an argument
quiz = QuizBrain(question_bank)

# Starts a loop that will continue to run as long as the QuizBrain object still has questions to ask
# In each iteration of the loop, the code calls the next_question() method on the QuizBrain object
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
