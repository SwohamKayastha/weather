# Weather API Project


## Description

This Python project utilizes the OpenWeatherMap API to fetch and display weather data for a specified location. The project includes functionalities to retrieve current weather, forecast, and various weather metrics.


# Features

1.Fetch current weather data for a specific city
2.Retrieve weather forecast for the next 5 days
3.Display weather metrics such as temperature, humidity, and wind speed


# Installation

To install and run this project, follow these steps:

Clone the repository:
  git clone https://github.com/SwohamKayastha/weather.git
  
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

API_KEY=your_api_key_here

# Usage
To use this project, run the main.py script with the desired city name:


python main.py -->"City Name"
Example:

python main.py -- "Kathmandu"

The script will display the current weather and forecast for the specified city.

Example Output:
Data : 27.708317 & 85.3205817
Weather : Clouds
JSON Format - main: {'temp': 297.34, 'feels_like': 297.98, 'temp_min': 297.34, 'temp_max': 297.34, 'pressure': 1005, 'humidity': 83, 'sea_level': 1005, 'grnd_level': 846}
Temperature: 24.189999999999998
Minimum Temperature: 24.189999999999998  &  Maximum Temperature: 24.189999999999998
Feels like - 24.83000000000004

Contributing
Contributions are welcome! Please check the contribution guidelines.

Acknowledgements
OpenWeatherMap for providing the weather data API.