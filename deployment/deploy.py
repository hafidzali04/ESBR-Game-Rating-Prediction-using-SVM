# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 18:51:25 2022

@author: Ali
"""

import streamlit as st
import pandas as pd
import joblib
from PIL import Image

st.header('ESRB RATINGS PREDICTION')
st.write("""The features is 0 : no and 1 : yes             
Use the sidebar to select input features.
""")
image = Image.open('ESRBFeature.jpg')

st.image(image)
@st.cache
def fetch_data():
    df = pd.read_csv('https://raw.githubusercontent.com/hafidzali04/Hacktiv8-phase0/main/data/Video_games_esrb_rating.csv')
    return df

df = fetch_data()
#st.write(df)

st.sidebar.header('User Input Features')

def user_input():
    blood = st.sidebar.selectbox('Blood ', df['blood'].unique())
    blood_and_gore = st.sidebar.selectbox('Blood and Gore', df['blood_and_gore'].unique())
    drug_reference = st.sidebar.selectbox('Drug reference ', df['drug_reference'].unique())
    intense_violence = st.sidebar.selectbox('Intense violenced ', df['intense_violence'].unique())
    language = st.sidebar.selectbox('language ', df['language'].unique())
    mild_cartoon_violence = st.sidebar.selectbox('Mild cartoon violence ', df['mild_cartoon_violence'].unique())
    mild_fantasy_violence = st.sidebar.selectbox('Mild fantasy violence ', df['mild_fantasy_violence'].unique())
    no_descriptors = st.sidebar.selectbox('no descriptors', df['no_descriptors'].unique())
    partial_nudity = st.sidebar.selectbox('Partial nudity', df['partial_nudity'].unique())
    sexual_content = st.sidebar.selectbox('Sexual content', df['sexual_content'].unique())
    sexual_themes = st.sidebar.selectbox('Sexual themes', df['sexual_themes'].unique())
    simulated_gambling = st.sidebar.selectbox('Simulated gambling', df['simulated_gambling'].unique())
    strong_janguage = st.sidebar.selectbox('Strong languages', df['strong_janguage'].unique())
    strong_sexual_content = st.sidebar.selectbox('Strong sexual content ', df['strong_sexual_content'].unique())
    suggestive_themes = st.sidebar.selectbox('Suggestive themes ', df['suggestive_themes'].unique())
    violence= st.sidebar.selectbox('violence ', df['violence'].unique())
	#	language	mild_cartoon_violence	mild_fantasy_violence	no_descriptors	partial_nudity	sexual_content	sexual_themes	simulated_gambling	strong_language	strong_sexual_content	suggestive_themes	violence						
    data = {
        'blood': blood,
        'blood_and_gore': blood_and_gore,
        'drug_reference': drug_reference,
        'intense_violence': intense_violence,
        'language': language,
        'mild_cartoon_violence': mild_cartoon_violence,
        'mild_fantasy_violence': mild_fantasy_violence,
        'no_descriptors': no_descriptors,
        'partial_nudity':partial_nudity,
        'sexual_content': sexual_content,
        'sexual_themes': sexual_themes,
        'simulated_gambling': simulated_gambling,
        'strong_janguage': strong_janguage,
        'strong_sexual_content': strong_sexual_content,
        'suggestive_themes': suggestive_themes,
        'violence':violence
    }
    features = pd.DataFrame(data, index=[0])
    return features


input = user_input()

st.subheader('User Input')
st.write(input)

load_model = joblib.load("my_model.pkl")

prediction = load_model.predict(input)



st.write('Based on user input, predicted is: ')
if(prediction==0):
  prediction='Everyone can play it'

elif(prediction==1):
 prediction='Game rating is Early Teen, you need to 10+ for play it'

elif(prediction==2):
  prediction='Game rating is Teen, you need to 13+ for play it'
else :
  prediction='Game rating is Mature, you need to 17+ for play it'

st.write(prediction)
