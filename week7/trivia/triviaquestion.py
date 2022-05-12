from dataclasses import dataclass
import random

@dataclass
class TriviaQuestion:
    question: str
    category: str
    difficulty_level: str
    correct_answer: str
    incorrect_anwser: list
    id: int
    
    def get_question(self):
        return self.question
        
    def get_category(self):
        return self.category 
        
    def get_difficulty_level(self):
        return self.difficulty_level
        
    def get_correct_answer(self):
        return self.correct_answer
        
    def get_incorrect_anwser(self):
        return self.incorrect_anwser
        
    def get_id(self):
        return self.id
        
    def __str__(self):
        return f'{self.question} {self.category}'
    
    def getShuffledAnswers(self):
        all_answers= []
        for incorrect in self.incorrect_anwser:
            all_answers.append(incorrect)
        all_answers.append(self.correct_answer)
        random.shuffle(all_answers)
        return all_answers
        
        
# test = TriviaQuestion("hello world", 'poker hard')
# print(test)