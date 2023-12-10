#!/usr/bin/env python3

from flask import Flask
import pytest 

app = Flask(__name__)

# 1ST README: Your index() view should be routed to at the base URL with /. It should Contain an h1 element that contains the title of this application, "Python Operations with Flask Routing and Views".
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# 2ND README: Your print() view should be routed to at /print/<parameter>. It should display the parameter in the browser. A print_string view should take one parameter, a string. It should print the string in the console and display it in the web browser. Its URL should be of the format /print/parameter.
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

# 3rd README: A count() view should take one parameter, an integer. It should display all numbers in the range of that parameter on separate lines. Its URL should be of the format /count/parameter.
@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = '/n'.join([str(i) for i in range(parameter)])
    #The newline character \n is an escape sequence that represents a line break or a new line.
    return numbers

# 4th README A math() view should take three parameters: num1, operation, and num2. It must perform the appropriate operation on the two numbers in the order that they are presented. The included operations should be: +, -, *, div (/ would change the URL path), and %. Its URL should be of the format /math/<num1>/<operation>/<num2>.

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation , num2):
    result = None
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div":
        result = num1 / num2
    elif operation == "%":
        result = num1 % num2 

    if result is not None:
        return str(result)
    else:
        return "Invalid Operation"
    
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    



if __name__ == '__main__':
    app.run(port=5555, debug=True)
