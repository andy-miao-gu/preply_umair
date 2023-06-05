from flask import Flask, render_template, request, redirect, url_for 
import pygame   
app = Flask(__name__) #

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/Exercise')
def exercise():
    return render_template('Exercise.html')

@app.route('/Eexercise')
def eexercise():
    return render_template('Eexercise.html')

@app.route('/more_info')
def More_info():
    return render_template('More_information.html')


@app.route('/submit', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Do something with the form data (e.g. store it in a database)
        return f'{name}!!!, Form submitted successfully!, your message {message} is terrible!'

    return render_template('form.html')

@app.route('/flappy_bird')
def flappy_bird():
    pygame.init()
    screen = pygame.display.set_mode((400, 600))
    # Game code goes here
    pygame.quit()
    return render_template('flappy_bird.html')



if __name__ == '__main__':
    app.run(debug=True) #   debug   logging

 