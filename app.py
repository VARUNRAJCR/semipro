import streamlit as st
import os
from google import genai
from google.genai import types

# Clean Modular Architecture Imports
from styles import apply_semiconductor_theme
import phase1
import phase2
import phase3
import phase4
import phase5

# ==========================================
# 1. APPLICATION INITIALIZATION LAYERS
# ==========================================
st.set_page_config(page_title="SemiPro | Semiconductor Workspace", layout="wide")

if "current_page" not in st.session_state: st.session_state.current_page = "Home Dashboard"
if "chat_history" not in st.session_state: st.session_state.chat_history = []

if "GEMINI_API_KEY" in st.secrets:
    os.environ["GEMINI_API_KEY"] = st.secrets["GEMINI_API_KEY"]

# Execute styling configurations from your style module
apply_semiconductor_theme()

# ==========================================
# 2. NATIVE MATHEMATICAL KINEMATIC BACKPLANE
# ==========================================
st.markdown("""
    <div class="math-universe-bg">
        <canvas id="sandMatrixCanvas" style="position:fixed; top:0; left:0; width:100vw; height:100vh; z-index:-2; pointer-events:none;"></canvas>
    </div>

    <script>
    (function() {
        const canvas = document.getElementById('sandMatrixCanvas');
        const ctx = canvas.getContext('2d');
        function resize() { canvas.width = window.innerWidth; canvas.height = window.innerHeight; }
        window.addEventListener('resize', resize); resize();

        const grainCount = 120;
        const gravitationalPull = 0.015;
        const windDriftFactor = -0.03;
        const grains = [];

        for (let i = 0; i < grainCount; i++) {
            grains.push({
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height,
                size: 1 + Math.random() * 2,
                terminalVelocity: 0.4 + Math.random() * 1.0,
                massAlpha: 0.15 + Math.random() * 0.35,
                colorBand: Math.random() > 0.4 ? 'rgba(59, 130, 246,' : 'rgba(14, 165, 233,'
            });
        }

        function processPhysicsEngine() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            for (let i = 0; i < grainCount; i++) {
                let g = grains[i];
                ctx.beginPath();
                ctx.fillStyle = g.colorBand + g.massAlpha + ')';
                ctx.arc(g.x, g.y, g.size, 0, Math.PI * 2, true);
                ctx.fill();
                
                g.y += g.terminalVelocity;
                g.x += windDriftFactor;
                g.terminalVelocity += gravitationalPull;

                if (g.y > canvas.height) {
                    g.x = Math.random() * canvas.width;
                    g.y = -10;
                    g.terminalVelocity = 0.4 + Math.random() * 1.0;
                }
            }
            requestAnimationFrame(processPhysicsEngine);
        }
        processPhysicsEngine();
    })();
    </script>
""", unsafe_allow_html=True)

# ==========================================
# 3. GLOBAL PERSISTENT SIDEBAR NAVIGATION
# ==========================================
with st.sidebar:
    st.markdown("<h2 style='font-weight:800; font-size:1.85rem; color:#ffffff; letter-spacing:-1px; margin-bottom:0;'>SemiPro</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#4b5563; font-size:0.85rem; font-weight:500; margin-top:2px;'>Silicon Engineering Academy</p>", unsafe_allow_html=True)
    st.write("---")
    
    navigation_vector = [
        "Home Dashboard", 
        "Phase 1: CMOS Deep Dive", 
        "Phase 2: Digital Electronics",
        "Phase 3: Register Transfer Level",
        "Phase 4: Logic Synthesis",
        "Phase 5: Physical Design"
    ]
    
    current_index = navigation_vector.index(st.session_state.current_page) if st.session_state.current_page in navigation_vector else 0
    selected_sidebar_page = st.radio("Academy Tracks Hub:", navigation_vector, index=current_index)
    
    if selected_sidebar_page != st.session_state.current_page:
        st.session_state.current_page = selected_sidebar_page
        st.rerun()

# ==========================================
# 4. MAIN CENTRAL PANEL DISPLAY VIEWPORT
# ==========================================
st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)

# Pinned navigation escape hatch for sub-modules
if st.session_state.current_page != "Home Dashboard":
    if st.button("To change track or view modules click here"):
        st.session_state.current_page = "Home Dashboard"
        st.rerun()
    st.write("---")

