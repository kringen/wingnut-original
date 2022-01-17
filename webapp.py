import redis
from rq import Queue, Connection
from flask import Flask, render_template, Blueprint, jsonify, request
import tasks
import rq_dashboard
import yaml
import logging
import os

logging.basicConfig(level=logging.WARNING)

cwd = os.path.dirname(__file__)
config_file = os.path.join(cwd,"wingnut.yaml")

with open(config_file, "r") as configfile:
            config = yaml.safe_load(configfile)
redis_url = config["webapp"]["redis_url"]
port = config["webapp"]["port"]
ip_address = config["webapp"]["ip_address"]
debug_bool = config["webapp"]["debug"]

app = Flask(
        __name__,
        template_folder="./ui/templates",
        static_folder="./ui/static"

    )


app.config.from_object(rq_dashboard.default_settings)
app.register_blueprint(rq_dashboard.blueprint, url_prefix="/rq")

@app.route("/", methods=["GET"])
def home():
    return render_template("main/home.html")

@app.route("/tasks", methods=["POST"])
def run_task():
    queue = request.form["queue"]
    qualifier = request.form["qualifier"]
    with Connection(redis.from_url(redis_url)):
        q = Queue()
        task = q.enqueue(tasks.create_task, queue, qualifier)
    response_object = {
        "status": "success",
        "data": {
            "task_id": task.get_id()
        }
    }
    return jsonify(response_object), 202

@app.route("/tasks/<task_id>", methods=["GET"])
def get_status(task_id):
    with Connection(redis.from_url(redis_url)):
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

@app.route("/configuration", methods=["GET"])
def get_configuration():
    response_object = {
        "status": "success",
        "data": config
    }
    return jsonify(response_object)

@app.route("/diagnostics", methods=["GET"])
def get_diagnostics():
    r = redis.Redis()

    diagnostics = {}
    diagnostics["power_level"] = "{} %".format(r.get("power_level").decode("utf-8"))
    diagnostics["temperature"] = "{} C&deg;".format(r.get("temperature").decode("utf-8"))
    diagnostics["free_memory_mb"] = "{} MB".format(r.get("free_memory_mb").decode("utf-8"))
    diagnostics["free_disk_space"] = "{} GB".format(r.get("free_disk_space").decode("utf-8"))

    response_object = {
        "status": "success",
        "data": {
            "diagnostics": diagnostics
        }
    }
    return jsonify(response_object)

@app.route('/api/entities', methods=['GET', 'POST'])
def entities():
    if request.method == "GET":
        return {
            'message': 'This endpoint should return a list of entities',
            'method': request.method
        }
    if request.method == "POST":
        return {
            'message': 'This endpoint should create an entity',
            'method': request.method,
		'body': request.json
        }

@app.route('/api/entities/<int:entity_id>', methods=['GET', 'PUT', 'DELETE'])
def entity(entity_id):
    if request.method == "GET":
        return {
            'id': entity_id,
            'message': 'This endpoint should return the entity {} details'.format(entity_id),
            'method': request.method
        }
    if request.method == "PUT":
        return {
            'id': entity_id,
            'message': 'This endpoint should update the entity {}'.format(entity_id),
            'method': request.method,
		'body': request.json
        }
    if request.method == "DELETE":
        return {
            'id': entity_id,
            'message': 'This endpoint should delete the entity {}'.format(entity_id),
            'method': request.method
        }

if __name__ == "__main__":
    app.run(host=ip_address,debug=debug_bool)



    
