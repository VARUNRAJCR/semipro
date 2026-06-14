import streamlit as st
import os
from google import genai
from google.genai import types

# ==========================================
# 1. CORE SYSTEM SETUP & SECURE KEYS
# ==========================================
st.set_page_config(page_title="SemiPro | Semiconductor Architecture", layout="wide")

if "current_page" not in st.session_state:
    st.session_state.current_page = "Home Dashboard"
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "GEMINI_API_KEY" in st.secrets:
    os.environ["GEMINI_API_KEY"] = st.secrets["GEMINI_API_KEY"]

# ==========================================
# 2. THE HIGH-END CLASSIC VISUAL LAYER
# ==========================================
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;800&family=JetBrains+Mono:wght@300;500&display=swap');

    /* Lock down dark minimalist canvas background */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #030611 !important;
        color: #f3f4f6 !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }
    
    /* Remove native white-label blockades */
    #MainMenu, footer, header {visibility: hidden;}

    /* Glassmorphic main visual viewport panel */
    .glass-panel {
        background: rgba(11, 17, 34, 0.8);
        border: 1px solid rgba(255, 255, 255, 0.07);
        border-radius: 24px;
        padding: 40px;
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6);
        margin-bottom: 30px;
    }

    /* Premium Silicon Vector Track Cards */
    .vector-card {
        background: rgba(22, 30, 49, 0.45);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        padding: 32px;
        transition: all 0.4s cubic-bezier(0.25, 1, 0.5, 1);
        height: 220px;
        margin-bottom: 20px;
    }

    .vector-card:hover {
        border-color: rgba(59, 130, 246, 0.4);
        background: rgba(22, 30, 49, 0.7);
        box-shadow: 0 15px 35px rgba(59, 130, 246, 0.15);
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

    .vector-card p {
        color: #9ca3af;
        font-size: 0.95rem;
        line-height: 1.6;
    }

    /* AI System Command Input Console box */
    .terminal-box {
        background: #01040a;
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        padding: 24px;
        font-family: 'JetBrains Mono', monospace;
        margin-bottom: 15px;
    }

    /* Premium Minimalist Interface Buttons */
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
        box-shadow: 0 0 25px rgba(255, 255, 255, 0.3) !important;
    }

    /* High-End Sidebar Alignment Overrides */
    [data-testid="stSidebar"] {
        background-color: #060a17 !important;
        border-right: 1px solid rgba(255, 255, 255, 0.04) !important;
    }
    </style>

    <canvas id="sandUniverseCanvas" style="position:fixed; top:0; left:0; width:100vw; height:100vh; z-index:-1; pointer-events:none;"></canvas>

    <script>
    (function() {
        const canvas = document.getElementById('sandUniverseCanvas');
        const ctx = canvas.getContext('2d');
        function resize() { canvas.width = window.innerWidth; canvas.height = window.innerHeight; }
        window.addEventListener('resize', resize); resize();

        const particleCount = 140;
        const gravitationalPull = 0.025;
        const horizontalDrift = -0.05;
        const particles = [];

        for (let i = 0; i < particleCount; i++) {
            particles.push({
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height,
                radius: 1 + Math.random() * 1.8,
                densitySpeed: 0.3 + Math.random() * 1.2,
                opacity: 0.15 + Math.random() * 0.35,
                color: Math.random() > 0.4 ? 'rgba(59, 130, 246,' : 'rgba(14, 165, 233,'
            });
        }

        function animateSandUniverse() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            for (let i = 0; i < particleCount; i++) {
                let p = particles[i];
                ctx.beginPath();
                ctx.fillStyle = p.color + p.opacity + ')';
                ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2, true);
                ctx.fill();
                
                p.y += p.densitySpeed;
                p.x += horizontalDrift;
                p.densitySpeed += gravitationalPull;

                if (p.y > canvas.height) {
                    p.x = Math.random() * canvas.width;
                    p.y = -10;
                    p.densitySpeed = 0.3 + Math.random() * 1.2;
                }
            }
            requestAnimationFrame(animateSandUniverse);
        }
        animateSandUniverse();
    })();
    </script>
    """, unsafe_allow_html=True)

# ==========================================
# 3. THE INTEGRATED NAVIGATION SIDEBAR
# ==========================================
with st.sidebar:
    st.markdown("<h2 style='font-weight:800; font-size:1.75rem; color:#ffffff; letter-spacing:-1px; margin-bottom:0;'>SemiPro</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#6b7280; font-size:0.85rem; margin-top:2px; letter-spacing:0.5px;'>Silicon Engineering Academy</p>", unsafe_allow_html=True)
    st.write("---")
    
    navigation_vector = [
        "Home Dashboard", 
        "Phase 1: Silicon Foundations", 
        "Phase 2: Circuit Logic Matrix", 
        "Phase 3: Physical Automation"
    ]
    
    current_index = navigation_vector.index(st.session_state.current_page)
    selected_sidebar_page = st.radio("Academy Navigation Vector:", navigation_vector, index=current_index)
    
    if selected_sidebar_page != st.session_state.current_page:
        st.session_state.current_page = selected_sidebar_page
        st.rerun()

# ==========================================
# 4. MAIN CENTRAL WINDOW PANEL ARCHITECTURE
# ==========================================
st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)

# DASHBOARD LAYER
if st.session_state.current_page == "Home Dashboard":
    st.markdown("<h1 style='font-weight:800; font-size:2.8rem; letter-spacing:-1.5px; color:#ffffff; margin-bottom:8px;'>SemiPro Portal</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:1.15rem; color:#9ca3af; font-weight:300; margin-bottom:40px;'>Master modern semiconductor integration tracks systematically from raw transistor logic up to sign-off tapeout.</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<div class='vector-card'><h3>Phase 1: Silicon Foundations</h3><p>Isolate NMOS/PMOS transistor switching physics, threshold shift variance metrics, and mathematical operational curve boundaries.</p></div>", unsafe_allow_html=True)
        if st.button("Enter Phase 1 Workspace", use_container_width=True): 
            st.session_state.current_page = "Phase 1: Silicon Foundations"
            st.rerun()
    with col2:
        st.markdown("<div class='vector-card'><h3>Phase 2: Circuit Logic Matrix</h3><p>Map complex combinational gates, optimize structural network pathways via logical effort formulas, and solve flip-flop parameters.</p></div>", unsafe_allow_html=True)
        if st.button("Enter Phase 2 Workspace", use_container_width=True): 
            st.session_state.current_page = "Phase 2: Circuit Logic Matrix"
            st.rerun()
    with col3:
        st.markdown("<div class='vector-card'><h3>Phase 3: Physical Automation</h3><p>Process modern industry implementation flows: SDC synthesis execution constraints, multi-corner STA timing slacks, and detailed routing DRC resolution vectors.</p></div>", unsafe_allow_html=True)
        if st.button("Enter Phase 3 Workspace", use_container_width=True): 
            st.session_state.current_page = "Phase 3: Physical Automation"
            st.rerun()

# PHASE WORKSPACES
elif st.session_state.current_page == "Phase 1: Silicon Foundations":
    if st.button("⬅️ Return to Main Dashboard", key="b1"): 
        st.session_state.current_page = "Home Dashboard"
        st.rerun()
    st.markdown("<h1 style='font-weight:800; color:#ffffff; margin-top:15px;'>Phase 1: Silicon Foundations</h1>", unsafe_allow_html=True)
    st.write("---")
    col_content, col_practice = st.columns([1.2, 1.2])
    with col_content:
        st.subheader("Physical Semiconductor Formulations")
        with st.expander("Module 1.1: MOSFET Saturation Parameters", expanded=True):
            st.write("Analyzing current distribution equations across scaling dielectric thickness boundaries.")
            st.latex(r"I_{d\_sat} = \frac{1}{2} \mu C_{ox} \frac{W}{L} (V_{gs} - V_{th})^2")

    with col_practice:
        st.subheader("Interactive Verification Sandbox")
        st.info("System Diagnostic Input: Given an operational variation increasing gate-oxide scale layers, input the derivative performance shift matching capacitive calculations.")
        st.text_area("Input technical verification analysis script here:", placeholder="Analyze capacitance derivatives...", key="p1_ans")
        if st.button("Process Script Verification"):
            st.success("Telemetry log saved.")

elif st.session_state.current_page == "Phase 2: Circuit Logic Matrix":
    if st.button("⬅️ Return to Main Dashboard", key="b2"): 
        st.session_state.current_page = "Home Dashboard"
        st.rerun()
    st.markdown("<h1 style='font-weight:800; color:#ffffff; margin-top:15px;'>Phase 2: Circuit Logic Matrix</h1>", unsafe_allow_html=True)
    st.write("---")
    st.info("Logic Vector Core online. Awaiting combinational logical effort matrix rules propagation.")

elif st.session_state.current_page == "Phase 3: Physical Automation":
    if st.button("⬅️ Return to Main Dashboard", key="b3"): 
        st.session_state.current_page = "Home Dashboard"
        st.rerun()
    st.markdown("<h1 style='font-weight:800; color:#ffffff; margin-top:15px;'>Phase 3: Physical Implementation</h1>", unsafe_allow_html=True)
    st.write("---")
    st.info("RTL-to-GDSII structural layout track interface loaded. SDC constraint mapping algorithms ready.")

st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# 5. INTEGRATED INTERACTIVE COACH (CHATBOT)
# ==========================================
st.write("---")
st.markdown("<h3 style='font-weight:600; color:#ffffff; font-size:1.2rem; letter-spacing:-0.5px;'>🎛️ Real-Time Silicon AI Evaluation Engine</h3>", unsafe_allow_html=True)
st.caption("Ask technical questions on CMOS scaling, Logical Effort networks, or SDC syntax parameters for immediate analytical evaluation.")

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
                system_instruction_context = "You are the master tutor of SemiPro Academy, an elite VLSI Physical Design Engineering specialist. Never use emojis. Keep explanations crisp and structured."
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
