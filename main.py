from flask import *

app = Flask(__name__)


@app.route('/')
def lists():
    return render_template("list.html")


@app.route('/items', methods=['POST', 'GET'])
def items():
    if request.method == "POST":
        result = request.form
        return render_template('items.html', result=result)


if __name__ == '__main__':
    app.debug = True
    app.run()

