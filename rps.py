from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

choices = ['rock', 'paper', 'scissors']

@app.route('/')
def home():
    return render_template('rps.html')  # Your HTML file should be named index.html

@app.route('/play', methods=['POST'])
def play():
    data = request.get_json()
    user_choice = data.get('choice')
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        outcome = "It's a draw!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        outcome = "You win!"
    else:
        outcome = "You lose!"

    return jsonify({
        "user": user_choice,
        "computer": computer_choice,
        "result": outcome
    })

if __name__ == '__main__':
    app.run(debug=True)
