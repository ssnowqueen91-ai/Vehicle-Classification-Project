import streamlit as st
from PIL import Image

st.title("Car Classification App")

uploaded_file = st.file_uploader(
    "Upload a car image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    st.success("Image uploaded successfully!") 