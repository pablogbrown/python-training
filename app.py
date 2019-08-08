from flask import Flask, jsonify, request
from flask import abort
import todosqlite
import json


app = Flask(__name__)

@app.route('/todos', methods=['GET'])
def home():
    return jsonify(todosqlite.list_todos())

@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    return jsonify(todosqlite.get_todo(todo_id))

@app.route('/todos', methods=['POST'])
def test():
    json = request.get_json()
    title = json['title']
    description = json['description']
    msg = todosqlite.insert_todo(title,description)
    return jsonify(msg)

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    if todo_id:
        return todosqlite.delete_todo(todo_id)
    else:
        abort(400)

@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    if todo_id:
        json = request.get_json()
        title = json['title']
        description = json['description']
        return todosqlite.update_todo(todo_id, title, description)
    else:
        abort(400)

if __name__ == '__main__':
   app.run()

