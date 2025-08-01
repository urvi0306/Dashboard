from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Registration.html')  # Your registration form HTML

@app.route('/submit', methods=['POST'])
def submit():
    fullname = request.form.get('fullname')
    email = request.form.get('email')
    password = request.form.get('password')
    gender = request.form.get('gender')
    dob = request.form.get('dob')

    # Placeholder: print or process the data (save to DB, etc.)
    print("New registration:")
    print(f"Name: {fullname}")
    print(f"Email: {email}")
    print(f"Gender: {gender}")
    print(f"Date of Birth: {dob}")

    return f"<h2>Thanks for registering, {fullname}!</h2><p>Details saved successfully.</p>"

if __name__ == '__main__':
    app.run(debug=True)
