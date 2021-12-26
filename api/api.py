import redis
from rq import Queue, Connection
from flask import Flask, render_template, Blueprint, jsonify, request
import tasks
import rq_dashboard

app = Flask(
        __name__,
        template_folder="./templates",
        static_folder="./static",
    )

app.config.from_object(rq_dashboard.default_settings)
app.register_blueprint(rq_dashboard.blueprint, url_prefix="/rq")

@app.route("/", methods=["GET"])
def home():
    return render_template("main/home.html")

@app.route("/tasks", methods=["POST"])
def run_task():
    task_type = request.form["type"]
    with Connection(redis.from_url("redis://localhost:6379")):
        q = Queue()
        task = q.enqueue(tasks.create_task, task_type)
    response_object = {
        "status": "success",
        "data": {
            "task_id": task.get_id()
        }
    }
    return jsonify(response_object), 202

@app.route("/mode", methods=["POST"])
def set_mode():
    task_type = request.form["type"]
    with Connection(redis.from_url("redis://localhost:6379")):
        q = Queue("mode")
        task = q.enqueue(tasks.set_mode, task_type)
    response_object = {
        "status": "success",
        "data": {
            "task_id": task.get_id()
        }
    }
    return jsonify(response_object), 202

@app.route("/tasks/<task_id>", methods=["GET"])
def get_status(task_id):
    with Connection(redis.from_url("redis://localhost:6379")):
        q = Queue()
        task = q.fetch_job(task_id)
    if task:
        response_object = {
            "status": "success",
            "data": {
                "task_id": task.get_id(),
                "task_status": task.get_status(),
                "task_result": task.result,
            },
        }
    else:
        response_object = {"status": "error"}
    return jsonify(response_object)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=1)



    
