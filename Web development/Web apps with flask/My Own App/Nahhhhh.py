from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/export', methods=['GET', 'POST'])
def export_fruits():
    if request.method == 'POST':
        fruit_name = request.form['fruit_name']
        quantity = request.form['quantity']
        destination = request.form['destination']

        # Process the exported items here
        with open('exported_items.txt', 'a') as file:
            file.write(f"{fruit_name},{quantity},{destination}\n")

        # Redirect to a success page or display a success message
        return redirect('/export/success')

    return render_template('export.html')

@app.route('/export/success')
def export_success():
    return "Export successful!"

@app.route('/imported_items')
def view_imported_items():
    items = []
    with open('exported_items.txt', 'r') as file:
        for line in file:
            values = line.strip().split(',')
            item = {
                'fruit_name': values[0],
                'quantity': int(values[1]),
                'destination': values[2]
            }
            items.append(item)
    return render_template('imported_items.html', items=items)

if __name__ == '__main__':
    app.run()