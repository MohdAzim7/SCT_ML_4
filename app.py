import streamlit as st
import cv2
import numpy as np
from src.predict_image import predict_image
import sys
import os
sys.path.append(os.path.abspath("src"))

from predict_image import predict_image

st.set_page_config(
    page_title="Gesture AI",
    page_icon="🎧",
    layout="wide"
)

# ---------- Custom CSS (Spotify Style) ----------
st.markdown("""
<style>
body {
    background-color: #0d0d0d;
    color: white;
    font-family: 'Poppins', sans-serif;
}

[data-testid="stAppViewContainer"] {
    background: #0d0d0d;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #000000;
    padding: 20px;
}

/* Title */
.title {
    font-size: 32px;
    font-weight: 700;
    color: #1DB954;
}

/* Card UI */
.card {
    background: linear-gradient(145deg, #1a1a1a, #111);
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.6);
}

/* Prediction */
.prediction {
    font-size: 26px;
    font-weight: bold;
    color: #1DB954;
}

.confidence {
    font-size: 18px;
    color: #ccc;
}

/* Upload box */
.upload-box {
    border: 2px dashed #1DB954;
    padding: 30px;
    border-radius: 15px;
    text-align: center;
}

/* Fake nav */
.nav-item {
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 5px;
}
.nav-item:hover {
    background: #1DB954;
    color: black;
    cursor: pointer;
}
</style>
""", unsafe_allow_html=True)

# ---------- Sidebar (Spotify Style Nav) ----------
st.sidebar.markdown("<div class='title'>🎧 Gesture AI</div>", unsafe_allow_html=True)

st.sidebar.markdown("### Navigation")
st.sidebar.markdown("<div class='nav-item'>🏠 Home</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='nav-item'>📊 Analytics</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='nav-item'>📁 Library</div>", unsafe_allow_html=True)
st.sidebar.markdown("<div class='nav-item'>⚙ Settings</div>", unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.markdown("### Supported Gestures")
st.sidebar.markdown("""
✋ Palm  
🤟 L  
✊ Fist  
👍 Thumb  
👌 OK  
👇 Down  
""")

# ---------- Layout ----------
col1, col2, col3 = st.columns([2, 3, 2])

# ---------- Left Panel ----------
with col1:
    st.markdown("<div class='card'><h4>🔥 Recent Activity</h4><p>No recent predictions</p></div>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<div class='card'><h4>📈 Model Info</h4><p>HOG + Random Forest</p></div>", unsafe_allow_html=True)

# ---------- Center Panel ----------
with col2:
    st.markdown("<h2 style='text-align:center;'>Upload Gesture</h2>", unsafe_allow_html=True)

    uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"])

    if uploaded_file:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        st.image(image, channels="BGR", use_container_width=True)

        prediction, confidence = predict_image(image)

# ---------- Right Panel ----------
with col3:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    if uploaded_file:
        st.markdown(f"<div class='prediction'>🎯 {prediction}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='confidence'>Confidence: {confidence}%</div>", unsafe_allow_html=True)
    else:
        st.markdown("<p>Upload an image to see prediction</p>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)