from fastapi import FastAPI
import pickle
import numpy as np
from pydantic import BaseModel

app = FastAPI()

# Load the model once when the server starts
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define what the input data should look like
class DataInput(BaseModel):
    age: float
    balance: float

@app.post("/predict")
def predict_risk(input_data: DataInput):
    # Convert input to the format the model expects
    features = np.array([[input_data.age, input_data.balance]])
    prediction = model.predict(features)
    
    return {"risk_score": int(prediction[0])}