from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

test_number = 0

@app.route("/my_function", methods=['POST'])
def do_something():
    print('called do_something')
    global test_number 
    test_number += 1
    return 'yeet ' + str(test_number)