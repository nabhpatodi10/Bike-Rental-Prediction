# Bike-Rental-Prediction

This is a FastAPI web application designed to predict the number of bicycle rentals based on various weather and seasonal factors. The application leverages a Linear Regression machine learning model (`Model.pkl`) to make predictions, and uses a simple HTML frontend powered by Jinja2 templates.

## Features

- **FastAPI Web Framework**: This project uses FastAPI for the backend, ensuring high performance and ease of development.
- **Machine Learning**: A Linear Regression model (`Model.pkl`) is used to predict the number of bicycle rentals.
- **HTML Frontend**: The app provides a user-friendly form to input the necessary weather and seasonal data, and displays the predicted rental count.
- **Jinja2 Templating**: Templates are used to render the frontend dynamically.
- **Static Files Support**: Images and other static files are supported using FastAPI’s `StaticFiles`.

## Prerequisites

Before running this application, ensure you have the following:

- **Python 3.7+**
- **Joblib** (for loading the trained model)
- **FastAPI** and **Uvicorn** (for running the web app)
- **Pandas** (for data handling)
- **Scikit-learn** (for model inference)

## Installation

1. Clone the repository:

    ```bash
    https://github.com/nabhpatodi10/Bike-Rental-Prediction.git
    cd Bike-Rental-Prediction
    ```

2. Install the required dependencies:

    ```bash
    pip install fastapi uvicorn joblib pandas scikit-learn
    ```

3. Ensure the `Model.pkl` file is available in the project root directory. This file contains the pre-trained model used for predictions.

4. Set up the directory structure as follows:

    ```
    your-repository/
    ├── main.py
    ├── Model.pkl
    ├── static/
    │   └── (your static files like images)
    └── templates/
        ├── index.html
        └── readings.html
    ```

## Usage

To run the FastAPI application, use the following command:

```bash
uvicorn main:app --reload
```

This will start the application on `http://127.0.0.1:8000`. Navigate to that URL in your browser to access the form where you can input the weather and seasonal data for predictions.

## Endpoints

### `/`
- **Method**: `GET`
- **Description**: The root route that serves the home page with the input form for users to submit weather and seasonal data.

### `/readings`
- **Method**: `POST`
- **Description**: Accepts form data, runs the prediction model on the input, and returns the predicted number of bicycle rentals.

## Form Fields

The form on the home page accepts the following fields:
- `season`: The season of the year (e.g., 1 for winter, 2 for spring, etc.).
- `year`: The year (e.g., 0 for 2011, 1 for 2012).
- `month`: The month of the year (1-12).
- `holiday`: Boolean field indicating whether the day is a holiday.
- `weekday`: The day of the week (0-6).
- `workingday`: Boolean field indicating if the day is a working day.
- `weather_situation`: Categorical value representing the weather (e.g., 1 for clear, 2 for mist, etc.).
- `temperature`: The normalized temperature in Celsius.
- `feels_like_temperature`: The normalized "feels-like" temperature in Celsius.
- `humidity`: The humidity percentage.
- `windspeed`: The wind speed in km/h.

## Prediction

After submitting the form, the application will use the trained machine learning model to predict the number of bicycle rentals based on the input data. The prediction is displayed on a results page (`readings.html`).

## File Structure

- **`main.py`**: The main FastAPI application script.
- **`Model.pkl`**: Pre-trained machine learning model used for predictions.
- **`static/`**: Directory for static files (like images).
- **`templates/`**: Directory for HTML templates (`index.html` and `readings.html`).

## License

This project is licensed under the MIT License.
