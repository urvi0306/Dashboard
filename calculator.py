from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    num1 = float(data['num1'])
    num2 = float(data['num2'])
    operator = data['operator']
    
    try:
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2 if num2 != 0 else 'Cannot divide by zero'
        else:
            result = 'Invalid operator'
    except Exception as e:
        result = f'Error: {str(e)}'

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
