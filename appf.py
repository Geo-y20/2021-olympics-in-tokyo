from fastapi import FastAPI, Form
from pydantic import BaseModel
import pickle
import numpy as np
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

# Initialize FastAPI app
app = FastAPI()

# Load the saved Random Forest model
with open('best_rf_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Setup Jinja2 templates for rendering HTML
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    # Renders the HTML form from index.html
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict", response_class=HTMLResponse)
async def predict(request: Request, discipline: int = Form(...), event: int = Form(...)):
    # Prepare the features for prediction
    features = np.array([[discipline, event]])
    
    # Make the prediction
    prediction = model.predict(features)
    
    # Map the prediction to the medal type
    medal_map = {0: 'Bronze', 1: 'Gold', 2: 'Silver'}
    predicted_medal = medal_map.get(prediction[0], "Unknown")
    
    # Render the result on the same page
    return templates.TemplateResponse("index.html", {
        "request": request,
        "prediction_text": f'The predicted medal type is: {predicted_medal}'
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
