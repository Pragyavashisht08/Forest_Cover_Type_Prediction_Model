import streamlit as st
import streamlit.components.v1 as com
import numpy as np
import pandas as pd
import pickle
from PIL import Image
st.set_page_config(page_title="Forest Cover Type", page_icon="Spruce_Fir.jpg", layout="centered", initial_sidebar_state="auto")
com.html("""
<div>
<h1 class = "heading" style="text-decoration:underline; width:1024px;">
ML PROJECT
</h1>
</div>
""")
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

page_header = """
<style>
[data-testid="stHeader"]{
background-color : #e5e5f7
}
</style>
"""


page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background-color : #e5e5f7
}
</style>
"""

page_tool_bar = """
<style>
[data-testid="stToolbar"]{
display:none
}
</style>
"""

sub_heading = """
<style>
[data-testid="StyledLinkIconContainer"]{
width:1000px
}
</style>
"""


st.markdown(page_bg_img,unsafe_allow_html=True)
st.markdown(page_header,unsafe_allow_html=True)
st.markdown(page_tool_bar,unsafe_allow_html=True)
Forest_Cover_Type_Prediction = pickle.load(open('Model_for_forest_cover.pkl','rb'))
st.title("FOREST COVER TYPE PREDICTION - BHAVYA BHALLA AND SHIVANSH GUPTA")
image = Image.open('Spruce_Fir.jpg')
st.image(image,use_column_width=True)
elevation = st.text_input('Enter the elevation in meters')
aspect = st.text_input('Enter the aspect angle')
slope = st.text_input('Enter the slope angle')
horizontal_distance_from_hydrology = st.text_input('Enter the horizontal distance from a water source')
vertical_distance_from_hydrology = st.text_input('Enter the vertical distance from a water source')
horizontal_distance_from_roadways = st.text_input('Enter the horizontal distance from road')
horizontal_distance_from_firepoints = st.text_input('Enter the horizontal distance from fire points')
wilderness_area = st.text_input('Enter 4 wilderness areas which are seperated by the commas')
soil_type = st.text_input('Enter 40 soil types seperated by commas')

user_input = []
user_input.append(elevation)
user_input.append(aspect)
user_input.append(slope)
user_input.append(horizontal_distance_from_hydrology)
user_input.append(vertical_distance_from_hydrology)
user_input.append(horizontal_distance_from_roadways)
user_input.append(horizontal_distance_from_firepoints)
wilderness_area1 = wilderness_area.split(',')

for i in wilderness_area1:
    user_input.append(i)

soil_type1 = soil_type.split(',')

for i in soil_type1:
    user_input.append(i)
if len(user_input) == 51:
    features = np.array([user_input],dtype=np.float64)
    prediction = Forest_Cover_Type_Prediction.predict(features).reshape(1,-1)
    st.write(prediction[0])
else:
    st.write('Please input all the values')