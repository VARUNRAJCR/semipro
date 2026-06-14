import streamlit as st
import os

# Import our custom isolated architecture chunks
from styles import inject_premium_ui
import curriculum
from chatbot import render_ai_chatbot

# 1. Base Setup & Configuration Routing
if "current_page" not in st.session_state: st.session_state.current_page = "Home Dashboard"
if "chat_history" not in st.session_state: st.session_state.chat_history = []

if "GEMINI_API_KEY" in st.secrets:
    os.environ["GEMINI_API_KEY"] = st.secrets["GEMINI_API_KEY"]

# Inject the dynamic background and glass themes from style module
inject_premium_ui()

# Helper Navigation routing function
def navigate_to(page_name):
    st.session_state.current_page = page_name

# ==========================================
# SIDEBAR CONTROL NODE
# ==========================================
with st.sidebar:
    st.markdown("<h2 style='font-weight:800; font-size:1.6rem; color:#ffffff; letter-spacing:-1px; margin-bottom:0;'>SemiPro</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#6b7280; font-size:0.85rem; margin-top:0;'>Silicon Engineering Portal</p>", unsafe_allow_html=True)
    st.write("---")
    
    navigation_vector = ["Home Dashboard", "Phase 1: Silicon Foundations", "Phase 2: Circuit Logic Matrix", "Phase 3: Physical Automation"]
    current_index = navigation_vector.index(st.session_state.current_page)
    selected_sidebar_page = st.sidebar.radio("System Vector Navigation:", navigation_vector, index=current_index)
    
    if selected_sidebar_page != st.session_state.current_page:
        navigate_to(selected_sidebar_page)
        st.rerun()

# ==========================================
# WORKSPACE DISPLAY RENDERING ENGINE
# ==========================================
st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)

if st.session_state.current_page == "Home Dashboard":
    st.markdown("<h1 style='font-weight:800; font-size:2.8rem; letter-spacing:-1.5px; color:#ffffff; margin-bottom:8px;'>The Physical Design Academy</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:1.15rem; color:#9ca3af; font-weight:300; margin-bottom:40px;'>Master modern semiconductor integration tracks systematically from raw transistor logic up to sign-off tapeout.</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<div class='vector-card'><h3>Phase 1: Silicon Foundations</h3><p>Isolate NMOS/PMOS transistor switching physics, threshold shift variance metrics, and mathematical operational curve boundaries.</p></div>", unsafe_allow_html=True)
        if st.button("Enter Phase 1 Workspace", use_container_width=True): navigate_to("Phase 1: Silicon Foundations"); st.rerun()
    with col2:
        st.markdown("<div class='vector-card'><h3>Phase 2: Circuit Logic Matrix</h3><p>Map complex combinational gates, optimize structural network pathways via logical effort formulas, and solve flip-flop parameters.</p></div>", unsafe_allow_html=True)
        if st.button("Enter Phase 2 Workspace", use_container_width=True): navigate_to("Phase 2: Circuit Logic Matrix"); st.rerun()
    with col3:
        st.markdown("<div class='vector-card'><h3>Phase 3: Physical Automation</h3><p>Process modern industry implementation flows: SDC synthesis execution constraints, multi-corner STA timing slacks, and detailed routing DRC resolution vectors.</p></div>", unsafe_allow_html=True)
        if st.button("Enter Phase 3 Workspace", use_container_width=True): navigate_to("Phase 3: Physical Automation"); st.rerun()

elif st.session_state.current_page == "Phase 1: Silicon Foundations":
    if st.button("⬅️ Return to Main Dashboard", key="b1"): navigate_to("Home Dashboard"); st.rerun()
    curriculum.show_phase_1()

elif st.session_state.current_page == "Phase 2: Circuit Logic Matrix":
    if st.button("⬅️ Return to Main Dashboard", key="b2"): navigate_to("Home Dashboard"); st.rerun()
    curriculum.show_phase_2()

elif st.session_state.current_page == "Phase 3: Physical Automation":
    if st.button("⬅️ Return to Main Dashboard", key="b3"): navigate_to("Home Dashboard"); st.rerun()
    curriculum.show_phase_3()

st.markdown("</div>", unsafe_allow_html=True)

# Inject the real-time evaluation chatbot loop dynamically at base layer
render_ai_chatbot()
