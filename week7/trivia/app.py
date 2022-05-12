from flask import Flask
from flask import request, render_template
import triviaGame

app = Flask(__name__)

new_trivia_game = triviaGame.TriviaGame()
new_trivia_game.store_questions(new_trivia_game.retrieve_questions(20, 5))

@app.route("/", methods=['GET'])
def questions():

    return render_template('index.html', questions=new_trivia_game.get_questions())

@app.route("/score", methods=['POST'])
def score():
    correct = []
    incorrect = []
    for question in new_trivia_game.get_questions():
        if (request.form.get(str(question.get_id())) == question.get_correct_answer()):
            correct.append(question)
        else:
            incorrect.append(question)
    return render_template('answers.html', answers=new_trivia_game.getAllQuestions(), correctQuestions = correct, incorrectQuestions = incorrect)

# @app.route('/score', methods=['GET'] )
# def score():
#     score_result = triviaGame.TriviaGame()

if __name__ == "__main__":
    app.run()