import requests
import os
from datetime import datetime

nutritionix_id =os.environ.get("nutritionix_id")
nutritionix_api_key=os.environ.get("nutritionix_api_key")
nutrients_endpoint = "https://trackapi.nutritionix.com//v2/natural/exercise"
headers = {
    "x-app-id": nutritionix_id,
    "x-app-key": nutritionix_api_key
}

workout_api_endpoint = "https://api.sheety.co/ed968313e6dbce797554c61f8199e9bc/workoutTracking/workouts"
workout_header = {
    "Authorization" : os.environ.get("sheety_bearer")
}

exercises = input("Your Exercises: ")
gender = "male"
weight_kg = 56.4
height_cm = 168
age= 20

body = {
    "query": exercises,
    "gender": gender,
    "weight_kg": weight_kg,
    "height_cm": height_cm,
    "age": age
}
response = requests.post(url=nutrients_endpoint, json=body, headers=headers)
response.raise_for_status()
# print(response.text)

for exercise in response.json()["exercises"]:

    body = {
        "workout":{
            "date" : datetime.today().strftime("%d/%m/%Y"),
            "time" : datetime.today().strftime("%H:%M"),
            "exercise" : exercise['name'],
            "duration" : exercise['duration_min'],
            "calories": exercise["nf_calories"]
        }
    }
    workout_response = requests.post(url=workout_api_endpoint, json=body, headers=workout_header)
    workout_response.raise_for_status()
    print(workout_response.text)
