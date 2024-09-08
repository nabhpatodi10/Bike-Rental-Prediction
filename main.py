from ast import For
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Form
import uvicorn
from pydantic import BaseModel, conint
import joblib
import pandas as pd
import math

app = FastAPI()

model = joblib.load("Model.pkl")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
def root(requests: Request):
    return templates.TemplateResponse("index.html", {"request" : requests})

@app.post("/readings", response_class=HTMLResponse)
def get_readings(requests: Request, season: int = Form(), year: int = Form(), month: int = Form(), holiday: bool = Form(), weekday: int = Form(), workingday: bool = Form(), weather_situation: int = Form(), temperature: float = Form(), feels_like_temperature: float = Form(), humidity: float = Form(), windspeed: float = Form()):
    prediction = model.predict(
                    pd.DataFrame({
                    'season': [season],
                    'yr': [year],
                    'mnth': [month],
                    'holiday': [1 if holiday else 0],
                    'weekday': [weekday],
                    'workingday': [1 if workingday else 0],
                    'weathersit': [weather_situation],
                    'temp': [temperature],
                    'atemp': [feels_like_temperature],
                    'hum': [humidity],
                    'windspeed': [windspeed]
                    })
                )[0]
    return templates.TemplateResponse("readings.html", {"request" : requests, "season" : season, "year" : year, "month" : month, "holiday" : holiday, "weekday" : weekday, "workingday" : workingday, "weather_situation" : weather_situation, "temperature" : temperature, "feels_like_temperature" : feels_like_temperature, "humidity" : humidity, "windspeed" : windspeed, "prediction" : math.ceil(prediction)})

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)