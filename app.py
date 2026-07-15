import streamlit as st
from utils import predict_career

st.set_page_config(
    page_title="AI Career Advisor",
    page_icon="🎯",
    layout="centered"
)

st.title("🎯 AI Career Advisor")
st.markdown("Get career recommendations based on your skills and profile.")

st.divider()

# -----------------------------
# Skills
# -----------------------------
skills = st.multiselect(
    "Select Your Skills",
    [
        "Python",
        "SQL",
        "Pandas",
        "Machine Learning",
        "Deep Learning",
        "Excel",
        "Power BI",
        "Tableau",
        "Java",
        "Spring Boot",
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Node.js",
        "MongoDB",
        "Django",
        "Flask",
        "TensorFlow",
        "OpenCV",
        "Spark",
        "Hadoop",
        "AWS",
        "Azure",
        "Docker",
        "Kubernetes",
        "Linux",
        "Networking",
        "FastAPI",
        "Statistics",
        "R",
        "LangChain",
        "LLM",
        "Prompt Engineering",
        "OpenAI API",
        "Communication",
        "Business Intelligence",
        "DAX",
        "Terraform",
        "Selenium",
        "Android Studio",
        "Swift",
        ".NET",
        "Scikit-learn"
    ]
)

# -----------------------------
# Education
# -----------------------------
education = st.selectbox(
    "Education",
    [
        "B.Sc",
        "B.Com",
        "BBA",
        "B.Tech",
        "MBA",
        "M.Sc",
        "M.Tech",
        "PhD"
    ]
)

# -----------------------------
# Experience
# -----------------------------
experience = st.slider(
    "Years of Experience",
    0,
    15,
    1
)

# -----------------------------
# Interest
# -----------------------------
interest = st.selectbox(
    "Area of Interest",
    [
        "AI",
        "Analytics",
        "Business",
        "Cloud",
        "Cyber Security",
        "Web Development",
        "Software Development",
        "Computer Vision",
        "Research",
        "Backend",
        "BI",
        "DevOps",
        "Generative AI",
        "Big Data",
        "Testing",
        "Mobile Development"
    ]
)

st.divider()

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict Career", use_container_width=True):

    if len(skills) == 0:
        st.warning("Please select at least one skill.")
    else:

        career = predict_career(
            skills,
            education,
            experience,
            interest
        )

        st.success(f"🎉 Recommended Career: **{career}**")

        st.balloons()

st.markdown("---")
st.caption("Built with ❤️ using Python, Scikit-learn & Streamlit")