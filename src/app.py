from flask import Flask, request, jsonify
from exception import exception_for_routes
from models import create_table_click, get_all, insert_data

app = Flask(__name__)


create_table_click()


@app.route("/add", methods=["POST"])
@exception_for_routes
def add_data():
    data = request.json
    insert_data(data["data"])
    return jsonify({"status": "success"}), 200


@app.route("/get", methods=["GET"])
@exception_for_routes
def get_data():
    result = get_all()
    return jsonify(result), 200


if __name__ == "__main__":
    app.run(debug=True)
