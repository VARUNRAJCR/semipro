import streamlit as st

def apply_semiconductor_theme():
    """
    Injects high-end matte obsidian glassmorphic layouts, a transparent canvas, 
    and hooks up a zero-reload CSS checkbox engine to execute a fluid, organic 
    ocean-wave cascading dropdown animation natively in the browser view.
    """
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@300;500&display=swap');

        /* Force background transparency across core block wrappers */
        html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], [data-testid="stSidebar"] {
            background: transparent !important;
            color: #f3f4f6 !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
        }

        /* Fixed Background Math Canvas Position Layer */
        .math-universe-bg {
            position: fixed;
            top: 0; left: 0;
            width: 100vw; height: 100vh;
            background-color: #030712;
            z-index: -3;
        }
        
        #MainMenu, footer, header {visibility: hidden;}

        /* ABSOLUTE FLOATING PACKAGING CONTAINER FOR THE NAV BADGE */
        .hardware-nav-wrapper {
            position: fixed !important;
            top: 25px !important;
            right: 40px !important;
            z-index: 999999 !important;
            display: block !important;
        }

        /* HIDDEN CHECKBOX ENGINE TO INTERCEPT CLICKS WITHOUT RELOADING */
        #waveNavToggle {
            display: none !important;
        }

        /* THE ANIMATED HIGH-END CONTENT INTERACTION BADGE */
        .hardware-wake-btn {
            background: linear-gradient(135deg, #0f172a, #1e293b) !important;
            color: #06b6d4 !important;
            border: 2px solid #06b6d4 !important;
            padding: 12px 32px;
            border-radius: 50px;
            font-size: 0.9rem;
            font-weight: 700;
            letter-spacing: 1px;
            text-transform: uppercase;
            cursor: pointer;
            box-shadow: 0 0 15px rgba(6, 182, 212, 0.2);
            transition: all 0.3s cubic-bezier(0.25, 1, 0.5, 1);
            display: inline-block;
            user-select: none;
            text-align: center;
        }

        /* Continuous GIF-Quality Pulsing Glow Effect */
        .hardware-wake-btn::after {
            content: '';
            position: absolute;
            top: -50%; left: -50%; width: 200%; height: 200%;
            background: radial-gradient(circle, rgba(6, 182, 212, 0.15) 0%, transparent 70%);
            animation: ambientWakePulse 2.5s infinite linear;
            pointer-events: none;
        }

        @keyframes ambientWakePulse {
            0% { transform: scale(0.5); opacity: 0; }
            50% { opacity: 1; }
            100% { transform: scale(1.2); opacity: 0; }
        }

        .hardware-wake-btn:hover {
            transform: scale(1.05);
            color: #ffffff;
            background: #06b6d4;
            box-shadow: 0 0 30px rgba(6, 182, 212, 0.6);
        }

        /* CHANGING TEXT STATE DYNAMICALLY INSIDE BROWSER */
        #waveNavToggle:checked + .hardware-wake-btn {
            background: #e11d48 !important;
            border-color: #e11d48 !important;
            color: #ffffff !important;
            box-shadow: 0 0 25px rgba(225, 29, 72, 0.5) !important;
        }
        
        #waveNavToggle:checked + .hardware-wake-btn .btn-text::before {
            content: "Close Content ✕" !important;
        }

        /* PURE NATIVE BROWSER DROPDOWN PANEL (Stays safely hidden under the floor) */
        .curriculum-wave-panel {
            position: fixed !important;
            top: 90px !important;
            right: 40px !important;
            left: 40px !important;
            background: rgba(10, 15, 30, 0.97) !important;
            border: 1px solid rgba(6, 182, 212, 0) !important;
            border-radius: 24px;
            padding: 0px 35px;
            box-shadow: 0 0px 0px rgba(0,0,0,0);
            z-index: 999998 !important;
            
            /* Fluid Ocean Wave Rolling Properties */
            max-height: 0px;
            opacity: 0;
            overflow: hidden;
            filter: blur(10px) brightness(1.5);
            transform: scaleY(0) translateY(-30px);
            transform-origin: top center;
            transition: max-height 0.5s ease-in-out, 
                        padding 0.5s ease-in-out,
                        opacity 0.4s ease-out, 
                        filter 0.4s ease-out, 
                        transform 0.5s cubic-bezier(0.19, 1, 0.22, 1),
                        border 0.3s ease !important;
        }

        /* THE OCEAN WAVE ROLL TRIGGER ACTION (Cascades open with a rising fluid roll) */
        #waveNavToggle:checked ~ .curriculum-wave-panel {
            max-height: 800px;
            padding: 35px;
            opacity: 1;
            filter: blur(0px) brightness(1);
            transform: scaleY(1) translateY(0);
            border: 1px solid rgba(6, 182, 212, 0.25) !important;
            box-shadow: 0 25px 60px rgba(0, 0, 0, 0.75), 0 0 40px rgba(6, 182, 212, 0.12) !important;
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
            margin-top: 50px;
            margin-bottom: 30px;
            z-index: 1;
        }

        /* Curricular Section Cards */
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
