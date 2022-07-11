import os
import flask
import sqlite3
from flask import render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from datetime import datetime

app = flask.Flask(__name__)


def connect_db(db_path):
    db = sqlite3.connect(db_path)
    db.row_factory = sqlite3.Row
    return db


def fetchlist():
    db = connect_db('todo.db')
    cursor = db.execute(
        'SELECT Todo.ID as id, Todo.Description as desc, Todo.Image as imageURL, Todo.Status as status, Todo.AddOn as addon, Category.name as categoryname FROM Todo, Category where Todo.Category = Category.ID')
    res = cursor.fetchall()
    cursor.close()
    db.close()
    return res


def fetchcats():
    db = connect_db('todo.db')
    cursor = db.execute('SELECT * FROM Category')
    res = cursor.fetchall()
    cursor.close()
    db.close()
    return res


def fetch_item(itemID):
    db = connect_db('todo.db')
    cursor = db.execute(
        'SELECT Todo.ID as id, Todo.Description as desc, Todo.Image as imageURL, Todo.Status as status, Category.name as categoryname FROM Todo, Category where Todo.Category = Category.ID and Todo.ID = ?',
        (itemID,))
    res = cursor.fetchone()  # need fetch 1 here else it will be a list and in Jinja2 have to use for loop to parse
    cursor.close()
    db.close()
    return res


def add_item(request):
    categoryID = request.form['categoryID']
    desc = request.form['description']
    if request.files['photo']:
        image = request.files['photo']
        fname = secure_filename(image.filename)
        image.save(os.path.join('uploads', fname))
    else:
        fname = ''
    db = connect_db('todo.db')
    db.execute('INSERT INTO Todo (Category, Description, Image, Status, AddOn) VALUES (?, ?, ?, ?, ?)', (categoryID, desc, fname, 'Incomplete', str(datetime.now())))
    db.commit()
    db.close()


def edit_item(request):
    ID = request.form['ID']
    categoryID = request.form['categoryID']
    desc = request.form['description']
    status = request.form['status']
    original_image = request.form['original_image']
    if request.files['photo']:
        image = request.files['photo']
        fname = secure_filename(image.filename)
        image.save(os.path.join('uploads', fname))
        if original_image:
            os.remove(os.path.join('uploads', original_image))
    else:
        fname = original_image
    db = connect_db('todo.db')
    db.execute('UPDATE Todo SET Category=?, Description=?, Image=?, Status=? WHERE Todo.ID = ?', (categoryID, desc, fname, status, ID))
    db.commit()
    db.close()


def delete_item(itemID):
    db = connect_db('todo.db')
    db.execute('DELETE FROM Todo where Todo.ID = ?', (itemID,))
    db.commit()
    db.close()


@app.route('/', methods=['GET'])
def home():
    return redirect(url_for('index'))


@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html', todoList=fetchlist())


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('add.html', categories=fetchcats())
    elif request.method == 'POST':
        try:
            add_item(request)
            return f'Added: {request.form["description"]} <a href={url_for("index")}>Back to list</a>'
        except Exception as e:
            return f'Error: {e} <a href={url_for("index")}>Back to list</a>'


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'GET':
        return render_template('edit.html', item=fetch_item(request.args.get('itemID')), categories=fetchcats())
    elif request.method == 'POST':
        try:
            edit_item(request)
            return f'Edited: {request.form["description"]} <a href={url_for("index")}>Back to list</a>'
        except Exception as e:
            return f'Error: {e} <a href={url_for("index")}>Back to list</a>'


@app.route('/delete', methods=['GET'])
def delete():
    try:
        delete_item(request.args.get('itemID'))
        return f'Deleted. <a href={url_for("index")}>Back to list</a>'
    except Exception as e:
        return f'Error: {e} <a href={url_for("index")}>Back to list</a>'


@app.route('/uploads/<filename>', methods=['GET'])
def getfile(filename):
    return send_from_directory('uploads', filename)


if __name__ == '__main__':
    app.run(debug=True)
