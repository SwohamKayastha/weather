Weather API Project


Description

This Python project utilizes the OpenWeatherMap API to fetch and display weather data for a specified location. The project includes functionalities to retrieve current weather, forecast, and various weather metrics.


Features

1.Fetch current weather data for a specific city
2.Retrieve weather forecast for the next 5 days
3.Display weather metrics such as temperature, humidity, and wind speed


Installation

To install and run this project, follow these steps:

Clone the repository:
  git clone https://github.com/your-username/weather-api-project.git
  
Navigate to the project directory:
  cd weather-api-project
  
Create a virtual environment (optional but recommended):
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
  
Install dependencies:
  pip install -r requirements.txt
  
Configuration
  Obtain an API key from OpenWeatherMap.

Create a .env file in the project directory and add your API key:

plaintext

OPENWEATHER_API_KEY=your_api_key_here
Usage
To use this project, run the main.py script with the desired city name:


python main.py --"City Name"
Example:

python main.py -- "New York"

The script will display the current weather and forecast for the specified city.

Example Output
Data : 40.7127281 & -74.0060152
Weather : Clear
JSON Format - main: {'temp': 300.86, 'feels_like': 300.51, 'temp_min': 298.12, 'temp_max': 303.31, 'pressure': 1003, 'humidity': 39}
Temperature: 27.710000000000036
Minimum Temperature: 24.970000000000027  &  Maximum Temperature: 30.160000000000025
Feels like - 27.360000000000014

Contributing
Contributions are welcome! Please check the contribution guidelines.

Acknowledgements
OpenWeatherMap for providing the weather data API.
