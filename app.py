# app.py
from flask import Flask, jsonify, render_template

app = Flask(__name__)

# 仮のデータ（後でデータベースに置き換えてもOK）
tasks = [
    {"id": 1, "title": "Gitの演習をする", "done": False},
    {"id": 2, "title": "Flaskを復習する", "done": True},
]

# ★画面（HTML）を返すルート。これがないとブラウザで404になる
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    return jsonify({"tasks": tasks})

@app.route("/api/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task)

if __name__ == "__main__":
    app.run(debug=True)