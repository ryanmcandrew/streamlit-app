import streamlit as st

def run():
    st.sidebar.checkbox('Healthy')
    st.sidebar.radio('Radio', ['Seven', 'Evil', 'Babies'])
    st.sidebar.selectbox('Select', {'America', 'India', 'Japan', 'British Isles'})
    st.sidebar.multiselect('MultiSelect', ['One', 'Two', 'Three'])
    st.sidebar.slider('Slider', min_value=0, max_value=100)
    st.sidebar.select_slider('Select Slider', ['Something', 'Butt', 'Ugly'])
    st.sidebar.text_input('Enter some text')
    st.sidebar.number_input('Enter a number')
    st.sidebar.text_area('Area for textual entry')
    st.sidebar.date_input('Date input')
    st.sidebar.time_input('Time entry')
    st.sidebar.file_uploader('File uploader')
    st.sidebar.color_picker('Pick a color')
    with st.sidebar.form(key='my_form'):
        text_input = st.text_input(label='Enter some text')
        submit_button = st.form_submit_button(label='Submit')