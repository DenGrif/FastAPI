from flask import Flask, render_template, request

app = Flask(__name__)

class User:
    def __init__(self, name, city, hobby, age):
        self.name = name
        self.city = city
        self.hobby = hobby
        self.age = age

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        city = request.form['city']
        hobby = request.form['hobby']
        age = request.form['age']

        user = User(name, city, hobby, age)
        return render_template('form.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)