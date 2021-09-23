import streamlit as st

class Session:
    def __init__(self):
        self.page_config = None

    def run_config(self):
        if not self.page_config:
            self.page_config = st.set_page_config(layout="wide")