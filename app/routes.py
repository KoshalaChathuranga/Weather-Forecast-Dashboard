# In routes.py
from flask import Blueprint, render_template, request

bp = Blueprint('routes', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    forecast_data = None
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            # Simulate weather data for demonstration
            weather_data = {
                'location': city,
                'temperature': '25',  # Simulated temperature
                'description': 'Sunny',  # Simulated weather description
                'humidity': '70',  # Simulated humidity
                'wind_speed': '5',  # Simulated wind speed
                'icon': 'sunny'  # Simulated weather icon
            }
            
            # Simulate forecast data for demonstration
            forecast_data = [
                {'date': '2024-04-11', 'description': 'Sunny', 'high_temp': '28', 'low_temp': '18', 'icon': 'sunny'},
                {'date': '2024-04-12', 'description': 'Partly Cloudy', 'high_temp': '26', 'low_temp': '17', 'icon': 'partly-cloudy'},
                {'date': '2024-04-13', 'description': 'Rainy', 'high_temp': '22', 'low_temp': '15', 'icon': 'rainy'},
                {'date': '2024-04-14', 'description': 'Cloudy', 'high_temp': '20', 'low_temp': '14', 'icon': 'cloudy'},
                {'date': '2024-04-15', 'description': 'Sunny', 'high_temp': '24', 'low_temp': '17', 'icon': 'sunny'}
            ]
            
    return render_template('index.html', weather_data=weather_data, forecast_data=forecast_data)
