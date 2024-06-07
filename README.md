Weather API Project


Description
This Python project utilizes the OpenWeatherMap API to fetch and display weather data for a specified location. The project includes functionalities to retrieve current weather, forecast, and various weather metrics.

Features
Fetch current weather data for a specific city
Retrieve weather forecast for the next 5 days
Display weather metrics such as temperature, humidity, and wind speed
Installation
To install and run this project, follow these steps:

Clone the repository:
bash
Copy code
git clone https://github.com/your-username/weather-api-project.git
Navigate to the project directory:
bash
Copy code
cd weather-api-project
Create a virtual environment (optional but recommended):
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Configuration
Obtain an API key from OpenWeatherMap.

Create a .env file in the project directory and add your API key:

plaintext
Copy code
OPENWEATHER_API_KEY=your_api_key_here
Usage
To use this project, run the main.py script with the desired city name:

bash
Copy code
python main.py --city "City Name"
Example:

bash
Copy code
python main.py --city "New York"
The script will display the current weather and forecast for the specified city.

Example Output
plaintext
Copy code
Current weather in New York:
Temperature: 15°C
Humidity: 72%
Wind Speed: 5 m/s

5-day forecast:
Day 1: Temperature: 18°C, Humidity: 70%
Day 2: Temperature: 17°C, Humidity: 65%
...
Contributing
Contributions are welcome! Please check the contribution guidelines.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
OpenWeatherMap for providing the weather data API.
