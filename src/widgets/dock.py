import streamlit as st


def run():
    st.title('Details')
    with st.expander('stuff'):
        st.write("Check out the [code](https://github.com/ryanmcandrew/streamlit-app)")