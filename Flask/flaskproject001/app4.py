from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/home')                     #now we can go to url: http://127.0.0.1:5000 and see the message 'Hello, World!'
def hello_home():                          #and when we go to url: http://127.0.0.1:5000/home we will see the message 'Hello, from home_page!'
    return 'Hello, from home_page!'  


@app.route("/<name>")
def user(name):
    return f"Hello, {name}!"
    

@app.route('/home/test')                         #when ever we clicking it we not want output as 'Hello, from home_page!' but we want output to be redirect to home page
def hello_test():                         
    return redirect(url_for('hello_home'))


if __name__ == '__main__':
    app.run(debug=True)