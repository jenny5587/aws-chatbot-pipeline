import streamlit as st
import text_lib_kr as glib

st.set_page_config(page_title="Text to Text")
st.title("Text to Text")

input_text = st.text_area("Input text", label_visibility="collapsed")
go_button = st.button("Go", type="primary")
a
if go_button:
    
    with st.spinner("입력중..."): 
        response_content = glib.get_text_response(input_content=input_text) 
        
        st.write(response_content)
