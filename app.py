import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("🖼️ Live Image Processing Web App")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img_np = np.array(image)

    st.image(img_np, caption='Original Image', use_column_width=True)

    option = st.selectbox("Choose a filter to apply", 
                         ["None", "Grayscale", "Smoothing", "Sharpening", "Edge Detection"])

    if option == "Grayscale":
        result = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)
        st.image(result, caption="Grayscale", use_column_width=True)

    elif option == "Smoothing":
        result = cv2.GaussianBlur(img_np, (9, 9), 0)
        st.image(result, caption="Smoothed", use_column_width=True)

    elif option == "Sharpening":
        kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])
        result = cv2.filter2D(img_np, -1, kernel)
        st.image(result, caption="Sharpened", use_column_width=True)

    elif option == "Edge Detection":
        gray = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)
        result = cv2.Canny(gray, 100, 200)
        st.image(result, caption="Edges", use_column_width=True)
        