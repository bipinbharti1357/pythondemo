# # app.py
# from flask import Flask, jsonify, request

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Hello, this is my first API! Home Not found"

# @app.route("/hello")
# def hello():
#     return jsonify({"message": "Hello from Python API"})

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000, debug=True)

# @app.route("/add", methods=["POST"])
# def add():
#     data = request.json
#     a = data["a"]
#     b = data["b"]
#     return jsonify({
#         "result": a + b
#     })

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, request, jsonify

app = Flask(__name__)

# Fake DB (in-memory)
todos = []
next_id = 1


# GET all todos
@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)


# ADD todo
@app.route("/todos", methods=["POST"])
def add_todo():
    global next_id
    data = request.json

    todo = {
        "id": next_id,
        "title": data["title"],
        "done": False
    }
    todos.append(todo)
    next_id += 1

    return jsonify(todo), 201


# UPDATE todo
@app.route("/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    data = request.json

    for todo in todos:
        if todo["id"] == todo_id:
            todo["title"] = data.get("title", todo["title"])
            todo["done"] = data.get("done", todo["done"])
            return jsonify(todo)

    return jsonify({"error": "Todo not found"}), 404


# DELETE todo
@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    global todos
    todos = [t for t in todos if t["id"] != todo_id]
    return jsonify({"message": "Todo deleted"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

