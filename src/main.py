
import os
import common.fetch

STREAMLIT_CMD = "streamlit run"
STREAMLIT_APP_SCRIPT = os.getcwd() + "/src/app.py"

cmd = STREAMLIT_CMD + " " + STREAMLIT_APP_SCRIPT
print("Running " + cmd)
os.system(cmd)