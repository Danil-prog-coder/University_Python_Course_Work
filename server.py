from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import json
import os
import time

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_FILE = 'data.json'


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}


def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


@app.get('/')
def index():
    return FileResponse('frontend/index.html')


@app.post('/api/upload')
async def upload_file(file: UploadFile = File(...)):
    if not file.filename.lower().endswith('.json'):
        raise HTTPException(status_code=400, detail='Поддерживаются только JSON файлы')

    try:
        content = await file.read()
        new_records = json.loads(content.decode('utf-8'))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f'Ошибка чтения файла: {str(e)}')

    if not isinstance(new_records, dict):
        raise HTTPException(status_code=400, detail='Неверный формат. Ожидается объект вида {"тип": [...]}')

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
    return {'added': added, 'message': f'Добавлено записей: {total}'}


@app.get('/api/records')
def get_records():
    return load_data()


app.mount('/', StaticFiles(directory='frontend', html=True), name='frontend')


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=5000)
