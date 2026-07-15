import pandas as pd
import pickle

from sklearn.preprocessing import LabelEncoder, MultiLabelBinarizer
from sklearn.ensemble import RandomForestClassifier

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("career_dataset.csv")

# -----------------------------
# Process Skills
# -----------------------------
df["Skills"] = df["Skills"].apply(lambda x: x.split(";"))

mlb = MultiLabelBinarizer()
skills_encoded = pd.DataFrame(
    mlb.fit_transform(df["Skills"]),
    columns=mlb.classes_
)

# -----------------------------
# Encode Education
# -----------------------------
education_encoder = LabelEncoder()
df["Education"] = education_encoder.fit_transform(df["Education"])

# -----------------------------
# Encode Interest
# -----------------------------
interest_encoder = LabelEncoder()
df["Interest"] = interest_encoder.fit_transform(df["Interest"])

# -----------------------------
# Encode Career (Target)
# -----------------------------
career_encoder = LabelEncoder()
df["Career"] = career_encoder.fit_transform(df["Career"])

# -----------------------------
# Prepare Features
# -----------------------------
X = pd.concat(
    [
        skills_encoded,
        df[["Education", "Experience", "Interest"]]
    ],
    axis=1
)

y = df["Career"]

# -----------------------------
# Train Model
# -----------------------------
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X, y)

# -----------------------------
# Save Model
# -----------------------------
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(mlb, open("skills_encoder.pkl", "wb"))

encoders = {
    "education": education_encoder,
    "interest": interest_encoder,
    "career": career_encoder
}

pickle.dump(encoders, open("label_encoder.pkl", "wb"))

print("Model trained successfully!")
print("Files created:")
print("✔ model.pkl")
print("✔ skills_encoder.pkl")
print("✔ label_encoder.pkl")