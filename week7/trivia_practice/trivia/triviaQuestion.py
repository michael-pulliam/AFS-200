import requests

class TriviaQuestion:
    def __init__(self, question, category, difficulty_level, correct_answers, incorrect_answers, id):
        self.question=question
        self.category=category
        self.difficulty_level=difficulty_level
        self.correct_answers=correct_answers
        self.incorrect_answers=incorrect_answers
        self.id=id
        
    def 