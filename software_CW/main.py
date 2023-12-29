from flask import Flask, render_template, request, url_for, flash, jsonify, redirect
from flask_cors import CORS


app = Flask(__name__)

# see https://flask-cors.readthedocs.io/
# run pip install -U flask-cors
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}
            ]

@app.route('/')
def index():
    return render_template('index.html', messages=messages)


@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        # get the form data
        username = request.form['username']
        password = request.form['password']

        # validate the data input
        if not username:
            flash('Title is required!')
        elif not password:
            flash('Password is required!')
        else:
            # do something with the data, e.g. insert into a database
            messages = ({'username': username, 'content': 'account created sucessfully'})
            # return redirect(url_for('index'))
            return jsonify(messages)

    if request.method == 'GET':
        # return jsonify({'username': request.form['username'], 'password':request.form['password']})
        args = request.args
        params = ((args.to_dict()))
        # good security practice is to never print the contents of passwords!
        print(args.get("username"))
        return jsonify({'username':args.get("username")})
    # return render_template('create.html')
    return {}