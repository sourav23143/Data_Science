from flask import Flask, render_template, request, redirect, session

app = Flask(__name__) #an instance of flask class

#set a secret key for encrypting session data
app.secret_key = "my_secret_key"


#dictionary to store user and password
users = {
    "sourav": "1234",
    "user2": "password2"
}

#to rendrer the login form
@app.route('/')
def view_form():
    return render_template('login.html')

#Forhandling get request form we can get
#the form inputs value by using args attribute.
#this values after submitting you will see in the urls.
# e.g http://127.0.0.1:5000/handle_get?username=sourav&password=1234
# this exploits our credentials so that's 
#why developers prefer POST request

# #args is a property
# of Flask's request object.
# It contains the query parameters from the URL in a GET request.

# For example, if your URL is:
# http://127.0.0.1:5000/handle_get?username=sourav&password=1234

# You can access username and password using:
# username = request.args['username']
# password = request.args['password']

# args acts like a dictionary for URL parameters.


@app.route('/handle_get', methods = ['GET'])   #here method is mention specifically that it is GET method, where we will fetch info. from server
def handle_get():
    if request.method == 'GET':
        username = request.args['username']
        password = request.args['password']
        print(username, password)
        if username in users and users[username] == password:
            return '<h1>Welcome!!!</h1>'
        else:
            return '<h1>Invalid credentials</h1>'
    else:
        return render_template('login.html')
    

#For handling post request form we can get the form 
#inputs value by using form attribute.
#this values after submitting you will not see in the urls.
@app.route('/handle_post', methods = ['POST'])
def handle_post():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username, password)            #it is not necessary 
        if username in users and users[username] == password:
            return '<h1>Welcome!!!</h1>'
        else:
            return '<h1>Invalid credentials</h1>'
    else:
        return render_template('login.html')
    

if __name__ == '__main__':
    app.run()
        
        