from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
import time

app = Flask(__name__, static_folder='frontend', static_url_path='')
CORS(app)

DATA_FILE = 'data.json'


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}


def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/api/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'Файл не найден'}), 400

    file = request.files['file']
    if not file.filename.lower().endswith('.json'):
        return jsonify({'error': 'Поддерживаются только JSON файлы'}), 400

    try:
        content = file.read().decode('utf-8')
        new_records = json.loads(content)
    except Exception as e:
        return jsonify({'error': f'Ошибка чтения файла: {str(e)}'}), 400

    if not isinstance(new_records, dict):
        return jsonify({'error': 'Неверный формат. Ожидается объект вида {"тип": [...]}'}), 400

    data = load_data()
    added = {}
    base_ts = int(time.time() * 1000)
    offset = 0

    for type_key, items in new_records.items():
        if not isinstance(items, list):
            continue
        if type_key not in data:
            data[type_key] = []
        added[type_key] = []
        for item in items:
            record = {k: v for k, v in item.items() if k != '_id'}
            record['_id'] = base_ts + offset
            offset += 1
            data[type_key].append(record)
            added[type_key].append(record)

    save_data(data)
    total = sum(len(v) for v in added.values())
    return jsonify({'added': added, 'message': f'Добавлено записей: {total}'})


@app.route('/api/records', methods=['GET'])
def get_records():
    return jsonify(load_data())


if __name__ == '__main__':
    app.run(debug=True, port=5000)
