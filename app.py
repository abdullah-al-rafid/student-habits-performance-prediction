import streamlit as st
import numpy as np
import joblib
import warnings
warnings.filterwarnings("ignore")

model = joblib.load('best_model.pkl')

st.title("Marks Predictor For DMML")

study_hours = st.slider("Study Hours Per Day", 0.0, 12.0, 2.0)
attendance = st.slider("Attendance Percentage",0.0, 100.0,80.0)
mental_health = st.slider("Mental Health Rating (1-10)",1,10,5)
sleep_hours = st.slider("Sleep Hours Per Night", 0.0, 12.0, 8.0)
social_media_hours = st.slider("Social Media Hours",0.0,12.0,2.0)
part_time_job = st.selectbox("Part-Time Job", ["Yes", "No"])


ptj_encode = 1 if part_time_job == "Yes" else 0

if st.button("Predict"):
    
    input_data = np.array([study_hours,attendance,mental_health,sleep_hours,social_media_hours,ptj_encode]).reshape(1,-1)
    prediction = model.predict(input_data)[0]
    
   prediction = model.predict(input_data)[0]

   prediction = max(0, min(100, prediction))

   st.success(f"Predicted Exam Score: {prediction:.2f}")
    
   st.success(f"Predicted Exam Score: {prediction:.2f}")
