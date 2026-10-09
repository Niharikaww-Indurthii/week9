from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello():
    return '''
        <center>
            <h1>Hello, World!</h1>
            <a href="/register">Go to Registration Page</a>
            <h1>New change did in week three only</h1>
        </center>
    '''


@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
        name = request.form['name']
        return render_template('success.html', name=name)

    return render_template('register.html')


if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000)
