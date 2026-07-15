import pickle
import pandas as pd


# -----------------------------
# Load Saved Files
# -----------------------------
model = pickle.load(open("model.pkl", "rb"))
mlb = pickle.load(open("skills_encoder.pkl", "rb"))
encoders = pickle.load(open("label_encoder.pkl", "rb"))

education_encoder = encoders["education"]
interest_encoder = encoders["interest"]
career_encoder = encoders["career"]


# -----------------------------
# Prediction Function
# -----------------------------
def predict_career(skills, education, experience, interest):

    # Encode skills
    skills_vector = mlb.transform([skills])
    skills_df = pd.DataFrame(skills_vector, columns=mlb.classes_)

    # Encode education
    education_value = education_encoder.transform([education])[0]

    # Encode interest
    interest_value = interest_encoder.transform([interest])[0]

    # Create input dataframe
    input_df = skills_df.copy()
    input_df["Education"] = education_value
    input_df["Experience"] = experience
    input_df["Interest"] = interest_value

    # Predict
    prediction = model.predict(input_df)[0]

    # Decode prediction
    career = career_encoder.inverse_transform([prediction])[0]

    return career