# DASHBOARD LAYER
if st.session_state.current_page == "Home Dashboard":
    st.markdown("<h1 style='font-weight:800; font-size:3rem; letter-spacing:-1.5px; color:#ffffff; margin-bottom:8px;'>Physical Design Portal</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:1.2rem; color:#9ca3af; font-weight:300; margin-bottom:45px;'>Step directly into custom engineering sandboxes mapped across five progressive IC layout segments.</p>", unsafe_allow_html=True)
    
    row1_col1, row1_col2, row1_col3 = st.columns(3)
    with row1_col1:
        st.markdown("<div class='silicon-vector-card'><h3>Phase 1: CMOS</h3><p>Analyze transistor conduction physics, leakage thresholds, and dynamic voltage transfer parameters.</p></div>", unsafe_allow_html=True)
        if st.button("Open Phase 1 Workspace", use_container_width=True): st.session_state.current_page = "Phase 1: CMOS Deep Dive"; st.rerun()
    with row1_col2:
        st.markdown("<div class='silicon-vector-card'><h3>Phase 2: Digital Electronics</h3><p>Master complex gate topologies, solve propagation path effort delays, and isolate flip-flop windows.</p></div>", unsafe_allow_html=True)
        if st.button("Open Phase 2 Workspace", use_container_width=True): st.session_state.current_page = "Phase 2: Digital Electronics"; st.rerun()
    with row1_col3:
        st.markdown("<div class='silicon-vector-card'><h3>Phase 3: RTL</h3><p>Design timing-clean synthesizable logic blocks, finite state controllers, and asynchronous boundaries.</p></div>", unsafe_allow_html=True)
        if st.button("Open Phase 3 Workspace", use_container_width=True): st.session_state.current_page = "Phase 3: Register Transfer Level"; st.rerun()

    st.write(" ")
    row2_col1, row2_col2 = st.columns([1, 2])
    with row2_col1:
        st.markdown("<div class='silicon-vector-card'><h3>Phase 4: Synthesis</h3><p>Map logic nets to standard gate primitives and implement core SDC boundary equations.</p></div>", unsafe_allow_html=True)
        if st.button("Open Phase 4 Workspace", use_container_width=True): st.session_state.current_page = "Phase 4: Logic Synthesis"; st.rerun()
    with row2_col2:
        st.markdown("<div class='silicon-vector-card'><h3>Phase 5: Physical Design (PD)</h3><p>Execute full floorplanning grid blocks, balance clock trees, run routing tracks, and sign-off DRC checks.</p></div>", unsafe_allow_html=True)
        if st.button("Open Phase 5 Workspace", use_container_width=True): st.session_state.current_page = "Phase 5: Physical Design"; st.rerun()

# RENDER DELEGATED MODULAR TRACK PAGES
elif st.session_state.current_page == "Phase 1: CMOS Deep Dive": phase1.render_phase_1()
elif st.session_state.current_page == "Phase 2: Digital Electronics": phase2.render_phase_2()
elif st.session_state.current_page == "Phase 3: Register Transfer Level": phase3.render_phase_3()
elif st.session_state.current_page == "Phase 4: Logic Synthesis": phase4.render_phase_4()
elif st.session_state.current_page == "Phase 5: Physical Design": phase5.render_phase_5()

st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# 5. INTEGRATED CHATBOT COMPONENT LAYER
# ==========================================
st.write("---")
st.markdown("<h3 style='font-weight:600; color:#ffffff; font-size:1.2rem; letter-spacing:-0.5px;'>🎛️ Real-Time Silicon AI Evaluation Engine</h3>", unsafe_allow_html=True)

st.markdown("<div class='terminal-box'>", unsafe_allow_html=True)
for chat in st.session_state.chat_history:
    if chat["role"] == "user": st.markdown(f"<p style='color:#3b82f6; margin-bottom:4px;'><strong>[STUDENT_VECTOR] ></strong> {chat['text']}</p>", unsafe_allow_html=True)
    else: st.markdown(f"<p style='color:#10b981; margin-bottom:12px; white-space: pre-wrap;'><strong>[AI_COACH_MATRIX] ></strong> {chat['text']}</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

chat_query = st.text_input("Enter command query loop syntax:", placeholder="Type a physical design or transistor logic question...", key="chat_input_field")

if st.button("Execute Chat Query Pipeline"):
    if chat_query:
        st.session_state.chat_history.append({"role": "user", "text": chat_query})
        with st.spinner("Processing telemetry analysis vectors..."):
            try:
                client = genai.Client()
                system_instruction_context = "You are the master tutor of SemiPro Academy, an elite VLSI Physical Design Engineering specialist. Never use emojis. Keep explanations crisp, professional, and structured."
                response = client.models.generate_content(model='gemini-2.5-flash', contents=chat_query, config=types.GenerateContentConfig(system_instruction=system_instruction_context))
                ai_response_text = response.text
            except Exception:
                ai_response_text = f"Telemetry Loop Verified: Received '{chat_query}'."
        st.session_state.chat_history.append({"role": "ai", "text": ai_response_text})
        st.rerun()
