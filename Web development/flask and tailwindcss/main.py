from flask import Flask, render_template

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

if __name__ == "__main__":
    app.run(debug = True)