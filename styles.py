import streamlit as st

def apply_semiconductor_theme():
    """
    Injects matte obsidian glassmorphic styles and customizes the right-aligned
    pulsing trigger to look like an active, animated GIF badge labeled 'Content'.
    """
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;800&family=JetBrains+Mono:wght@300;500&display=swap');

        /* Force transparency across default content sheets so canvas shows behind them */
        html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], [data-testid="stSidebar"] {
            background: transparent !important;
            color: #f3f4f6 !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
        }

        /* Fixed Background Math Position Layer */
        .math-universe-bg {
            position: fixed;
            top: 0; left: 0;
            width: 100vw; height: 100vh;
            background-color: #030712;
            z-index: -3;
        }
        
        #MainMenu, footer, header {visibility: hidden;}

        /* FORCE THE BUTTON CONTAINER TO THE UPPER RIGHT OF THE WINDOW VIEW */
        div.element-container:has(button[key="right_topics_trigger"]) {
            position: fixed !important;
            top: 25px !important;
            right: 40px !important;
            left: auto !important;
            z-index: 999999 !important;
            width: auto !important;
        }

        /* DIGITAL KINETIC GIF EMULATION STYLING RULES */
        button[key="right_topics_trigger"] {
            background: linear-gradient(270deg, #1e40af, #3b82f6, #0284c7, #1e40af) !important;
            background-size: 600% 600% !important;
            animation: kineticGifSweep 4s linear infinite, pristineRightPulse 2s infinite cubic-bezier(0.66, 0, 0, 1) !important;
            color: #ffffff !important;
            padding: 12px 30px !important;
            border-radius: 50px !important;
            font-weight: 600 !important;
            font-size: 0.95rem !important;
            border: 1px solid rgba(255, 255, 255, 0.35) !important;
            box-shadow: 0 0 0 0 rgba(59, 130, 246, 0.7) !important;
            transition: all 0.3s ease !important;
            text-transform: uppercase !important;
            letter-spacing: 0.5px !important;
        }
        
        button[key="right_topics_trigger"]:hover {
            transform: scale(1.04) !important;
            box-shadow: 0 0 25px rgba(59, 130, 246, 0.4) !important;
        }

        /* GIF Animation Pattern A: Continuous Linear Color Sweep */
        @keyframes kineticGifSweep {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        /* GIF Animation Pattern B: Shockwave Pulse Matrix */
        @keyframes pristineRightPulse {
            0% { box-shadow: 0 0 0 0 rgba(59, 130, 246, 0.7); }
            70% { box-shadow: 0 0 0 20px rgba(59, 130, 246, 0); }
            100% { box-shadow: 0 0 0 0 rgba(59, 130, 246, 0); }
        }

        /* Premium Matte Obsidian Glass Panels */
        .glass-panel {
            background: rgba(15, 23, 42, 0.78) !important;
            border: 1px solid rgba(255, 255, 255, 0.08) !important;
            border-radius: 24px;
            padding: 40px;
            backdrop-filter: blur(24px);
            -webkit-backdrop-filter: blur(24px);
            box-shadow: 0 25px 55px rgba(0, 0, 0, 0.5);
            margin-top: 60px;
            margin-bottom: 30px;
            z-index: 1;
        }

        /* Full Curriculum Overlay Panel Map */
        .curriculum-overlay-map {
            background: rgba(10, 15, 30, 0.96) !important;
            border: 1px solid rgba(59, 130, 246, 0.25) !important;
            border-radius: 20px;
            padding: 35px;
            margin-bottom: 30px;
            box-shadow: 0 0 40px rgba(59, 130, 246, 0.15);
        }

        /* Silicon Layout Cards */
        .silicon-vector-card {
            background: linear-gradient(145deg, rgba(30, 41, 59, 0.45), rgba(15, 23, 42, 0.35)) !important;
            border: 1px solid rgba(255, 255, 255, 0.05) !important;
            border-radius: 20px;
            padding: 28px;
            transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
            height: 210px;
            margin-bottom: 20px;
        }

        .silicon-vector-card:hover {
            border-color: rgba(59, 130, 246, 0.5) !important;
            background: linear-gradient(145deg, rgba(30, 41, 59, 0.6), rgba(15, 23, 42, 0.5)) !important;
            box-shadow: 0 15px 35px rgba(59, 130, 246, 0.2);
            transform: translateY(-5px);
        }

        .silicon-vector-card h3 {
            font-weight: 600;
            font-size: 1.35rem;
            color: #ffffff;
            margin-top: 0;
            margin-bottom: 12px;
        }

        .silicon-vector-card p {
            color: #9ca3af;
            font-size: 0.95rem;
            line-height: 1.6;
        }

        .terminal-box {
            background: rgba(15, 23, 42, 0.65) !important;
            border: 1px solid rgba(255, 255, 255, 0.06) !important;
            border-radius: 20px;
            padding: 24px;
            font-family: 'JetBrains Mono', monospace;
            margin-bottom: 15px;
        }

        .stButton>button:not([key="right_topics_trigger"]) {
            background: #ffffff !important;
            color: #030712 !important;
            border: none !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-weight: 600 !important;
            border-radius: 14px !important;
            padding: 14px 28px !important;
            transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1) !important;
        }

        [data-testid="stSidebar"] { visibility: hidden !important; width: 0px !important; }
        
        textarea {
            background-color: rgba(30, 41, 59, 0.4) !important;
            border: 1px solid rgba(255, 255, 255, 0.08) !important;
            color: #f3f4f6 !important;
            border-radius: 12px !important;
        }
        </style>
    """, unsafe_allow_html=True)
