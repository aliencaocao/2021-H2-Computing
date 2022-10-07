import flask
from flask import render_template
import sqlite3

app = flask.Flask(__name__)
app.root_path = 'Task_4_4/'  # treat this folder as root dir to access subfolders within it


def connect_db(path):
    db = sqlite3.connect(path)
    db.row_factory = sqlite3.Row
    return db


def fetch():
    db = connect_db('LIBRARY.db')
    cursor = db.execute('SELECT Member.FamilyName as family_name, Member.GivenName as given_name, Book.Title as title FROM Book, Member, Loan WHERE Loan.Returned="FALSE" AND Loan.MemberNumber=Member.MemberNumber AND Loan.BookID=Book.BookID')
    results = cursor.fetchall()
    return results


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', results=fetch())


if __name__ == '__main__':
    app.run(debug=True)