import streamlit as st
import pandas as pd
import pickle

with open('placement_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.set_page_config(page_title="Placement Predictor", layout="centered")

st.title("🎓 Student Placement Predictor")
st.write("Enter the academic and technical profile to predict placement probability.")
st.divider()

col1, col2 = st.columns(2)

with col1:
    cgpa = st.number_input("CGPA (Out of 10)", min_value=0.0, max_value=10.0, value=7.5, step=0.1)
    internships = st.number_input("Number of Internships", min_value=0, max_value=10, value=1)
    projects = st.number_input("Number of Projects", min_value=0, max_value=15, value=2)

with col2:
    aptitude = st.slider("Aptitude Test Score (%)", min_value=0, max_value=100, value=70)
    soft_skills = st.slider("Soft Skills Rating (1-5)", min_value=1, max_value=5, value=3)
    coding_skills = st.slider("Coding/Tech Skills Rating (1-5)", min_value=1, max_value=5, value=3)

if st.button("Analyze Profile", type="primary"):
    input_data = pd.DataFrame({
        'CGPA': [cgpa],
        'Internships': [internships],
        'Projects': [projects],
        'Aptitude_Score': [aptitude],
        'Soft_Skills_Rating': [soft_skills],
        'Coding_Skills_Rating': [coding_skills]
    })
    
    # Get the probability of getting placed (Class 1)
    probability = model.predict_proba(input_data)[0][1] * 100
    
    st.divider()
    st.subheader("Analysis Results")
    
    # Tiered Results Logic
    if probability >= 85:
        st.success(f"🌟 Excellent! (Probability: {probability:.1f}%)")
        st.write("Outstanding profile. With these core technical skills and projects, you are highly likely to secure a premium placement.")
        st.balloons()
        
    elif probability >= 60:
        st.info(f"👍 Good Chances (Probability: {probability:.1f}%)")
        st.write("You have a solid foundation. Polishing your communication skills or adding one more complex backend or UI/UX project could make you a top-tier candidate.")
        
    elif probability >= 40:
        st.warning(f"⚠️ Borderline/Average (Probability: {probability:.1f}%)")
        st.write("You are in the middle of the pack. To stand out to recruiters, you need to actively work on improving your coding fundamentals and aim for at least one solid internship.")
        
    else:
        st.error(f"🚨 High Risk (Probability: {probability:.1f}%)")
        st.write("Your current profile needs significant improvement. Focus urgently on raising your CGPA, mastering a core programming language (like Python or Java), and practicing aptitude tests.")