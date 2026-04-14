import streamlit as st
import requests
from datetime import datetime
from API.config.details import Type, Priority, Sub_category, Impact, Category


# API endpoint
API_URL = "http://localhost:8000/predict"

st.set_page_config(page_title="API Tester", layout="centered")

st.title("🔐 Cyber Alert API Tester")

st.markdown("Enter alert details and call the FastAPI `/predict` endpoint.")

# ---------------------------
# INPUT FORM
# ---------------------------
with st.form("prediction_form"):

    category_input = st.selectbox("Category", list(Category.keys()))
    impact_input = st.selectbox("Impact", ["High", "Medium", "Low"])
    priority_input = st.selectbox("Priority", ["Low", "Medium", "High", "Urgent"])
    sub_category_input = st.selectbox("Sub Category", list(Sub_category.keys()))
    type_input = st.selectbox("Type", list(Type.keys()))

    st.markdown("### ⏱️ Time Inputs")

    created_date = st.date_input("Created Date")
    created_time = st.time_input("Created Time")

    due_date = st.date_input("Due Date")
    due_time = st.time_input("Due Time")

    Status = st.text_area(
        "Status",
        "Suspicious email detected and reported"
    )

    submit = st.form_submit_button("🚀 Call API")

# ---------------------------
# PROCESS
# ---------------------------
if submit:

    Created_time = datetime.combine(created_date, created_time)
    Due_by_Time = datetime.combine(due_date, due_time)

    payload = {
        "category_input": category_input,
        "impact_input": impact_input,
        "priority_input": priority_input,
        "sub_category_input": sub_category_input,
        "type_input": type_input,
        "Created_time": Created_time.isoformat(),
        "Due_by_Time": Due_by_Time.isoformat(),
        "Status": Status
    }


    try:
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            result = response.json()
            st.subheader("🔍 Parsed Result")
            st.write(f"**Prediction:** {result.get('predicted_category')}")
            st.write(f"**Confidence:** {result.get('confidence')}")

        else:
            st.error(f"❌ API Error: {response.text}")

    except Exception as e:
        st.error(f"❌ Connection Failed: {str(e)}")