import streamlit as st
from PIL import Image

with st.expander("Start Camera"):
    #Start the camera
    camera_image= st.camera_input("Camera")

    if camera_image:
        #Create a Pillow Image Instance
        img=Image.open(camera_image)

        #Convert the pillow image to Grayscale
        gray_img = img.convert("L")

        #Render the grayscale image on the webpage
        st.image(gray_img)
