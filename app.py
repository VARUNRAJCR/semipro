import streamlit as st

def apply_semiconductor_theme():
    """
    Applies clean matte obsidian glassmorphic formatting rules, enforces background
    transparency, and handles the absolute float layer for the right-side GIF tab.
    """
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@300;500&display=swap');

        /* Force layout transparency so the background sand canvas is fully visible */
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

        /* PREMIUM FLOATING WRAPPER - ABSOLUTELY PINS TO THE UPPER RIGHT */
        .gif-pop-container {
            position: fixed !important;
            top: 30px !important;
            right: 40px !important;
            z-index: 999999 !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
        }

        /* HIDE THE TOGGLE ELEMENT */
        #gifPopToggle {
            display: none !important;
        }

        /* TRUE DIGITAL KINETIC GIF STYLE BUTTON LAYER */
        .gif-pop-badge {
            background: linear-gradient(270deg, #1e40af, #06b6d4, #3b82f6, #1e40af) !important;
            background-size: 400% 400% !important;
            animation: glowMoveLoop 3s linear infinite, shockwavePulse 2s infinite cubic-bezier(0.66, 0, 0, 1) !important;
            color: #ffffff !important;
            padding: 12px 30px;
            border-radius: 50px;
            font-size: 0.9rem;
            font-weight: 800;
            letter-spacing: 1px;
            text-transform: uppercase;
            cursor: pointer;
            border: 2px solid rgba(255, 255, 255, 0.4);
            transition: transform 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
            display: inline-block;
            user-select: none;
            box-shadow: 0 4px 20px rgba(6, 182, 212, 0.3);
        }

        /* Pop Out Motion on Hover */
        .gif-pop-badge:hover {
            transform: scale(1.08) translateY(-2px);
            border-color: #ffffff;
            box-shadow: 0 10px 25px rgba(6, 182, 212, 0.5);
        }

        /* GIF Color Sweep Loop Mechanics */
        @keyframes glowMoveLoop {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        @keyframes shockwavePulse {
            0% { box-shadow: 0 0 0 0 rgba(6, 182, 212, 0.6); }
            70% { box-shadow: 0 0 0 15px rgba(6, 182, 212, 0); }
            100% { box-shadow: 0 0 0 0 rgba(6, 182, 212, 0); }
        }

        /* Dynamic Title Update via CSS */
        .gif-pop-badge::before {
            content: "Content ☰";
        }
        #gifPopToggle:checked + .gif-pop-badge::before {
            content: "Close Content ✕";
        }
        #gifPopToggle:checked + .gif-pop-badge {
            background: #e11d48 !important;
            border-color: #ffffff !important;
            box-shadow: 0 0 25px rgba(225, 29, 72, 0.6) !important;
        }

        /* INSTANT HIGH-SPEED DROP DOWN PANEL */
        .instant-curriculum-panel {
            position: fixed !important;
            top: 95px !important;
            right: 40px !important;
            left: 40px !important;
            background: rgba(10, 15, 30, 0.98) !important;
            border: 1px solid rgba(6, 182, 212, 0.3) !important;
            border-radius: 24px;
            padding: 35px;
            box-shadow: 0 30px 70px rgba(0, 0, 0, 0.8), 0 0 40px rgba(6, 182, 212, 0.15) !important;
            z-index: 999998 !important;
            
            /* Ultra-fast 0.18s popup animation setup */
            transform-origin: top right;
            transform: scale(0);
            opacity: 0;
            visibility: hidden;
            transition: transform 0.18s cubic-bezier(0.34, 1.56, 0.64, 1), opacity 0.15s ease !important;
        }

        /* Open Trigger state configuration */
        #gifPopToggle:checked ~ .instant-curriculum-panel {
            transform: scale(1);
            opacity: 1;
            visibility: visible;
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
            margin-top: 20px;
            margin-bottom: 30px;
            z-index: 1;
        }

        /* Course Phase Cards */
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

        .stButton>button {
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
