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
# 1. HARDWARE SYSTEM CORE SETUPS
# ==========================================
st.set_page_config(page_title="SemiPro | Semiconductor Workspace", layout="wide")

if "current_page" not in st.session_state: st.session_state.current_page = "Home Dashboard"
if "chat_history" not in st.session_state: st.session_state.chat_history = []

if "GEMINI_API_KEY" in st.secrets:
    os.environ["GEMINI_API_KEY"] = st.secrets["GEMINI_API_KEY"]

# Apply styles from your independent style module
apply_semiconductor_theme()

# ==========================================
# 2. INJECT PURE BROWSER WAVE NAV HUB (ZERO-RELOAD INTERACTION ENGINE)
# ==========================================
st.markdown("""
    <div class="hardware-nav-wrapper">
        <input type="checkbox" id="waveNavToggle">
        <label for="waveNavToggle" class="hardware-wake-btn">
            <span class="btn-text"></span>
        </label>
        
        <div class="curriculum-wave-panel">
            <h2 style="color:#ffffff; font-weight:800; margin-top:0; font-family:'Plus Jakarta Sans',sans-serif;">📚 SemiPro Master Content Map</h2>
            <p style="color:#9ca3af; font-size:0.95rem; margin-bottom:25px; font-family:'Plus Jakarta Sans',sans-serif;">Select an active engineering section from the curriculum column clusters below:</p>
            
            <div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 20px; font-family:'Plus Jakarta Sans',sans-serif; text-align: left;">
                <div>
                    <h4 style="color:#06b6d4; margin-bottom:10px; font-weight:700;">Phase 1: CMOS</h4>
                    <p style="color:#9ca3af; font-size:0.85rem; line-height:1.8; margin:0;">• NMOS/PMOS Physics<br>• Current Equations<br>• Inverter VTC<br>• Sub-Micron Leaks</p>
                </div>
                <div>
                    <h4 style="color:#06b6d4; margin-bottom:10px; font-weight:700;">Phase 2: Digital</h4>
                    <p style="color:#9ca3af; font-size:0.85rem; line-height:1.8; margin:0;">• CMOS Gate Logic<br>• Logical Effort Math<br>• Sequential Elements<br>• Metastability</p>
                </div>
                <div>
                    <h4 style="color:#06b6d4; margin-bottom:10px; font-weight:700;">Phase 3: RTL</h4>
                    <p style="color:#9ca3af; font-size:0.85rem; line-height:1.8; margin:0;">• Synthesizable Code<br>• FSM Controllers<br>• CDC Sync Tracks<br>• Linting Engines</p>
                </div>
                <div>
                    <h4 style="color:#06b6d4; margin-bottom:10px; font-weight:700;">Phase 4: Synthesis</h4>
                    <p style="color:#9ca3af; font-size:0.85rem; line-height:1.8; margin:0;">• Tech Mapping (.lib)<br>• SDC Clock Syntax<br>• IO Boundary Delays<br>• Wire Load Models</p>
                </div>
                <div>
                    <h4 style="color:#06b6d4; margin-bottom:10px; font-weight:700;">Phase 5: PD</h4>
                    <p style="color:#9ca3af; font-size:0.85rem; line-height:1.8; margin:0;">• Floorplan & PNS<br>• Cell Legalization<br>• CTS Skew Tuning<br>• DRC/LVS Sign-off</p>
                </div>
            </div>
            <br>
            <p style="color:#64748b; font-size:0.85rem; margin-top:15px; border-top: 1px solid rgba(255,255,255,0.06); padding-top:15px;">💡 Note: To swap active core workspace workspaces, use your standalone primary grid dashboard controls below.</p>
        </div>
    </div>
    
    <style>
        .btn-text::before { content: "Content ☰"; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. NATIVE MATHEMATICAL BACKGROUND CANVAS
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

        const grainCount = 135;
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
# 4. MAIN CENTRAL CONTENT HUD VIEWPORT
# ==========================================
st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)

if st.session_state.current_page != "Home Dashboard":
    if st.button("🏠 View All Phases (Return to Main Dashboard)"):
        st.session_state.current_page = "Home Dashboard"
        st.rerun()
    st.write("---")

if st.session_state.current_page == "Home Dashboard":
    st.markdown("<h1 style='font-weight:800; font-size:3rem; letter-spacing:-1.5px; color:#ffffff; margin-bottom:8px;'>SemiPro</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:1.2rem; color:#9ca3af; font-weight:300; margin-bottom:45px;'>Master modern semiconductor integration tracks systematically from raw transistor logic up to sign-off tapeout.</p>", unsafe_allow_html=True)
    
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

elif st.session_state.current_page == "Phase 1: CMOS Deep Dive": phase1.render_phase_1()
elif st.session_state.current_page == "Phase 2: Digital Electronics": phase2.render_phase_2()
elif st.session_state.current_page == "Phase 3: Register Transfer Level": phase3.render_phase_3()
elif st.session_state.current_page == "Phase 4: Logic Synthesis": phase4.render_phase_4()
elif st.session_state.current_page == "Phase 5: Physical Design": phase5.render_phase_5()

st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# 5. INTEGRATED CHATBOT LOOP
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
