from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form.get('test_string', '')
    regex_pattern = request.form.get('regex', '')

    # Split the input string into lines
    lines = test_string.split('\n')

    # Find matches in each line using the regex pattern
    matches = []
    for line in lines:
        line_matches = re.findall(regex_pattern, line)
        matches.extend(line_matches)

    # Check if the provided email is valid
    email = request.form.get('email', '')
    email_status = ''
    if email:
        email_pattern = r'^\w+[\w\.-]*@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
        if re.match(email_pattern, email):
            email_status = "valid"
        else:
            email_status = "not valid"
    else:
        email_status = "No email provided"

    return render_template('results.html', matches=matches, email_status=email_status)
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)