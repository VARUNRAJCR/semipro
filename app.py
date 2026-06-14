import streamlit as st
import os
from google import genai
from google.genai import types

# 1. Branding SemiPro on Browser Tab
st.set_page_config(page_title="SemiPro | VLSI Academy", page_icon="🎛️", layout="wide")

# Hide default headers for a clean, custom app look
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Secure API Token mapping for later use
if "GEMINI_API_KEY" in st.secrets:
    os.environ["GEMINI_API_KEY"] = st.secrets["GEMINI_API_KEY"]

# Main Public Header
st.title("🎛️ SemiPro: The Physical Design Academy")
st.markdown("### Master VLSI from Scratch • Interactive Sandboxes • **No Login • No Trackers • 100% Free**")
st.write("---")

# Layout Split: Left for study tree, Right for Sandbox
col_tree, col_sandbox = st.columns([1.2, 1.2])

# ==========================================
# LEFT SIDE: THE CLICKABLE KNOWLEDGE TREE
# ==========================================
with col_tree:
    st.header("🌿 1. Study & Concept Explorer")
    st.caption("Click a module to expand details, study formulas, and see cross-stage impacts.")

    with st.expander("🏗️ MODULE 1: Logic Synthesis & Timing Basics"):
        st.markdown("#### Subtopic 1.1: Setup Time Constraints")
        st.write("""
        * **The Core Concept:** Data launched by a launching flip-flop must arrive at the capturing flip-flop before the next clock edge arrives, minus the setup time of the destination cell.
        * **Cross-Stage Impact:** If the logic synthesis engine chooses dense, high-delay cells to minimize area, **Stage 4 (Placement)** will inherit a netlist that inherently cannot meet high-frequency timing constraints.
        """)
        st.latex(r"Slack_{setup} = T_{period} - T_{data\_delay} - T_{setup\_time}")

    with st.expander("🗺️ MODULE 2: Floorplanning & Macro Placement"):
        st.markdown("#### Subtopic 2.1: Core Utilization Metrics")
        st.write("""
        * **The Core Concept:** Core Utilization defines how packed your chip is with hardware components.
        * **Cross-Stage Impact:** Setting utilization to 85% leaves almost no room for inter-cell wiring. While the floorplan looks small and efficient, **Stage 6 (Routing)** will completely fail due to thousands of short-circuit DRC violations because there isn't enough physical space to run wires.
        """)
        st.latex(r"Utilization = \frac{Area_{Macros} + Area_{Standard\_Cells}}{Area_{Total\_Core}}")

# ==========================================
# RIGHT SIDE: THE INTERACTIVE INTERVIEW SANDBOX
# ==========================================
with col_sandbox:
    st.header("🎯 2. Real-Time Interview Sandbox")
    st.caption("Test your understanding with live problems. Type calculations or scripts directly below.")

    challenge_selection = st.selectbox(
        "Choose a Challenge to Solve:",
        ["Setup Slack Calculation (Entry Level)", "Fixing Congestion via Floorplanning (Professional Level)"]
    )
    
    st.write("---")

    if challenge_selection == "Setup Slack Calculation (Entry Level)":
        st.subheader("📝 Problem Statement:")
        st.warning("""
        Given a digital design operating at a clock frequency of **1 GHz** ($T_{period} = 1.0\text{ ns}$):
        * Total Data Path Delay ($T_{data\_delay}$) = **0.65 ns**
        * Destination Cell Setup Time ($T_{setup\_time}$) = **0.15 ns**
        
        Calculate the Setup Slack and write down the single line tool-independent TCL constraint command 
        used to define a standard clock profile named 'sys_clk' with a 1.0 ns period on the physical port 'clk_in'.
        """)
        
        user_math = st.text_input("Enter your calculated Slack value (e.g., 0.25):", key="math_1")
        user_code = st.text_area("Write your SDC/TCL constraint script here:", placeholder="create_clock -name ...", key="code_1")
        
        if st.button("Submit for Evaluation", key="sub_1"):
            if not user_math or not user_code:
                st.error("Please fill out both boxes before submitting.")
            else:
                with st.spinner("AI Coach is analyzing your solution..."):
                    try:
                        client = genai.Client()
                        evaluation_prompt = f"""
                        You are an elite VLSI Physical Design interviewer. 
                        Evaluate the student's response. 
                        Correct Math: 0.20 ns. Correct TCL: create_clock -name sys_clk -period 1.0 [get_ports clk_in]
                        Student Math: {user_math}
                        Student TCL: {user_code}
                        """
                        response = client.models.generate_content(model='gemini-2.5-flash', contents=evaluation_prompt)
                        st.success("📝 AI Coach Review:")
                        st.write(response.text)
                    except Exception:
                        st.info("💡 *SemiPro interface verified! Once a free key is saved in the cloud settings, the automated AI tutor will evaluate your response here.*")
