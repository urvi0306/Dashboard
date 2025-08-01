from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Static currency rates (can be updated or replaced with a live API)
rates = {
    "USD": {"INR": 83, "EUR": 0.92, "JPY": 160},
    "INR": {"USD": 0.012, "EUR": 0.011, "JPY": 1.93},
    "EUR": {"USD": 1.09, "INR": 90.5, "JPY": 173.5},
    "JPY": {"USD": 0.0063, "INR": 0.52, "EUR": 0.0058}
}

@app.route('/')
def home():
    return render_template('Currency_Con.html')  # Make sure this file has your HTML

@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    amount = float(data['amount'])
    from_currency = data['from']
    to_currency = data['to']

    if from_currency == to_currency or amount <= 0:
        return jsonify({"error": "Invalid input"})

    rate = rates.get(from_currency, {}).get(to_currency)
    if not rate:
        return jsonify({"error": "Conversion rate not available"})

    result = round(amount * rate, 2)
    return jsonify({"converted": result})

if __name__ == '__main__':
    app.run(debug=True)
