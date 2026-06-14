import streamlit as st

def render_phase_4():
    st.markdown("<h2 style='font-weight:700; color:#ffffff; margin-bottom:5px;'>Phase 4: Logic Synthesis & Optimization</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#9ca3af; font-size:1.05rem; margin-bottom:30px;'>Translate synthesizable RTL structures into gate-level primitives bounded by library parameters.</p>", unsafe_allow_html=True)
    
    # Segmenting Synthesis into 4 comprehensive sub-modules
    tab1, tab2, tab3, tab4 = st.tabs([
        "Module 4.1: Technology Mapping", 
        "Module 4.2: SDC Clock Formulation", 
        "Module 4.3: Boundary IO Delays", 
        "Module 4.4: Wire Load & Areas"
    ])
    
    with tab1:
        st.markdown("### The Library Translation Matrix")
        st.write("""
        * **Liberty Files (.lib):** Reading timing, power, and functional properties of standard cells at specific process corners.
        * **Gate Selection:** How the synthesis tool maps Boolean equations to target cells to meet user constraints for area, speed, and power.
        """)
        
    with tab2:
        st.markdown("### Creating Primary and Generated Clocks")
        st.write("""
        * **Primary SDC Clocks:** Defining frequency and initial phase edges using the `create_clock` syntax constraint.
        * **Internal Derivations:** Modeling clock dividers, multipliers, and phase-locked loop (PLL) outputs safely using `create_generated_clock`.
        """)
        
    with tab3:
        st.markdown("### Port Constraints & Boundaries")
        st.write("""
        * **Input Delay Limits:** Constraining input port timings (`set_input_delay`) to account for signal propagation times outside the chip.
        * **Output Delay Limits:** Reserving timing margin for external circuitry (`set_output_delay`) relative to the interface clock edge.
        """)
        
    with tab4:
        st.markdown("### Wire Load Interconnect Approximations")
        st.write("""
        * **Pre-Layout Estimations:** Using wire-load models (WLM) to estimate RC resistance and capacitance before cell placement.
        * **Area vs. Speed Tuning:** Resolving critical path violations by swapping standard-threshold cells (SVTH) for high-speed low-threshold cells (LVTH).
        """)
        
    # Practice Sandbox dedicated strictly to Phase 4 content
    st.write("---")
    st.markdown("<h4 style='font-weight:600; color:#4facfe;'>Phase 4 Diagnostic Sandbox</h4>", unsafe_allow_html=True)
    st.info("Challenge: An engineer writes an SDC file but sets a clock uncertainty value that is way too low. How does this impact the synthesis tool's choices regarding cell sizes, and what happens when the design reaches real hardware?")
    
    st.text_area("Input your synthesis analysis script here:", placeholder="Analyze constraint uncertainty parameters...", key="p4_sandbox_input")
    if st.button("Submit Phase 4 Analysis"):
        st.success("Telemetry saved. Verification engine ready.")
