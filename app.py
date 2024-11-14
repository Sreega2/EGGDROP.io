from flask import Flask, render_template, session, redirect, url_for, request
import random
import json

# Создаем Flask приложение
app = Flask(__name__)

# Ключ для работы с сессиями
app.secret_key = 'secret_key_for_session'

# Загрузка данных о кейсах и скинах из JSON файла
def load_items():
    with open('data/items.json', 'r', encoding='utf-8') as f:
        return json.load(f)

items_data = load_items()

@app.route('/')
def index():
    # Главная страница с кейсами
    return render_template('index.html', cases=items_data['cases'])

@app.route('/case/<case_id>', methods=['GET', 'POST'])
def case_page(case_id):
    # Страница открытия кейса
    case = next((case for case in items_data['cases'] if case['id'] == case_id), None)
    if case:
        if request.method == 'POST':
            # Случайный выбор предмета при открытии кейса
            skin = random.choice(case['skins'])
            session['inventory'] = session.get('inventory', []) + [skin]
            session['opened_cases'] = session.get('opened_cases', 0) + 1
            return render_template('case.html', case=case, skin=skin)
        return render_template('case.html', case=case)
    else:
        return "Кейс не найден", 404

if __name__ == '__main__':
    app.run(debug=True)
