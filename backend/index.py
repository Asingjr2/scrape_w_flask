# python libraries
import datetime
import json

# flask open-source library to handle creation anf presentation of webpage
from flask import (
    Flask,
    redirect,
    render_template,
    jsonify
)


# creating 'app' object that has built in methods that can register endpoints, start server, etc
app = Flask(__name__)
COMPANY_INFO_FILE = 'company.json'

# simulating login route
@app.route('/login')
def login():
    return render_template('login.html')

# simulates bad login credentials and redirect back to login
# similar code exists when forms are submitted to databases, or login credentials are received from somewhere else (bank, ticketmaster, etc)
@app.route('/bad_login')
def bad_login_redirect():
    return redirect('/login')

# simulates html welcome page
@app.route('/')
def homepage():
    today = datetime.datetime.today()
    return render_template('welcome.html', today=today)

# simulates api return json value
@app.route('/api/first_example')
def api_company_info():
    filename = COMPANY_INFO_FILE
    with open(filename) as f:
        data = json.load(f)
    return data

# return message based on user input such as url endpoint api/second_example/123456
@app.route('/api/second_example/<transaction_id>')
def get_sale(transaction_id=0):
  return "The transaction is "+str(transaction_id)

# simulates api return value json based on data being passed by user
# enter a number in the place of fake_id such as api/third_example/100
@app.route('/api/third_example/<fake_id>')
def api_add_10(fake_id):
    new_num = int(fake_id) + 10
    data = {
        "submitted_number": fake_id, 
        "new_num": new_num,
        "message": f"You entered {fake_id} and 10 was added to create {new_num}"
    }
    return jsonify(data)

@app.route('/copy')
def copy_page():
    return render_template('copy.html')


if __name__ == '__main__':
    DEBUG=False
    app.run(debug=DEBUG)
    