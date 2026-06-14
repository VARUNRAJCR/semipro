import streamlit as st

def render_phase_5():
    st.markdown("<h2 style='font-weight:700; color:#ffffff; margin-bottom:5px;'>Phase 5: Physical Design (PD) Implementation</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#9ca3af; font-size:1.05rem; margin-bottom:30px;'>Execute floorplanning, optimize placement grids, balance clock tree distribution paths, and route interconnect networks.</p>", unsafe_allow_html=True)
    
    # Segmenting Physical Design into 4 comprehensive sub-modules
    tab1, tab2, tab3, tab4 = st.tabs([
        "Module 5.1: Floorplanning & PNS", 
        "Module 5.2: Cell Placement & STA", 
        "Module 5.3: Clock Tree Synthesis", 
        "Module 5.4: Routing & Physical Sign-off"
    ])
    
    with tab1:
        st.markdown("### Structural Die Architecture Mapping")
        st.write("""
        * **Floorplan Frameworks:** Calculating core area targets, aspect ratio, and boundary cell configurations.
        * **Macro Rules:** Defining macro channel spaces, obstruction blocks, and halo configurations.
        * **Power Network Synthesis (PNS):** Designing VDD/VSS rings, horizontal/vertical straps, and standard cell rails to control dynamic IR drop.
        """)
        
    with tab2:
        st.markdown("### Standard Cell Legalization & Timing Analysis")
        st.write("""
        * **Placement Phases:** Global placement congestion profiling followed by legal coarse row cell mapping.
        * **STA Sign-off Calculations:** Formulating setup and hold data required margins, tracking slack paths, and fixing bottlenecks with sizing modifications.
        """)
        st.latex(r"\text{Setup Slack} = T_{required} - T_{arrival}")
        
    with tab3:
        st.markdown("### Balancing Clock Distribution Trees")
        st.write("""
        * **CTS Metrics:** Balancing clock tree topologies (H-Tree, Trunk, or Mesh networks) to hit global and local skew targets.
        * **Insertion Delay Controls:** Scaling buffers and clock gates to compress insertion latency and limit clock power.
        """)
        
    with tab4:
        st.markdown("### Routing Interconnects & DRC Sign-off")
        st.write("""
        * **Routing Architecture:** Global grid tracking, cell pad track attachments, and detailed metal layer routing assignments.
        * **Signal Integrity:** Correcting crosstalk noise delays and cross-coupling glitches using metal shield lines.
        * **Physical Verification:** Running layout sign-off rules like Design Rule Checks (DRC) for metal spacing, and Layout vs. Schematic (LVS) comparison checks.
        """)
        
    # Practice Sandbox dedicated strictly to Phase 5 content
    st.write("---")
    st.markdown("<h4 style='font-weight:600; color:#4facfe;'>Phase 5 Diagnostic Sandbox</h4>", unsafe_allow_html=True)
    st.info("Challenge: During post-route timing evaluation, a data line encounters a massive hold time violation. Explain why you cannot solve this violation by simply increasing the clock frequency, and outline the proper physical fix.")
    
    st.text_area("Input your physical design analysis script here:", placeholder="Analyze delay buffer insertions...", key="p5_sandbox_input")
    if st.button("Submit Phase 5 Analysis"):
        st.success("Telemetry saved. Verification engine ready.")
