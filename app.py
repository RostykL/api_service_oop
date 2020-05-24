from flask import jsonify, render_template
import requests
import config
import models
from container import Container

connex_app = config.connex_app

# Головна сторінка, де відображаються всі тварини
@connex_app.route('/')
def home_page():
    url = 'http://localhost:5000/pets'
    response = requests.get(url)
    data = response.json()
    data_len = len(data)
    return render_template('main.html', data=data, length=data_len)

# сторінка через яку можна приютити тварину
@connex_app.route('/adopt/<id>/')
def adopt_page(id):
    # ініціалізуємо контейнер, який перед тим заімпортили з ioc папки
    container = Container()
    try:
        # беремо ім'я яке має id - id
        name = requests.get("http://0.0.0.0:5000/pets/{0}/".format(id))
        # перевіряємо чи в нас є такий елемент
        if(len(name.json()) >= 1):
            # видаляємо елемент з бази даних через request
            container.adoption(id)
            return render_template('adoptionDone.html', name=name.json()['name'])
        else:
            return render_template('adoptionDone.html', name='No Pet was found by this id')

    except IndexError:
        print("No pets are found")


# Run Server
if __name__ == "__main__":
    connex_app.run(debug=True)
