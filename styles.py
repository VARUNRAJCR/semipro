import streamlit as st

def apply_semiconductor_theme():
    """
    Injects matte obsidian glassmorphic formatting rules, enforces background
    transparency, and styles the right-aligned high-speed wave trigger badge.
    """
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@300;500&display=swap');

        /* Force deep layout transparency so the background sand canvas is fully visible */
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

        /* STYLING THE NATIVE RIGHT-ALIGNED HIGH-SPEED TOGGLE BADGE */
        div[data-testid="stColumn"] button[key="native_wave_trigger"] {
            background: linear-gradient(135deg, #0f172a, #1e293b) !important;
            color: #06b6d4 !important;
            border: 2px solid #06b6d4 !important;
            padding: 10px 24px !important;
            border-radius: 50px !important;
            font-size: 0.9rem !important;
            font-weight: 700 !important;
            letter-spacing: 1px !important;
            text-transform: uppercase !important;
            box-shadow: 0 0 15px rgba(6, 182, 212, 0.2) !important;
            transition: all 0.25s cubic-bezier(0.25, 1, 0.5, 1) !important; /* Accelerated high-speed vector wave */
            float: right !important; /* Pushes it beautifully to your right side */
        }

        /* Kinetic Hover Effect */
        div[data-testid="stColumn"] button[key="native_wave_trigger"]:hover {
            transform: scale(1.04) translateY(-1px) !important;
            color: #ffffff !important;
            background: #06b6d4 !important;
            box-shadow: 0 0 25px rgba(6, 182, 212, 0.5) !important;
            border-color: #ffffff !important;
        }

        /* Premium Matte Obsidian Glass Panel Containers - Safe and Clean */
        .glass-panel {
            background: rgba(15, 23, 42, 0.76) !important;
            border: 1px solid rgba(255, 255, 255, 0.08) !important;
            border-radius: 24px;
            padding: 40px;
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            box-shadow: 0 25px 55px rgba(0, 0, 0, 0.5);
            margin-top: 15px;
            margin-bottom: 30px;
            z-index: 1;
        }

        /* HIGH-SPEED OCEAN WAVE DROPDOWN OVERLAY (Graceful, responsive wave expander) */
        .curriculum-overlay-map {
            background: rgba(10, 15, 30, 0.97) !important;
            border: 1px solid rgba(6, 182, 212, 0.25) !important;
            border-radius: 24px;
            padding: 35px;
            margin-bottom: 30px;
            box-shadow: 0 15px 50px rgba(0, 0, 0, 0.6), 0 0 40px rgba(6, 182, 212, 0.12);
            transform-origin: top center;
            animation: highSpeedWaveRoll 0.28s cubic-bezier(0.25, 1, 0.5, 1) forwards; /* Snappy wave boot curve */
            will-change: transform, opacity;
        }

        @keyframes highSpeedWaveRoll {
            0% { 
                transform: translateY(-15px) scaleY(0.7) scaleX(0.98); 
                opacity: 0; 
                filter: blur(4px);
            }
            100% { 
                transform: translateY(0) scaleY(1) scaleX(1); 
                opacity: 1; 
                filter: blur(0px);
            }
        }

        /* Hardware Module Curriculum Display Cards */
        .silicon-vector-card {
            background: linear-gradient(145deg, rgba(30, 41, 59, 0.45), rgba(15, 23, 42, 0.35)) !important;
            border: 1px solid rgba(255, 255, 255, 0.05) !important;
            border-radius: 20px;
            padding: 28px;
            transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
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

        .stButton>button:not([key="native_wave_trigger"]) {
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
