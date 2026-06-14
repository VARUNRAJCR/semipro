import streamlit as st

def render_phase_1():
    st.markdown("<h2 style='font-weight:700; color:#ffffff; margin-bottom:5px;'>Phase 1: CMOS Deep Dive Workspace</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#9ca3af; font-size:1.05rem; margin-bottom:30px;'>Isolate device physics parameters, threshold voltage variances, and switching profiles.</p>", unsafe_allow_html=True)
    
    # Segmenting into comprehensive sub-modules using clean tabs
    tab1, tab2, tab3, tab4 = st.tabs([
        "Module 1.1: NMOS/PMOS Physics", 
        "Module 1.2: Current Equations", 
        "Module 1.3: The Inverter VTC", 
        "Module 1.4: Fabrication Realities"
    ])
    
    with tab1:
        st.markdown("### MOSFET Structural Mechanics")
        st.write("""
        * **Operational Regions:** Deep mathematical boundaries defining Cut-off, Linear, and Saturation zones.
        * **Threshold Voltage ($V_{th}$):** Factors dictating the inversion layer formation, body effect coefficients, and doping concentration scaling metrics.
        """)
        
    with tab2:
        st.markdown("### Drain Current Formulations")
        st.write("Evaluating drift velocities, carrier mobility degradation, and channel-length modulation ($\lambda$).")
        st.latex(r"I_{d\_sat} = \frac{1}{2} \mu C_{ox} \frac{W}{L} (V_{gs} - V_{th})^2 (1 + \lambda V_{ds})")
        
    with tab3:
        st.markdown("### Symmetrical Switching Profiles")
        st.write("""
        * **VTC Characteristics:** Midpoint switching voltages ($V_{sp}$), Noise Margin High ($NM_H$), and Noise Margin Low ($NM_L$).
        * **Sizing Rules:** Sizing the PMOS width relative to NMOS ($W_p / W_n$) to compensate for lower hole mobility.
        """)
        
    with tab4:
        st.markdown("### Sub-Micron Leakage & Parasitics")
        st.write("""
        * **Parasitic Capacitances:** Overlap capacitance, gate-to-source channel profiles, and source/drain depletion junctions.
        * **Short-Channel Effects:** Drain-Induced Barrier Lowering (DIBL), subthreshold conduction leaks, and gate-oxide tunneling.
        """)
        
    # Practice Sandbox dedicated strictly to Phase 1 content
    st.write("---")
    st.markdown("<h4 style='font-weight:600; color:#4facfe;'>Phase 1 Diagnostic Sandbox</h4>", unsafe_allow_html=True)
    st.info("Challenge: If a fabrication shift compromises the gate oxide layer, thickness ($t_{ox}$) increases. Detail the analytical impact on $C_{ox}$ and overall execution delay.")
    
    st.text_area("Input your physics-based explanation script here:", placeholder="Analyze derivative capacitance properties...", key="p1_sandbox_input")
    if st.button("Submit Phase 1 Analysis"):
        st.success("Telemetry saved. Verification engine ready.")
