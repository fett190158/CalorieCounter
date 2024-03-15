from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
calories = 0

@app.route('/')
def index():
    return render_template('index.html', calories=calories)

@app.route('/add_calories', methods=['POST'])
def add_calories():
    global calories
    calories += int(request.form['calories'])
    return redirect(url_for('index'))

@app.route('/reset_calories', methods=['POST'])
def reset_calories():
    global calories
    calories = 0
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
