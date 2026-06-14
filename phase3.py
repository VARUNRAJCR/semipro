import streamlit as st

def render_phase_3():
    st.markdown("<h2 style='font-weight:700; color:#ffffff; margin-bottom:5px;'>Phase 3: Register Transfer Level (RTL) Workspace</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#9ca3af; font-size:1.05rem; margin-bottom:30px;'>Structure synthesizable logic codes, state machines, and clock-crossing synchronization boundaries.</p>", unsafe_allow_html=True)
    
    # Segmenting RTL into 4 comprehensive sub-modules
    tab1, tab2, tab3, tab4 = st.tabs([
        "Module 3.1: Synthesizable Verilog", 
        "Module 3.2: FSM & Control Paths", 
        "Module 3.3: Clock Domain Crossing", 
        "Module 3.4: RTL Rules & Linting"
    ])
    
    with tab1:
        st.markdown("### Structural vs. Behavioral Code Layouts")
        st.write("""
        * **Synthesizable Constructs:** Writing deterministic code logic that maps cleanly to physical gates. Avoiding simulation-only constructs (like initial blocks, delays `#`, or loops without bounds).
        * **Blocking vs. Non-Blocking Assignments:** Mastering code behaviors (`=` vs `<=`) to prevent simulation-synthesis mismatches.
        """)
        
    with tab2:
        st.markdown("### Finite State Machine (FSM) Design")
        st.write("""
        * **Mealy vs. Moore Architectures:** Comparing state register logic, output calculation profiles, and timing implications.
        * **State Encoding Styles:** Implementing Binary, Gray, and One-Hot encoding to trade off lookahead logic delay versus power optimization.
        """)
        
    with tab3:
        st.markdown("### Clock Domain Crossing (CDC) Signals")
        st.write("""
        * **Data Stream Transfers:** Moving single-bit and multi-bit control buses safely between completely asynchronous clock trees.
        * **CDC Solutions:** Building 2-flip-flop synchronizers, toggle synchronizers, and asynchronous FIFO logic blocks.
        """)
        
    with tab4:
        st.markdown("### RTL Static Verification Layouts")
        st.write("""
        * **Linting Rules:** Identifying structural coding issues like inferred latches, un-driven nets, combinational feedback paths, and multi-driven registers.
        * **DFT Coding Rules:** Structuring hardware targets to cleanly support scan chains and manufacturing text insertions later.
        """)
        
    # Practice Sandbox dedicated strictly to Phase 3 content
    st.write("---")
    st.markdown("<h4 style='font-weight:600; color:#4facfe;'>Phase 3 Diagnostic Sandbox</h4>", unsafe_allow_html=True)
    st.info("Challenge: An engineer creates a combinational 'always' block but omits one of the input variables from the sensitivity list. Detail the compilation mismatch this creates between functional simulation and physical gate layout synthesis.")
    
    st.text_area("Input your RTL analysis script here:", placeholder="Analyze look-up table inference behaviors...", key="p3_sandbox_input")
    if st.button("Submit Phase 3 Analysis"):
        st.success("Telemetry saved. Verification engine ready.")
