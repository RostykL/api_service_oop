from flask import jsonify, render_template
import requests
import config
import models

connex_app = config.connex_app


@connex_app.route('/')
def home_page():
    url = 'http://localhost:5000/product'
    response = requests.get(url)
    data = response.json()
    data_len = len(data)
    return render_template('main.html', data=data, length=data_len)


@connex_app.route('/api/')
def api_page():
    return render_template('api.html')


# Run Server
if __name__ == "__main__":
    connex_app.run(debug=True)
