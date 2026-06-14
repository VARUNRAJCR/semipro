import streamlit as st

def apply_semiconductor_theme():
    """
    Injects matte obsidian glassmorphic styles and forces a right-anchored 
    kinetic GIF-sweep element with a 3D scaling pop-out interaction state.
    """
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;800&family=JetBrains+Mono:wght@300;500&display=swap');

        /* Force layout transparency so the mathematical canvas displays perfectly */
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

        /* FORCE THE CONTENT BUTTON TO POSITION EXACTLY ON THE RIGHT OF THE SCREEN VIEWPORT */
        div.element-container:has(button[key="right_topics_trigger"]) {
            position: fixed !important;
            top: 25px !important;
            right: 40px !important;  /* Pins it perfectly to the right border */
            left: auto !important;   /* Sweeps away any left-side alignments */
            z-index: 999999 !important;
            width: auto !important;
        }

        /* HIGH-SPEED KINETIC EMBEDDED GIF EFFECT */
        button[key="right_topics_trigger"] {
            background: linear-gradient(270deg, #1e40af, #3b82f6, #06b6d4, #1e40af) !important;
            background-size: 400% 400% !important;
            animation: circuitGifSweep 3s linear infinite, hardwareShockwave 2s infinite cubic-bezier(0.66, 0, 0, 1) !important;
            color: #ffffff !important;
            padding: 12px 32px !important;
            border-radius: 50px !important;
            font-weight: 700 !important;
            font-size: 0.95rem !important;
            border: 2px solid rgba(255, 255, 255, 0.4) !important;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important; /* Premium Elastic Pop Out Engine */
            text-transform: uppercase !important;
            letter-spacing: 0.7px !important;
            transform: scale(1);
        }
        
        /* 3D POP OUT ANIMATION EFFECT ON HOVER */
        button[key="right_topics_trigger"]:hover {
            transform: scale(1.1) translateY(-2px) !important; /* Pops outward and upwards towards the user */
            border-color: #ffffff !important;
            box-shadow: 
                0 15px 30px rgba(59, 130, 246, 0.4),
                0 0 25px rgba(6, 182, 212, 0.6) !important;
        }

        /* GIF Animation Logic Block A: Seamless Current Sweep */
        @keyframes circuitGifSweep {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        /* GIF Animation Logic Block B: Radial Core Waves */
        @keyframes hardwareShockwave {
            0% { box-shadow: 0 0 0 0 rgba(6, 182, 212, 0.7); }
            70% { box-shadow: 0 0 0 18px rgba(6, 182, 212, 0); }
            100% { box-shadow: 0 0 0 0 rgba(6, 182, 212, 0); }
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

        /* Dynamic Pop-Out Curricular Sheet Grid Map */
        .curriculum-overlay-map {
            background: rgba(10, 15, 30, 0.96) !important;
            border: 1px solid rgba(6, 182, 212, 0.3) !important;
            border-radius: 20px;
            padding: 35px;
            margin-bottom: 30px;
            box-shadow: 0 0 50px rgba(6, 182, 212, 0.15);
            animation: panelPopFade 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }

        @keyframes panelPopFade {
            0% { transform: scale(0.95); opacity: 0; }
            100% { transform: scale(1); opacity: 1; }
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
            border-color: rgba(6, 182, 212, 0.5) !important;
            background: linear-gradient(145deg, rgba(30, 41, 59, 0.6), rgba(15, 23, 42, 0.5)) !important;
            box-shadow: 0 15px 35px rgba(6, 182, 212, 0.2);
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

        textarea {
            background-color: rgba(30, 41, 59, 0.4) !important;
            border: 1px solid rgba(255, 255, 255, 0.08) !important;
            color: #f3f4f6 !important;
            border-radius: 12px !important;
        }
        </style>
    """, unsafe_allow_html=True)
