from flask import Flask, render_template,request,jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/andy")
def hello_world2():
    return render_template("andy.html")

@app.route("/home")
def hello_world3():
    return render_template("home.html")
@app.route("/calculator")
def hello_world4():
    return render_template("calculator.html")

# a function for GET POST requests

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    expression = data['expression']

    try:
        # Evaluate the expression to get the result
        result = eval(expression)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})
    

if __name__ == "__main__":
    app.run(debug = True)