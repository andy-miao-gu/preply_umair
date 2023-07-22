from flask import Flask, render_template,request

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
@app.route("/pros_cal_data", methods=['POST'])
def hello_world5():
    data = request.form.get("data")
    print(data)

if __name__ == "__main__":
    app.run(debug = True)