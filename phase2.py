import streamlit as st

def render_phase_2():
    st.markdown("<h2 style='font-weight:700; color:#ffffff; margin-bottom:5px;'>Phase 2: Digital Electronics Matrix</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#9ca3af; font-size:1.05rem; margin-bottom:30px;'>Master gate topologies, optimize delay paths, and solve sequential timing requirements.</p>", unsafe_allow_html=True)
    
    # Segmenting Digital Electronics into 4 comprehensive sub-modules
    tab1, tab2, tab3, tab4 = st.tabs([
        "Module 2.1: Combinational Logic", 
        "Module 2.2: Logical Effort Math", 
        "Module 2.3: Sequential Elements", 
        "Module 2.4: Clock Hazards & Metastability"
    ])
    
    with tab1:
        st.markdown("### Static CMOS Gate Topology")
        st.write("""
        * **Gate Construction:** Building NAND, NOR, XOR, and complex And-Or-Invert (AOI) / Or-And-Invert (OAI) structures from transistor networks.
        * **Sizing for Balance:** Sizing series and parallel pull-up/pull-down networks to match worst-case rise and fall times ($T_{rise} / T_{fall}$).
        """)
        
    with tab2:
        st.markdown("### Path Delay Optimization (Logical Effort)")
        st.write("""
        * **The Linear Delay Model:** Understanding parasitic delay ($p$) and logical effort ($g$) of standard gates.
        * **Asymmetry Mitigation:** Calculating path logical effort ($G$), branching effort ($B$), and electrical effort ($H$) to determine absolute fastest transistor sizes.
        """)
        st.latex(r"D = \sum (g_i h_i + p_i)")
        
    with tab3:
        st.markdown("### Sequential Circuits & Latches")
        st.write("""
        * **Storage Mechanics:** Transparent latches versus edge-triggered master-slave flip-flops.
        * **Timing Constraints:** Defining internal setup times ($T_{setup}$), hold times ($T_{hold}$), and clock-to-Q propagation delays ($T_{clk-to-q}$).
        """)
        
    with tab4:
        st.markdown("### Timing Failure Mechanics")
        st.write("""
        * **Metastability:** What happens when data violates setup/hold windows, causing the bistable element to hang between logic states.
        * **MTBF & Synchronizers:** Calculating Mean Time Between Failures (MTBF) and designing multi-stage synchronizers for async boundaries.
        """)
        
    # Practice Sandbox dedicated strictly to Phase 2 content
    st.write("---")
    st.markdown("<h4 style='font-weight:600; color:#4facfe;'>Phase 2 Diagnostic Sandbox</h4>", unsafe_allow_html=True)
    st.info("Challenge: A data signal arrives right at the active clock edge, violating the flip-flop's setup window. Explain the internal electrical behavior and how this creates metastability.")
    
    st.text_area("Input your logical analysis script here:", placeholder="Analyze the feedback loop state...", key="p2_sandbox_input")
    if st.button("Submit Phase 2 Analysis"):
        st.success("Telemetry saved. Verification engine ready.")
