import streamlit as st
import numpy as np
import pandas as pd
import webbrowser
from bokeh.models.widgets import Div

st.title('Our Awesome Name')
st.header('There are three main methods to generate flashcards.')

#Method1
st.subheader('Method 1:')
st.write('This is the reccomended method. The extention will automatically generate flashcards based on what is on your screen.')

if st.button('Download Browser Extension'):
    js = "window.open('https://www.streamlit.io/')"  # New tab or window
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)

#Method2
st.subheader('Method 2:')
st.write('Feel free to copy and paste your text.')
sentence = st.text_input('Paste Text Here:') 

#Method3
st.subheader('Method 3:')
st.write('You can also upload files')
uploaded_file = st.file_uploader("Insert Text File", type="csv")
st.set_option('deprecation.showfileUploaderEncoding', False)

st.subheader('Use the side bar to display you current flashcards')
st.subheader('       ')
#sidetoggle
st.sidebar.title('CLIMATE FORECAST')
topic = st.sidebar.selectbox('Topic', ['Biology', 'Chemistry', 'MCAT'])
vocab = st.sidebar.selectbox('Vocab:', ['Words', 'Definitions'])
fig = f'{topic}_{vocab}.jpg'
submit = st.sidebar.button('submit')
if submit:
    st.image(open(fig, 'rb').read(), format='jpg')

#toggles 
progress = st.checkbox("My Progress", key=2)

if progress: 
    progress_chart = pd.DataFrame(np.random.randn(20,3), columns=['a','b','c',])

    st.area_chart(progress_chart)

#removewarning
st.set_option('deprecation.showImageFormat', False)