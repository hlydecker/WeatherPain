# WeatherPain

### Features
Record pain scores (integer values between 0 and 10) along with date, time, and geolocation.
Fetch weather data using date, time, and geolocation from a free weather API provider.
Visualize pain scores and weather variables like temperature, rain, and humidity.
Built with Python, Flask for the backend, SQLite for the database, and Plotly for data visualization.

### How to Run
1. Clone this repository.
2. Create a new python environment using python 3.10. `conda create weatherpain python==3.10`
3. Install the dependencies listed in requirements.txt. `pip install -r requirements.txt`
4. Run `python app.py` to start the Flask server.
5. Access the application at http://localhost:5000.

### Core Classes, Functions, and Files

- `app.py`: Entrypoint for the Flask application.
- `models.py`: Defines the SQLite database models.
- `weather_api.py`: Handles fetching weather data from an external API.
- `forms.py`: Defines Flask-WTF forms for user input.
- `templates/`: Contains HTML files for the frontend.
  - `index.html`: The main page with forms for input and visualization.
- `static/`: Contains CSS and JS files.
- `requirements.txt`: Lists all Python package dependencies.
