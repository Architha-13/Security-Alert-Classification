from fastapi import FastAPI
from fastapi.responses import JSONResponse
from models.predict import predict_risk, Model_Version
from schema.user_input import Alert
from schema.prediction_response import PredictionResponse


app = FastAPI()

@app.get("/")   
def home():   
    return {"message": "Welcome to Cyber Security Alert Classification System!"} 

@app.get("/health")      #used msotly in cloud services for them to monitor the health of the API, and also to provide a welcome message or basic information about the API to users who access the root URL.
def health_check():
    return {"status": "OK", "model_version": Model_Version, "model_loaded": True}

@app.post("/predict", response_model=PredictionResponse)
def predict(alert: Alert):
    input_data = {
       
    "Category": alert.Category,
        "Impact": alert.Impact,
        "Priority": alert.Priority,
        "Type": alert.Type,
        "Created_time": alert.Created_time,
        "Due_by_Time": alert.Due_by_Time,
        "Sub_category": alert.Sub_category,
        "Status": alert.Status
    }
    try:
        prediction = predict_risk(alert)
        return prediction
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
