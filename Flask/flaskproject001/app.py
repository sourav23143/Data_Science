from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)


# #In your code, __name__ is a special built-in Python variable.

# If you run app.py directly, __name__ is set to "__main__".
# If you import app.py into another script, __name__ is set to "app".