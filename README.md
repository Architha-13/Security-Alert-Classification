# Cyber Security Alert Classification System

A machine learning-powered system to classify cyber security alerts using structured metadata and BERT-based text embeddings.

---

## Overview
This project provides an end-to-end pipeline:
- FastAPI backend for prediction
- BERT embeddings for alert text (Status)
- ML model (pickle) for classification
- Streamlit UI for testing

---

## Features
- Validates inputs using Pydantic schemas
- Converts categorical inputs into model-ready format
- Uses BERT (bert-base-uncased) for text embeddings
- Returns:
  - Predicted category
  - Confidence score
  - Class probability distribution

---

## Project Structure
API/
├── config/              # Label mappings
├── models/              # Model + prediction logic
├── schema/              # Input/output schemas
├── app.py               # FastAPI app
streamlit_ui.py          # UI for testing
requirements.txt

---

## Installation
pip install -r requirements.txt

---

## Run the Application

### Start FastAPI server
cd API
uvicorn API.app:app --reload

### Start Streamlit UI
streamlit run streamlit_ui.py

---

## API Endpoints

### Health Check
GET /health

### Predict Alert
POST /predict

#### Sample Input
{
  "Category": "Email Sec",
  "Impact": "High",
  "Priority": "Urgent",
  "Type": "Incident",
  "Created_time": "2024-01-01T00:00:00",
  "Due_by_Time": "2024-01-02T00:00:00",
  "Sub_category": "Spam",
  "Status": "Suspicious email detected and reported"
}

---

## Output
{
  "predicted_category": "True Positive",
  "confidence": 0.87,
  "class_probabilities": {
    "Benign": 0.05,
    "False Positive": 0.08,
    "Report": 0.10,
    "True Positive": 0.87,
    "Wireless": 0.02
  }
}

---

## Model Details
- Embeddings: BERT (768-dim)
- Classifier: Pre-trained ML model (security_alert.pkl)
- Labels: Benign, False Positive, Report, True Positive

---

## Notes
- Ensure label names match training data exactly
- Time inputs must be valid ISO format
- Model expects aligned feature columns

---

## License
MIT License
