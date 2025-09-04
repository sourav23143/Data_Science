from flask import Flask, render_template, request, jsonify

#we are using request since in html we have form and for fetching data from form we use it , what user will enter there

#we use jsonify for Postman , what ever data we will pass to test in  Postman, we will be converting that into json format, the result will be in the form of json for that reson we are using this


app = Flask(__name__) #an instance of flask class

@app.route('/')
def view_form():
    return render_template('index.html')


@app.route('/math', methods =['POST'])
def math_ops():
    if(request.method == "POST"):
        ops = request.form['operation']
        num1 = int(request.form['num1'])  #since when we take input bu default it is string
        num2 = int(request.form['num2'])
        if ops == 'add':
            r = num1+num2
            result = "The sum of " +str(num1) +'and ' + str(num2) + "is " + str(r)
        if ops == 'subtract':
            r = num1-num2
            result = "The subtraction of " +str(num1) +'and ' + str(num2) + "is " + str(r)
        if ops == 'multiply':
            r = num1*num2
            result = "The multiplication of " +str(num1) +'and ' + str(num2) + "is " + str(r)
        if ops == 'divide':
            r = num1/num2
            result = "The division of " +str(num1) +'and ' + str(num2) + "is " + str(r)

        return render_template('results.html' , result = result)  #here we are passing the result
    

@app.route('/postman_action', methods =['POST'])
def math_ops1():
    if(request.method == "POST"):
        ops = request.form['operation']
        num1 = int(request.json['num1'])  #since when we take input bu default it is string
        num2 = int(request.json['num2'])
        if ops == 'add':
            r = num1+num2
            result = "The sum of " +str(num1) +'and ' + str(num2) + "is " + str(r)
        if ops == 'subtract':
            r = num1-num2
            result = "The subtraction of " +str(num1) +'and ' + str(num2) + "is " + str(r)
        if ops == 'multiply':
            r = num1*num2
            result = "The multiplication of " +str(num1) +'and ' + str(num2) + "is " + str(r)
        if ops == 'divide':
            r = num1/num2
            result = "The division of " +str(num1) +'and ' + str(num2) + "is " + str(r)

        return jsonify(result)
    
if __name__ == '__main__':
    app.run(host="0.0.0.0")
    
