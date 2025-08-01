from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('dashboard.html')

@app.route('/Calculator.html')
def calculator():
    return render_template('Calculator.html')

@app.route('/Currency_Con.html')
def currency_converter():
    return render_template('Currency_Con.html')

@app.route('/rps.html')
def rock_paper_scissors():
    return render_template('rps.html')

@app.route('/Registration.html')
def registration():
    return render_template('Registration.html')

if __name__ == '__main__':
    app.run(debug=True)
