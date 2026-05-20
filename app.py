import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import streamlit as st
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

# ── Page config ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Nike Sales Intelligence",
    page_icon="👟",
    layout="wide",
    initial_sidebar_state="expanded",
)
