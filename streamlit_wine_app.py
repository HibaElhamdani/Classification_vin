import streamlit as st
import pandas as pd
import joblib
import warnings

# ======================
# 0️⃣ Nettoyer les warnings (optionnel)
# ======================
warnings.filterwarnings("ignore")

# ======================
# 1️⃣ Charger le modèle
# ======================
@st.cache_resource
def load_model():
    return joblib.load("Stacking_wine_model.pkl")

model = load_model()

# ======================
# 2️⃣ Charger dataset pour min / max
# ======================
@st.cache_data
def load_data():
    return pd.read_csv("wine_selected_features.csv")

df = load_data()

# ======================
# 3️⃣ UI
# ======================
st.set_page_config(page_title="Wine Quality Prediction", layout="centered")

st.title("🍷 Wine Quality Prediction")
st.write("Prédiction basée sur le modèle **StackingClassifier optimisé**")

st.markdown("---")
st.subheader("🔧 Paramètres du vin")

# ======================
# 4️⃣ Features de base
# ======================
base_features = [
    "alcohol",
    "sulphates",
    "density",
    "volatile acidity",
    "citric acid",
    "chlorides",
    "total sulfur dioxide",
    "fixed acidity"
]

inputs = {}

for feature in base_features:
    col_min = float(df[feature].min())
    col_max = float(df[feature].max())
    col_mean = float(df[feature].mean())

    inputs[feature] = st.slider(
        label=feature,
        min_value=col_min,
        max_value=col_max,
        value=col_mean
    )

# ======================
# 5️⃣ Construire DataFrame
# ======================
df_feat = pd.DataFrame([inputs])

# ======================
# 6️⃣ Features dérivées (UNIQUEMENT celles du modèle)
# ======================
df_feat["sulphates_alcohol"] = df_feat["sulphates"] * df_feat["alcohol"]
df_feat["density_alcohol"]   = df_feat["density"] / (df_feat["alcohol"] + 1e-6)
df_feat["alcohol_squared"]   = df_feat["alcohol"] ** 2

# ======================
# 7️⃣ Sélection finale (ordre EXACT du modèle)
# ======================
final_features = [
    "sulphates_alcohol",
    "density_alcohol",
    "alcohol",
    "alcohol_squared",
    "volatile acidity",
    "sulphates",
    "citric acid",
    "chlorides",
    "density",
    "total sulfur dioxide",
    "fixed acidity"
]

X_final = df_feat[final_features]

# ======================
# 8️⃣ Prédiction
# ======================
st.markdown("---")

if st.button("🔮 Prédire la qualité du vin"):
    prediction = model.predict(X_final)[0]
    proba = model.predict_proba(X_final)[0]

    if prediction == 1:
        st.success(f"✅ **Vin de BONNE qualité** (probabilité = {proba[1]:.2f})")
    else:
        st.error(f"❌ **Vin de MAUVAISE qualité** (probabilité = {proba[0]:.2f})")

    st.subheader("📊 Données envoyées au modèle")
    st.dataframe(X_final)
