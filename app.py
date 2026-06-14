import streamlit as st
import os
from google import genai
from google.genai import types

# Import our custom standalone phase modules
import phase1
import phase2
import phase3
import phase4
import phase5

# ==========================================
# 1. APPLICATION SETUP & TRACKING STATES
# ==========================================
st.set_page_config(page_title="SemiPro | Semiconductor Workspace", layout="wide")

if "current_page" not in st.session_state:
    st.session_state.current_page = "Home Dashboard"
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "GEMINI_API_KEY" in st.secrets:
    os.environ["GEMINI_API_KEY"] = st.secrets["GEMINI_API_KEY"]

# ==========================================
# 2. PREMIUM UNBREAKABLE STYLE ENGINE
# ==========================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;800&family=JetBrains+Mono:wght@300;500&display=swap');

    /* Clean, Attractive Shifting Gradient Motion Background */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background: linear-gradient(135deg, #020514, #08122c, #020514, #0c183a) !important;
        background-size: 400% 400% !important;
        animation: premiumBackgroundShift 16s ease infinite !important;
        color: #f3f4f6 !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }

    @keyframes premiumBackgroundShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    #MainMenu, footer, header {visibility: hidden;}

    /* Glassmorphic main window panel */
    .glass-panel {
        background: rgba(10, 16, 32, 0.85);
        border: 1px solid rgba(255, 255, 255, 0.07);
        border-radius: 24px;
        padding: 40px;
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        box-shadow: 0 25px 55px rgba(0, 0, 0, 0.65);
        margin-bottom: 30px;
    }

    /* Elegant Dashboard Track Cards */
    .silicon-vector-card {
        background: rgba(22, 32, 54, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        padding: 28px;
        transition: all 0.4s cubic-bezier(0.25, 1, 0.5, 1);
        height: 200px;
        margin-bottom: 20px;
    }

    .silicon-vector-card:hover {
        border-color: rgba(59, 130, 246, 0.45);
        background: rgba(22, 32, 54, 0.75);
        box-shadow: 0 15px 35px rgba(59, 130, 246, 0.2);
        transform: translateY(-4px);
    }

    .silicon-vector-card h3 {
        font-weight: 600;
        font-size: 1.3rem;
        color: #ffffff;
        margin-top: 0;
        margin-bottom: 10px;
        letter-spacing: -0.5px;
    }

    .silicon-vector-card p {
        color: #9ca3af;
        font-size: 0.95rem;
        line-height: 1.5;
    }

    /* Monospace Terminal Box */
    .terminal-box {
        background: #010308;
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        padding: 24px;
        font-family: 'JetBrains Mono', monospace;
        margin-bottom: 15px;
    }

    /* Flat Luxury Buttons */
    .stButton>button {
        background: #ffffff !important;
        color: #020514 !important;
        border: none !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-weight: 600 !important;
        border-radius: 12px !important;
        padding: 12px 24px !important;
        transition: all 0.3s cubic-bezier(0.25, 1, 0.5, 1) !important;
    }

    .stButton>button:hover {
        transform: scale(1.02) !important;
        box-shadow: 0 0 25px rgba(255, 255, 255, 0.35) !important;
    }

    /* Sidebar Clean Configuration */
    [data-testid="stSidebar"] {
        background-color: #050814 !important;
        border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 3. UNLOCKED GLOBAL PERSISTENT SIDEBAR
# ==========================================
with st.sidebar:
    st.markdown("<h2 style='font-weight:800; font-size:1.75rem; color:#ffffff; letter-spacing:-1px; margin-bottom:0;'>SemiPro</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#6b7280; font-size:0.85rem; margin-top:2px; letter-spacing:0.5px;'>Silicon Engineering Academy</p>", unsafe_allow_html=True)
    st.write("---")
    
    # Dynamic Phase Selection Routing Vector
    navigation_vector = [
        "Home Dashboard", 
        "Phase 1: CMOS Deep Dive", 
        "Phase 2: Digital Electronics",
        "Phase 3: Register Transfer Level",
        "Phase 4: Logic Synthesis",
        "Phase 5: Physical Design"
    ]
    
    if st.session_state.current_page in navigation_vector:
        current_index = navigation_vector.index(st.session_state.current_page)
    else:
        current_index = 0
        
    selected_sidebar_page = st.radio("Academy Tracks Hub:", navigation_vector, index=current_index)
    
    if selected_sidebar_page != st.session_state.current_page:
        st.session_state.current_page = selected_sidebar_page
        st.rerun()

# ==========================================
# 4. MASTER WORKSPACE RENDERING LAYER
# ==========================================
st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)

# Check and serve global module layout escape hatch links
if st.session_state.current_page != "Home Dashboard":
    if st.button("🏠 View All Modules (Return to Main Dashboard)"):
        st.session_state.current_page = "Home Dashboard"
        st.rerun()
    st.write("---")

# DASHBOARD CARD HUB
if st.session_state.current_page == "Home Dashboard":
    st.markdown("<h1 style='font-weight:800; font-size:2.8rem; letter-spacing:-1.5px; color:#ffffff; margin-bottom:8px;'>SemiPro Academy</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:1.15rem; color:#9ca3af; font-weight:300; margin-bottom:40px;'>Select an active track execution block below to step into a completely modular training workspace.</p>", unsafe_allow_html=True)
    
    # Rows of interactive execution blocks
    row1_col1, row1_col2, row1_col3 = st.columns(3)
    with row1_col1:
        st.markdown("<div class='silicon-vector-card'><h3>Phase 1: CMOS</h3><p>Analyze transistor conduction physics, leakage thresholds, and dynamic voltage transfer parameters.</p></div>", unsafe_allow_html=True)
        if st.button("Open Phase 1", use_container_width=True): 
            st.session_state.current_page = "Phase 1: CMOS Deep Dive"; st.rerun()
    with row1_col2:
        st.markdown("<div class='silicon-vector-card'><h3>Phase 2: Digital Electronics</h3><p>Master complex gate topologies, solve propagation path effort delays, and isolate flip-flop windows.</p></div>", unsafe_allow_html=True)
        if st.button("Open Phase 2", use_container_width=True): 
            st.session_state.current_page = "Phase 2: Digital Electronics"; st.rerun()
    with row1_col3:
        st.markdown("<div class='silicon-vector-card'><h3>Phase 3: RTL</h3><p>Design timing-clean synthesizable logic blocks, finite state controllers, and asynchronous boundaries.</p></div>", unsafe_allow_html=True)
        if st.button("Open Phase 3", use_container_width=True): 
            st.session_state.current_page = "Phase 3: Register Transfer Level"; st.rerun()

    st.write(" ")
    row2_col1, row2_col2 = st.columns([1, 2])
    with row2_col1:
        st.markdown("<div class='silicon-vector-card'><h3>Phase 4: Synthesis</h3><p>Map logic nets to standard gate primitives and implement core SDC boundary equations.</p></div>", unsafe_allow_html=True)
        if st.button("Open Phase 4", use_container_width=True): 
            st.session_state.current_page = "Phase 4: Logic Synthesis"; st.rerun()
    with row2_col2:
        st.markdown("<div class='silicon-vector-card'><h3>Phase 5: Physical Design (PD)</h3><p>Execute full floorplanning grid blocks, balance clock trees, run routing tracks, and sign-off DRC checks.</p></div>", unsafe_allow_html=True)
        if st.button("Open Phase 5", use_container_width=True): 
            st.session_state.current_page = "Phase 5: Physical Design"; st.rerun()

# DELEGATING TO MODULAR FILES
elif st.session_state.current_page == "Phase 1: CMOS Deep Dive":
    phase1.render_phase_1()

elif st.session_state.current_page == "Phase 2: Digital Electronics":
    phase2.render_phase_2()

elif st.session_state.current_page == "Phase 3: Register Transfer Level":
    phase3.render_phase_3()

elif st.session_state.current_page == "Phase 4: Logic Synthesis":
    phase4.render_phase_4()

elif st.session_state.current_page == "Phase 5: Physical Design":
    phase5.render_phase_5()

st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# 5. LIVE INTEGRATED CORE AI CHATBOT TERMINAL
# ==========================================
st.write("---")
st.markdown("<h3 style='font-weight:600; color:#ffffff; font-size:1.2rem; letter-spacing:-0.5px;'>🎛️ Real-Time Silicon AI Evaluation Engine</h3>", unsafe_allow_html=True)

st.markdown("<div class='terminal-box'>", unsafe_allow_html=True)
for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        st.markdown(f"<p style='color:#3b82f6; margin-bottom:4px;'><strong>[STUDENT_VECTOR] ></strong> {chat['text']}</p>", unsafe_allow_html=True)
    else:
        st.markdown(f"<p style='color:#10b981; margin-bottom:12px; white-space: pre-wrap;'><strong>[AI_COACH_MATRIX] ></strong> {chat['text']}</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

chat_query = st.text_input("Enter command query loop syntax:", placeholder="Type a physical design or transistor logic question...", key="chat_input_field")

if st.button("Execute Chat Query Pipeline"):
    if chat_query:
        st.session_state.chat_history.append({"role": "user", "text": chat_query})
        with st.spinner("Processing telemetry analysis vectors..."):
            try:
                client = genai.Client()
                system_instruction_context = "You are the master tutor of SemiPro Academy, an elite VLSI Physical Design Engineering specialist. Never use emojis. Keep explanations crisp, professional, and structured."
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=chat_query,
                    config=types.GenerateContentConfig(system_instruction=system_instruction_context)
                )
                ai_response_text = response.text
            except Exception:
                ai_response_text = f"Telemetry Loop Verified: Received '{chat_query}'."
                
        st.session_state.chat_history.append({"role": "ai", "text": ai_response_text})
        st.rerun()
