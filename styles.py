import streamlit as st

def apply_semiconductor_theme():
    """
    Applies matte obsidian glassmorphic styling, transparent layouts,
    and sets up the pure animated formatting rules for the right-side badge.
    """
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;800&family=JetBrains+Mono:wght@300;500&display=swap');

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

        /* PREMIUM ABSOLUTE FLOATING BADGE (Forces it to the top-right corner) */
        .premium-right-badge {
            position: fixed !important;
            top: 30px !important;
            right: 40px !important;
            z-index: 999999 !important;
        }

        /* HARDWARE CIRCUIT SYSTEM COLOR SWEEP EFFECT */
        .kinetic-gif-btn {
            background: linear-gradient(270deg, #1e40af, #3b82f6, #06b6d4, #1e40af) !important;
            background-size: 400% 400% !important;
            animation: circuitGifSweep 3s linear infinite, hardwareShockwave 2s infinite cubic-bezier(0.66, 0, 0, 1) !important;
            color: #ffffff !important;
            border: 2px solid rgba(255, 255, 255, 0.4) !important;
            padding: 10px 28px !important;
            border-radius: 50px !important;
            font-size: 0.9rem !important;
            font-weight: 700 !important;
            letter-spacing: 0.8px !important;
            text-transform: uppercase !important;
            cursor: pointer !important;
            box-shadow: 0 4px 15px rgba(0,0,0,0.3) !important;
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
            display: inline-block !important;
        }

        /* Springy Pop-out Animation on Hover */
        .kinetic-gif-btn:hover {
            transform: scale(1.1) translateY(-2px) !important;
            border-color: #ffffff !important;
            box-shadow: 
                0 15px 30px rgba(59, 130, 246, 0.4),
                0 0 25px rgba(6, 182, 212, 0.6) !important;
        }

        /* Infinite color-sweep loop mechanics */
        @keyframes circuitGifSweep {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        /* Infinite radial pulse wave loops */
        @keyframes hardwareShockwave {
            0% { box-shadow: 0 0 0 0 rgba(6, 182, 212, 0.6); }
            70% { box-shadow: 0 0 0 16px rgba(6, 182, 212, 0); }
            100% { box-shadow: 0 0 0 0 rgba(6, 182, 212, 0); }
        }

        /* Clean Glassmorphic Blueprint Panel Container */
        .glass-panel {
            background: rgba(15, 23, 42, 0.76) !important;
            border: 1px solid rgba(255, 255, 255, 0.08) !important;
            border-radius: 24px;
            padding: 40px;
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            box-shadow: 0 25px 55px rgba(0, 0, 0, 0.5);
            margin-top: 50px;
            margin-bottom: 30px;
            z-index: 1;
        }

        /* Pop-Out Overlay Map Grid Box */
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

        /* Content Track Matrix Layout Cards */
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
        </style>
    """, unsafe_allow_html=True)
