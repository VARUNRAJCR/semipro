import streamlit as st

def apply_semiconductor_theme():
    """
    Applies clean matte obsidian glassmorphic styles and sets up structural 
    presentation layers for the right-side layout alignment elements.
    """
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;800&family=JetBrains+Mono:wght@300;500&display=swap');

        /* Force transparency across layers so the sand math canvas plays perfectly */
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

        /* NATIVE BUTTON OVERRIDE FOR THE INTEGRATED CONTENT ACTION BADGE */
        div[data-testid="stColumn"] button[key="native_right_trigger"] {
            background: linear-gradient(270deg, #1e40af, #3b82f6, #06b6d4, #1e40af) !important;
            background-size: 400% 400% !important;
            animation: circuitGifSweep 3s linear infinite, hardwareShockwave 2s infinite cubic-bezier(0.66, 0, 0, 1) !important;
            color: #ffffff !important;
            border: 2px solid rgba(255, 255, 255, 0.4) !important;
            padding: 10px 24px !important;
            border-radius: 50px !important;
            font-size: 0.9rem !important;
            font-weight: 700 !important;
            letter-spacing: 0.8px !important;
            text-transform: uppercase !important;
            box-shadow: 0 4px 15px rgba(0,0,0,0.3) !important;
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
            float: right !important; /* Forces it smoothly to the absolute right side */
        }

        div[data-testid="stColumn"] button[key="native_right_trigger"]:hover {
            transform: scale(1.06) translateY(-2px) !important;
            border-color: #ffffff !important;
            box-shadow: 0 12px 25px rgba(59, 130, 246, 0.4) !important;
        }

        /* Infinite linear color sweep animations */
        @keyframes circuitGifSweep {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        @keyframes hardwareShockwave {
            0% { box-shadow: 0 0 0 0 rgba(6, 182, 212, 0.6); }
            70% { box-shadow: 0 0 0 14px rgba(6, 182, 212, 0); }
            100% { box-shadow: 0 0 0 0 rgba(6, 182, 212, 0); }
        }

        /* Matte Obsidian Glass Panel Containers */
        .glass-panel {
            background: rgba(15, 23, 42, 0.76) !important;
            border: 1px solid rgba(255, 255, 255, 0.08) !important;
            border-radius: 24px;
            padding: 40px;
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            box-shadow: 0 25px 55px rgba(0, 0, 0, 0.5);
            margin-bottom: 30px;
            z-index: 1;
        }

        /* Overlay Map Grid Panel */
        .curriculum-overlay-map {
            background: rgba(10, 15, 30, 0.96) !important;
            border: 1px solid rgba(6, 182, 212, 0.3) !important;
            border-radius: 20px;
            padding: 35px;
            margin-bottom: 30px;
            box-shadow: 0 0 50px rgba(6, 182, 212, 0.15);
            animation: panelPopFade 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }

        @keyframes panelPopFade {
            0% { transform: scale(0.97); opacity: 0; }
            100% { transform: scale(1); opacity: 1; }
        }

        /* Curriculum Section Cards */
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

        .silicon-vector-card h3 { font-weight: 600; font-size: 1.35rem; color: #ffffff; margin-top: 0; margin-bottom: 12px; }
        .silicon-vector-card p { color: #9ca3af; font-size: 0.95rem; line-height: 1.6; }
        .terminal-box { background: rgba(15, 23, 42, 0.65) !important; border: 1px solid rgba(255, 255, 255, 0.06) !important; border-radius: 20px; padding: 24px; font-family: 'JetBrains Mono', monospace; margin-bottom: 15px; }

        .stButton>button:not([key="native_right_trigger"]) {
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
