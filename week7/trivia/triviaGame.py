import requests
import triviaquestion

class TriviaGame():
    def __init__(self):
        self.gameQuestions = []
        
    def get_questions(self):
        return self.gameQuestions
    
    def retrieve_questions(self, category_ID, num_of_questions):
        
        URL = f"https://opentdb.com/api.php?amount={num_of_questions}&category={category_ID}&difficulty=easy&type=multiple"

        try:
            response = requests.get(URL, timeout=5)
            response.raise_for_status()
            response_JSON = response.json()
            return response_JSON
        except requests.exceptions.HTTPError as errh:
            print(errh)
        except requests.exceptions.ConnectionError as errc:
            print(errc)
        except requests.exceptions.Timeout as errt:
            print(errt)
        except requests.exceptions.RequestException as err:
            print(err)
         
    def store_questions(self, json_question_list):
        id = 0
        for current_question in json_question_list['results']:
            
            incorrect_answers = []
            
            for answer in current_question['incorrect_answers']:
                incorrect_answers.append(answer)
                
            new_trivia_question = triviaquestion.TriviaQuestion(
                                    current_question['question'],
                                    current_question['category'],
                                    current_question['difficulty'],
                                    current_question['correct_answer'],
                                    current_question['incorrect_answers'],
                                    id
            )
            id = id + 1
            self.gameQuestions.append(new_trivia_question)
# display_users = triviaquestion.AddressBook()
# json_users_data = getData(25, 'us')

    # def loadGameQuestions(self, category_ID, num_of_questions):
        
    #     URL = f"https://opentdb.com/api.php?amount={num_of_questions}&category={category_ID}&difficulty=easy&type=multiple"
        
    #     try:
    #         response = requests.get(URL, timeout=5)
    #         response.raise_for_status()
    #         response_JSON = response.json()
            
    #         for current_question in response_JSON['results']:
            
    #             incorrect_answers = []
            
    #             for answer in current_question['incorrect_answers']:
    #                 incorrect_answers.append(answer)
                
    #             new_trivia_question = triviaquestion.TriviaQuestion(
    #                                     current_question['category'],
    #                                     current_question['difficulty'],
    #                                     current_question['question'],
    #                                     current_question['correct_answers'],
    #                                     current_question['incorrect_answers']
    #             )
                
    #             self.gameQuestions.append(new_trivia_question)
                
    #     except requests.exceptions.HTTPError as errh:
    #         print(errh)
    #     except requests.exceptions.ConnectionError as errc:
    #         print(errc)
    #     except requests.exceptions.Timeout as errt:
    #         print(errt)
    #     except requests.exceptions.RequestException as err:
    #         print(err) 
            
    #         return response_JSON
