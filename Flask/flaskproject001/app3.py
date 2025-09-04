from flask import Flask
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
    

@app.route('/home/test')               
def hello_test():                         
    return 'Hello, from test page!'


if __name__ == '__main__':
    app.run(debug=True)