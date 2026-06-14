import streamlit as st
import os
from google import genai
from google.genai import types

# ==========================================
# 1. CORE SYSTEM CONFIGURATION
# ==========================================
st.set_page_config(page_title="SemiPro | Semiconductor Architecture", layout="wide")

# Persistent page state initialization
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home Dashboard"
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "GEMINI_API_KEY" in st.secrets:
    os.environ["GEMINI_API_KEY"] = st.secrets["GEMINI_API_KEY"]

# ==========================================
# 2. NATIVE UNBREAKABLE MOTION BACKGROUND & CSS
# ==========================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;800&family=JetBrains+Mono:wght@300;500&display=swap');

    /* Native CSS Animated Shifting Gradient Background (No JavaScript required) */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background: linear-gradient(125deg, #020512, #070f26, #020512, #0b1536) !important;
        background-size: 400% 400% !important;
        animation: universalGradientMotion 15s ease infinite !important;
        color: #f3f4f6 !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }

    @keyframes universalGradientMotion {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Remove native white-label blockades */
    #MainMenu, footer, header {visibility: hidden;}

    /* Glassmorphic main visual panel */
    .glass-panel {
        background: rgba(11, 17, 34, 0.85);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 24px;
        padding: 40px;
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6);
        margin-bottom: 30px;
    }

    /* Premium Silicon Vector Track Cards */
    .vector-card {
        background: rgba(22, 30, 49, 0.55);
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 16px;
        padding: 32px;
        transition: all 0.4s cubic-bezier(0.25, 1, 0.5, 1);
        height: 220px;
        margin-bottom: 20px;
    }

    .vector-card:hover {
        border-color: rgba(59, 130, 246, 0.5);
        background: rgba(22, 30, 49, 0.8);
        box-shadow: 0 15px 35px rgba(59, 130, 246, 0.2);
        transform: translateY(-4px);
    }

    .vector-card h3 {
        font-weight: 600;
        font-size: 1.35rem;
        color: #ffffff;
        margin-top: 0;
        margin-bottom: 12px;
        letter-spacing: -0.5px;
    }

    /* AI Console Box */
    .terminal-box {
        background: #01040a;
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        padding: 24px;
        font-family: 'JetBrains Mono', monospace;
        margin-bottom: 15px;
    }

    /* Premium Interface Buttons */
    .stButton>button {
        background: #ffffff !important;
        color: #030611 !important;
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

    /* High-End Sidebar Overrides */
    [data-testid="stSidebar"] {
        background-color: #050917 !important;
        border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 3. GLOBAL ROUTING OVERLAY (PERSISTENT SIDEBAR)
# ==========================================
with st.sidebar:
    st.markdown("<h2 style='font-weight:800; font-size:1.75rem; color:#ffffff; letter-spacing:-1px; margin-bottom:0;'>SemiPro</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#6b7280; font-size:0.85rem; margin-top:2px; letter-spacing:0.5px;'>Silicon Engineering Academy</p>", unsafe_allow_html=True)
    st.write("---")
    
    # Complete 8-Module Expanded Engineering Sequence Architecture Map
    navigation_vector = [
        "Home Dashboard", 
        "Module 1: CMOS Transistor Mechanics", 
        "Module 2: The CMOS Inverter & VTC",
        "Module 3: Combinational Gate Design",
        "Module 4: Sequential Elements & Delay",
        "Module 5: Logic Synthesis & SDC",
        "Module 6: Static Timing Analysis",
        "Module 7: Floorplanning & Placement",
        "Module 8: Clock Tree Synthesis & Routing"
    ]
    
    # Dynamically find index to guarantee safety if state jumps inside workspace
    if st.session_state.current_page in navigation_vector:
        current_index = navigation_vector.index(st.session_state.current_page)
    else:
        current_index = 0
        
    selected_sidebar_page = st.radio("System Execution Tracks:", navigation_vector, index=current_index)
    
    if selected_sidebar_page != st.session_state.current_page:
        st.session_state.current_page = selected_sidebar_page
        st.rerun()

# ==========================================
# 4. MAIN ACTION INTERFACE ROUTING
# ==========================================
st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)

# DASHBOARD CONTROLLER LAYER
if st.session_state.current_page == "Home Dashboard":
    st.markdown("<h1 style='font-weight:800; font-size:2.8rem; letter-spacing:-1.5px; color:#ffffff; margin-bottom:8px;'>SemiPro Academy</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:1.15rem; color:#9ca3af; font-weight:300; margin-bottom:40px;'>An elite, unstructured physical design knowledge tree, mapped from absolute scratch to sign-off tapeout.</p>", unsafe_allow_html=True)
    
    st.subheader("Launch Workspace Pipelines")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<div class='vector-card'><h3>Module 1: CMOS Mechanics</h3><p>Isolate NMOS/PMOS transistor operational physics, threshold variances, and saturation current calculation boundaries.</p></div>", unsafe_allow_html=True)
        if st.button("Open Module 1 Workspace", use_container_width=True): 
            st.session_state.current_page = "Module 1: CMOS Transistor Mechanics"
            st.rerun()
            
    with col2:
        st.markdown("<div class='vector-card'><h3>Module 6: Static Timing Analysis</h3><p>Formulate setup and hold boundaries, track sequential clock uncertainties, and evaluate path slacks systematically.</p></div>", unsafe_allow_html=True)
        if st.button("Open Module 6 Workspace", use_container_width=True): 
            st.session_state.current_page = "Module 6: Static Timing Analysis"
            st.rerun()
            
    with col3:
        st.markdown("<div class='vector-card'><h3>Module 8: CTS & Routing</h3><p>Manage clock networks, isolate insertion delays, minimize clock skew metrics, and route cells around physical layout blockages.</p></div>", unsafe_allow_html=True)
        if st.button("Open Module 8 Workspace", use_container_width=True): 
            st.session_state.current_page = "Module 8: Clock Tree Synthesis & Routing"
            st.rerun()

# MODULE VIEWPORTS (With Global Navigation Safe Jumps)
elif st.session_state.current_page == "Module 1: CMOS Transistor Mechanics":
    st.markdown("### 🗺️ Navigation Node: You are inside Module 1")
    if st.button("🏠 Click here to view all modules (Return Home)"):
        st.session_state.current_page = "Home Dashboard"
        st.rerun()
        
    st.write("---")
    st.markdown("<h1>Module 1: CMOS Transistor Mechanics</h1>", unsafe_allow_html=True)
    st.latex(r"I_{d\_sat} = \frac{1}{2} \mu C_{ox} \frac{W}{L} (V_{gs} - V_{th})^2")
    st.info("Silicon Foundation parameters initialized. Use the sidebar at any time to hop directly to any other track layer.")

elif st.session_state.current_page == "Module 6: Static Timing Analysis":
    st.markdown("### 🗺️ Navigation Node: You are inside Module 6")
    if st.button("🏠 Click here to view all modules (Return Home)"):
        st.session_state.current_page = "Home Dashboard"
        st.rerun()
        
    st.write("---")
    st.markdown("<h1>Module 6: Static Timing Analysis (STA)</h1>", unsafe_allow_html=True)
    st.info("Timing vector analysis engine active. Calculate data arrival slacks or ask questions below.")

# MODULE 8 DEEP DEPLOYMENT INTERFACE
elif st.session_state.current_page == "Module 8: Clock Tree Synthesis & Routing":
    st.markdown("### 🗺️ Navigation Node: You are inside Module 8")
    
    # Accessible Map Quick-Link Button right inside the workspace view
    if st.button("🏠 Click here to view all modules (Return Home)"):
        st.session_state.current_page = "Home Dashboard"
        st.rerun()
        
    st.write("---")
    st.markdown("<h1>Module 8: Clock Tree Synthesis & Routing</h1>", unsafe_allow_html=True)
    st.markdown("#### Physical Layout Routing Core")
    st.write("""
    * **Clock Distribution Structure:** Balancing H-Tree, Trunk, and clock mesh layouts to compress global skew windows.
    * **Routing Optimization Matrix:** Eliminating signal integrity cross-coupling noise parameters ($C_{crosstalk}$) via shield tracks.
    """)
    st.success("Module 8 Core Online. The persistent sidebar on the left lets you view or switch modules instantly at any time.")

# FALLBACK HOOKS FOR INTERMEDIARY MODULES
else:
    st.markdown("### 🗺️ Navigation Node")
    if st.button("🏠 Click here to view all modules (Return Home)"):
        st.session_state.current_page = "Home Dashboard"
        st.rerun()
    st.write("---")
    st.markdown(f"<h1>{st.session_state.current_page}</h1>", unsafe_allow_html=True)
    st.info("Workspace environment online. Content matrix layer ready for textbook data stream mapping injections.")

st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# 5. INTEGRATED INTERACTIVE AI TERMINAL CHAT
# ==========================================
st.write("---")
st.markdown("<h3 style='font-weight:600; color:#ffffff; font-size:1.2rem; letter-spacing:-0.5px;'>🎛 ... Real-Time Silicon AI Evaluation Engine</h3>", unsafe_allow_html=True)

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
                ai_response_text = f"Telemetry Loop Verified: Received '{chat_query}'. Once your operational API key is integrated in the secrets panel, this line executes real-time code assessment."
                
        st.session_state.chat_history.append({"role": "ai", "text": ai_response_text})
        st.rerun()
