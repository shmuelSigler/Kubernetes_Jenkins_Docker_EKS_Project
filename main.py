import os
import requests
from datetime import datetime
from flask import Flask, render_template, request, send_file
import pycountry
from dotenv import load_dotenv
import socket
import json
from datetime import datetime

app = Flask(__name__)
# if templates folder moved to outside of app folder then use the following to tell flask to look in the appropriate level of the directory hierarchy
#     app = Flask(__name__, template_folder='../templates')
load_dotenv()

weather_data = {}
history_file = "history_data.json"


# Define a template context processor
@app.context_processor
def inject_variables():
    # Define the variable you want to pass to the template
    bg = os.getenv('BG_COLOR')

    # Return a dictionary with the variable(s) you want to pass
    return dict(bg=bg)

def name_to_cord(location):
    """
    receive user input from form_page
    sends the reacived long and lat to cord_to_weather which returns the actual weather data
    returns the response
    """
    res = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid={os.getenv("key")}').json()
    if not res or 'cod' in res:
        return False

    weather_data['lat'] = res[0]["lat"]
    weather_data['lon'] = res[0]["lon"]
    weather_data['name'] = res[0]["name"]
    weather_data['country'] = pycountry.countries.get(alpha_2=res[0]["country"]).name
    return True


def cord_to_weather(lat, lon):
    """
    reacives cords from name_to_cord and returns the actual weather response
    """
    res = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}"
                       f"&exclude=hourly,minutely,current&units=metric&appid={os.getenv('key')}").json()
    weather_data['daily'] = res['daily'][1:8]


def ensure_history_file_exists():
    if not os.path.exists(history_file):
        with open(history_file, 'w') as file:
            json.dump([], file)


def load_history_data():
    if os.path.exists(history_file):
        with open(history_file, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []


def save_history(city):
    # Ensure the existence of the history file
    ensure_history_file_exists()

    # Load existing history data
    history_data = load_history_data()

    # Create a dictionary with the relevant information
    query_data = {
        'date': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        'city': city
    }

    # Append the query data to the history
    history_data.append(query_data)

    # Save the updated history data to the file
    with open(history_file, 'w') as file:
        json.dump(history_data, file)


@app.route("/", methods=['GET'])
def form_page():
    return render_template("weather.html", host=socket.gethostname())


@app.route("/", methods=['POST'])
def weather():
    form = request.form
    invalid_input = name_to_cord(form['location'])
    if not invalid_input:
        return render_template("weather.html", error=True)

    cord_to_weather(weather_data['lat'], weather_data['lon'])

    for item in weather_data['daily']:
        for key, val in item.items():
            if key == 'dt':
                item['dt'] = datetime.fromtimestamp(item['dt']).date()
    save_history(weather_data['name'])

    return render_template("weather.html", name=weather_data["name"], latitude=weather_data['lat'],
                           longitude=weather_data['lon'], country=weather_data['country'], daily=weather_data['daily'], error=False, host=socket.gethostname())


@app.route("/history")
def history():
    return render_template('history.html')


@app.route('/history/download')
def download():
    return send_file(history_file, as_attachment=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
    # flask --app main --debug  run
