# app.py
import streamlit as st
import torch
import joblib
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from inference_utils import preprocess_text

# =====================
# Page Config
# =====================
st.set_page_config(
    page_title="Analisis Sentimen Cancel Culture",
    layout="centered"
)

# =====================
# Header
# =====================
st.markdown(
    """
    <h1 style="text-align:center;"> Analisis Sentimen Cancel Culture</h1>
    <p style="text-align:center;">
    Perbandingan Model IndoBERT dan SVM
    </p>
    <hr>
    """,
    unsafe_allow_html=True
)

# =====================
# Load Models
# =====================
@st.cache_resource
def load_models():
    tokenizer = AutoTokenizer.from_pretrained("saved_models/indobert")
    model = AutoModelForSequenceClassification.from_pretrained("saved_models/indobert")
    model.eval()

    svm = joblib.load("saved_models/svm.pkl")
    tfidf = joblib.load("saved_models/tfidf.pkl")
    le = joblib.load("saved_models/label_encoder.pkl")

    return tokenizer, model, svm, tfidf, le

tokenizer, model, svm, tfidf, le = load_models()

# =====================
# Input Section
# =====================
st.subheader("📝 Input Teks")
text = st.text_area(
    "Masukkan kalimat:",
    height=120,
    placeholder="Contoh: Cancel culture merupakan budaya yang baik dan bermanfaat untuk melindungi korban."
)

# =====================
# Prediction
# =====================
if st.button("🔍 Prediksi Sentimen", use_container_width=True) and text.strip():

    # Preprocessing
    clean_bert = preprocess_text(text, model_type="indobert")
    clean_svm  = preprocess_text(text, model_type="svm")

    # ---------------------
    # IndoBERT
    # ---------------------
    inputs = tokenizer(
        clean_bert,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    with torch.no_grad():
        logits = model(**inputs).logits
        indobert_pred = logits.argmax(dim=1).item()

    # ---------------------
    # SVM
    # ---------------------
    vec = tfidf.transform([clean_svm])
    svm_pred = svm.predict(vec)[0]

    # =====================
    # Output Section
    # =====================
    st.subheader("📊 Hasil Prediksi")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🤖 IndoBERT")
        st.success(le.inverse_transform([indobert_pred])[0])

    with col2:
        st.markdown("### 📐 SVM")
        st.info(le.inverse_transform([svm_pred])[0])

# =====================
# Footer
# =====================
st.markdown(
    """
    <hr>
    <p style="text-align:center; font-size:12px;">
    Tugas Akhir – Hazna Hamida Saputri
    """,
    unsafe_allow_html=True
)
