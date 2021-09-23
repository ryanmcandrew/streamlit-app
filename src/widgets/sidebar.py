import streamlit as st

def run():
    
    with st.sidebar.form(key='my_form'):
        cb = st.checkbox('Healthy')
        r = st.radio('Radio', ['Seven', 'Evil', 'Babies'])
        sb = st.selectbox('Select', {'America', 'India', 'Japan', 'British Isles'})
        ms = st.multiselect('MultiSelect', ['One', 'Two', 'Three'])
        s = st.slider('Slider', min_value=0, max_value=100)
        ss = st.select_slider('Select Slider', ['Something', 'Butt', 'Ugly'])
        ti = st.text_input('Enter some text')
        ni = st.number_input('Enter a number')
        ta = st.text_area('Area for textual entry')
        di = st.date_input('Date input')
        ti = st.time_input('Time entry')
        fu = st.file_uploader('File uploader')
        cp = st.color_picker('Pick a color')
        submit_button = st.form_submit_button(label='Submit')