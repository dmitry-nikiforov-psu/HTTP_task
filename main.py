from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

API_KEY = '6efd5c4d9b0fa6190e25fb5222746c4c'


@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({'error': 'Failed to fetch data from OpenWeatherMap'}), response.status_code

    return jsonify(response.json()), response.status_code


if __name__ == '__main__':
    app.run(debug=True)