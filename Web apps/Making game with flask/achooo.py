from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.py')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        guess_number = int(request.form['guess'])
        message, attempts = guess(target_number, guess_number)
        return render_template('index.html', message=message)
    else:
        target_number, _ = start_game()
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
