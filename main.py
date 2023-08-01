import streamlit as st
from PIL import Image
import io

with st.expander("Start Camera"):
    # Start the camera
    camera_image = st.camera_input("Camera")

    if camera_image:
        # Create a Pillow Image Instance
        img = Image.open(camera_image)

        # Convert the pillow image to Grayscale
        gray_img = img.convert("L")

        # Render the grayscale image on the webpage
        st.image(gray_img)

        # Add download buttons for both images
        col1, col2 = st.beta_columns(2)

        # Download button for grayscale image
        buffer = io.BytesIO()
        gray_img.save(buffer, format="PNG")
        buffer.seek(0)
        col1.download_button("Download Grayscale Image", data=buffer, file_name="grayscale.png")

        # Download button for the original image
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)
        col2.download_button("Download Original Image", data=buffer, file_name="original.png")
