from flask import Flask, render_template, request
import random

app = Flask(__name__)
secret_number = random.randint(1, 100)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        try:
            guess = int(request.form["guess"])
            if guess < secret_number:
                message = "Too low! Try again."
            elif guess > secret_number:
                message = "Too high! Try again."
            else:
                message = "🎉 Correct! You guessed the number!"
        except:
            message = "Please enter a valid number."
    return render_template("guessing_game.html", message=message)

if __name__ == "__main__":
    app.run(port=5003,debug=True)
