# Defines a new class called Question
class Question:
    #  The text attribute stores the text of the question, and the answer attribute stores the correct answer to the question
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
