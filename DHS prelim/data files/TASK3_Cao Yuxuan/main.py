import flask
from flask import request, render_template
import sqlite3

app = flask.Flask(__name__)


def get_results(nric):
    db = sqlite3.connect('ballot.db')
    db.row_factory = sqlite3.Row
    cursor = db.execute('SELECT ballot_result FROM Results WHERE nric=?', (nric,))
    ballot_result = cursor.fetchone()[0]
    cursor.close()
    cursor = db.execute("SELECT Name.names as name, Results.ballot_result as ballot_result FROM Name, Results WHERE Results.nric=Name.nric AND Results.group_id=(SELECT group_id FROM Results WHERE nric=?)", (nric,))
    group_result = cursor.fetchall()
    cursor.close()
    db.close()
    print(group_result)
    return ballot_result, group_result


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('home.html')
    elif request.method == 'POST':
        nric = request.form['nric']
        ballot_result, group_result = get_results(nric)
        if not ballot_result:
            return '<h1>Invalid NRIC</h1>'
        return render_template('dashboard.html', ballot_result=ballot_result, group_result=group_result)
        


app.run(debug=True, port=5000)