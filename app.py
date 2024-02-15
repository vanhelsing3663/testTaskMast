from flask import Flask, request, jsonify
from models import create_table_click, get_all, insert_data

app = Flask(__name__)


create_table_click()

@app.route('/add', methods=['POST'])
def add_data():
    try:
        data = request.json
        result = insert_data(data['data'])
        return jsonify({'status': 'success'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
        

@app.route('/get', methods=['GET'])
def get_data():
    try:
        result = get_all()
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)