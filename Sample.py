import streamlit as st

st.title('Hack for Africa - AI OCR')
st.subheader('Optical Character Recognition with Voice output')

st.text('Select source language from the sidebar')

image = st.file_uploader('Upload Image',['JPG','PNG'])

if st.button('Convert'):
	pass

st.sidebar.title('Language Selection Menu')

st.sidebar.subheader('Select...')

from_language = st.sidebar.selectbox('From language',['English','French'],key = '1')

st.sidebar.write('')

st.sidebar.subheader('Select...')

to_language = st.sidebar.selectbox('to language',['English','French'],key = '2')

st.sidebar.write('')

st.sidebar.subheader('Enter text')

st.sidebar.text_area('Auto detection enabled')

if st.sidebar.button('Transalate'):
	pass

