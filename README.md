
# 2021 Olympics in Tokyo - Medal Prediction

![Olympic Rings](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQo95CICavoc3Zh2dIAFYuYRz8-0WgtbrSeIA&s)

## Overview

This project aims to predict the type of Olympic medal (Gold, Silver, or Bronze) that a country or participant will win based on features such as the discipline and event. The project is built using **FastAPI** and a machine learning model (Random Forest) that processes input features and predicts the medal type. The application is containerized using **Docker** for easy deployment.

## Dataset

The dataset used in this project is from the **2021 Tokyo Olympics** and is available on Kaggle:

[2021 Olympics in Tokyo Dataset - Kaggle](https://www.kaggle.com/datasets/arjunprasadsarkhel/2021-olympics-in-tokyo)

### **Dataset Details**

- **File**: `Tokyo 2021 Olympics Dataset.csv`
- **Size**: 231 KB
- **Features**:
  - **Discipline**: The sport or activity involved (e.g., Athletics, Swimming, Gymnastics).
  - **Event**: The specific event in the discipline (e.g., 100m Sprint, 200m Freestyle).
  - **Country/Team**: The country or team participating in the event.
  - **Medal**: The type of medal won (Gold, Silver, or Bronze).
  - **Gender**: Male or Female participants.
  - **Athlete**: Name of the athlete.
  
### Sample Rows from the Dataset:

| Discipline | Event             | Country/Team | Medal  | Gender | Athlete          |
|------------|-------------------|--------------|--------|--------|------------------|
| Athletics  | 100m Sprint        | USA          | Gold   | Male   | John Doe         |
| Swimming   | 200m Freestyle     | Australia    | Silver | Female | Jane Smith       |
| Gymnastics | Floor Exercise     | Russia       | Bronze | Male   | Ivan Petrov      |

This dataset provides a rich set of features for training a machine learning model to predict the type of medal a participant might win based on their event and discipline.

---

## Project Structure

```
/2021-olympics-in-tokyo
  |-- /templates
      |-- index.html         # Frontend HTML file for user interaction
  |-- appf.py                # Main FastAPI application
  |-- best_rf_model.pkl       # Pre-trained Random Forest model for predictions
  |-- Dockerfile              # Dockerfile for containerizing the FastAPI app
  |-- README.md               # This README file
  |-- requirements.txt        # Python dependencies for the project
  |-- test.txt                # Sample test file for input/output validation
```

---

## Features

- **Medal Prediction**: Input the discipline and event, and the application predicts whether a participant is likely to win a Gold, Silver, or Bronze medal.
- **User Interface**: A simple HTML form where users can input the event details.
- **FastAPI Backend**: The application is powered by FastAPI, a modern web framework for building APIs.
- **Dockerized**: The application is containerized using Docker, making it easy to deploy and run on any platform.

---

## Setup Instructions

### Prerequisites

- **Python 3.8+**
- **Docker** (if running the application in a container)
- **Git** (for version control)

### Local Development

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Geo-y20/2021-olympics-in-tokyo.git
   cd 2021-olympics-in-tokyo
   ```

2. **Create a virtual environment and activate it**:

   ```bash
   python -m venv myenv
   source myenv/bin/activate   # For Linux/Mac
   myenv\Scripts\activate      # For Windows
   ```

3. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application locally**:

   ```bash
   uvicorn appf:app --reload
   ```

5. Open your browser and go to `http://localhost:8000` to access the application.

### Running with Docker

1. **Build the Docker image**:

   ```bash
   docker build -t fastapi-app .
   ```

2. **Run the Docker container**:

   ```bash
   docker run -p 8000:8000 fastapi-app
   ```

3. Access the app at `http://localhost:8000` in your browser.

---

## How It Works

1. **Input**: Users input the `Discipline` and `Event` in the form provided on the website.
2. **Prediction**: The pre-trained Random Forest model processes the input and predicts whether the team will win a Gold, Silver, or Bronze medal.
3. **Output**: The predicted medal type is displayed on the same page.

---

## API Endpoints

- **GET `/`**: Renders the HTML form for input.
- **POST `/predict`**: Accepts form data (discipline and event), processes it, and returns a prediction of the medal type.

### Example API Request (for testing via CURL or Postman):

```bash
curl -X POST "http://localhost:8000/predict" -F 'discipline=1' -F 'event=100'
```

### Example Response:

```json
{
    "prediction_text": "The predicted medal type is: Gold"
}
```

---

## Known Issues

- **Input Validation**: The model may not handle unexpected input values very well. Improvements in input validation and error handling are planned.
- **UI Limitations**: The current HTML form has basic functionality. More complex and interactive UI elements can be added in future updates.

---

## Future Improvements

- **Model Enhancements**: Further tuning of the machine learning model can improve prediction accuracy.
- **Expanded Dataset**: Including additional features (e.g., country ranking, athlete performance history) can lead to better predictions.
- **UI Enhancements**: Creating a more user-friendly and responsive design for the frontend.

---

## Acknowledgements

- **Dataset**: [2021 Olympics in Tokyo - Kaggle](https://www.kaggle.com/datasets/arjunprasadsarkhel/2021-olympics-in-tokyo)
- **FastAPI Documentation**: [FastAPI Official Docs](https://fastapi.tiangolo.com/)
- **Docker Documentation**: [Docker Official Docs](https://docs.docker.com/)

---
Here’s a note you can add to the repository to clarify the two versions of `app.py` and the transition from Flask to FastAPI:

---

### Note on Application Versions

In this repository, there are **two versions** of the application code, each using a different web framework. Initially, the project was implemented using **Flask**, but it was later migrated to **FastAPI** for better performance and flexibility.

#### Version 1: `app.py` (Flask)

- This version of the application was the original implementation using Flask.
- The application worked correctly but lacked some of the performance benefits and modern features that **FastAPI** provides.
- You can still find the `app.py` file in the repository, which contains the Flask version of the app.

#### Version 2: `appf.py` (FastAPI)

- This is the **current and actively used version** of the application, rewritten using **FastAPI**.
- FastAPI offers better performance, asynchronous support, and is more scalable, which is why we transitioned to using it.
- The `appf.py` file contains the FastAPI version of the application, which is now the main file for running the project.

#### Documentation

- The **README.md** file in this repository has been updated to reflect the usage of **FastAPI**.
- If you're using this repository, please follow the setup instructions provided in the README to use the FastAPI version (`appf.py`).
- The Dockerfile and environment settings have been configured for FastAPI as well.

If you need to switch back to the **Flask** version, simply refer to the `app.py` file and modify the Dockerfile or startup command accordingly.

---

