<<<<<<< HEAD
from flask import Flask, render_template
from markupsafe import escape
=======
from flask import Flask
>>>>>>> parent of 8918826 (Dodano nowe pliki)
app = Flask(__name__)


@app.route('/')
def index():
<<<<<<< HEAD
    return render_template('index.html')


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
=======
    return '<h1>Hello WSB! Greetings from Flask!</h1>'
if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> parent of 8918826 (Dodano nowe pliki)
