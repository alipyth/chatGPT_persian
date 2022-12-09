import streamlit as st
from deep_translator import GoogleTranslator
from pyChatGPT import ChatGPT

st.title("MY Name is Tarfandoon")

token=""
api = ChatGPT(token)


with st.form('mm'):
    inp = st.text_input('message')
    translated = GoogleTranslator(source='fa', target='en').translate(inp)  # output -> Weiter so, du bist großartig
    sub = st.form_submit_button('submit')
    if sub :
        
        x = api.send_message(translated)
        target = GoogleTranslator(source='en', target='fa').translate(x['message'])
        st.write(target)
