import streamlit as st
import requests

st.title("🎓 Student Performance Predictor")

st.markdown("Fill in the student details to predict performance.")

# --- Dropdown options ---
gender_options = ['female', 'male']
race_options = ['group A', 'group B', 'group C', 'group D', 'group E']
education_options = [
    "bachelor's degree", 'some college', "master's degree",
    "associate's degree", 'high school', 'some high school'
]
lunch_options = ['standard', 'free/reduced']
prep_course_options = ['none', 'completed']

# --- User Inputs ---
gender = st.selectbox("Gender", gender_options)
race_ethnicity = st.selectbox("Race/Ethnicity", race_options)
parental_level_of_education = st.selectbox("Parental Level of Education", education_options)
lunch = st.selectbox("Lunch Type", lunch_options)
test_preparation_course = st.selectbox("Test Preparation Course", prep_course_options)

reading_score = st.slider("Reading Score", 0, 100, 70)
writing_score = st.slider("Writing Score", 0, 100, 70)

# --- Send to API ---
if st.button("Predict"):
    payload = {
        "gender": gender,
        "race_ethnicity": race_ethnicity,
        "parental_level_of_education": parental_level_of_education,
        "lunch": lunch,
        "test_preparation_course": test_preparation_course,
        "reading_score": str(reading_score),
        "writing_score": str(writing_score)
    }

    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=payload)
        if response.status_code == 200:
            st.success(f"✅ Predicted Value: {response.json()['result']}")
        else:
            st.error(f"❌ Error from server: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"🚨 Could not connect to API: {e}")
