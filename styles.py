import streamlit as st

def apply_semiconductor_theme():
    """
    Injects matte obsidian glassmorphic styles, establishes a transparent layout
    canvas, and handles the organic ocean-wave cascading menu animation curves.
    """
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@300;500&display=swap');

        /* Force deep background transparency across all default Streamlit block wrappers */
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

        /* FIXED RIGHT WINDOW PLACEMENT NODE FOR CUSTOM INTERACTIVE BADGE */
        .hardware-trigger-container {
            position: fixed !important;
            top: 30px !important;
            right: 40px !important;
            z-index: 999999 !important;
        }

        /* HIGH-END METALLIC GIF INTERACTION BUTTON */
        .hardware-wake-btn {
            background: linear-gradient(135deg, #0f172a, #1e293b) !important;
            color: #06b6d4 !important;
            border: 2px solid #06b6d4 !important;
            padding: 12px 28px !important;
            border-radius: 50px !important;
            font-size: 0.9rem !important;
            font-weight: 700 !important;
            letter-spacing: 1px !important;
            text-transform: uppercase !important;
            cursor: pointer !important;
            box-shadow: 0 0 15px rgba(6, 182, 212, 0.2) !important;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
            display: inline-block !important;
            position: relative;
            overflow: hidden;
        }

        /* Continuous Ambient Pulse Wave */
        .hardware-wake-btn::after {
            content: '';
            position: absolute;
            top: -50%; left: -50%; width: 200%; height: 200%;
            background: radial-gradient(circle, rgba(6, 182, 212, 0.15) 0%, transparent 70%);
            animation: ambientWakePulse 2.5s infinite linear;
        }

        @keyframes ambientWakePulse {
            0% { transform: scale(0.5); opacity: 0; }
            50% { opacity: 1; }
            100% { transform: scale(1.2); opacity: 0; }
        }

        .hardware-wake-btn:hover {
            transform: scale(1.08) !important;
            color: #ffffff !important;
            background: #06b6d4 !important;
            box-shadow: 
                0 0 30px rgba(6, 182, 212, 0.6),
                0 0 50px rgba(30, 64, 175, 0.4) !important;
            border-color: #ffffff !important;
        }

        /* Premium Matte Obsidian Glass Panels */
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

        /* OCEAN WAVE PANEL ANIMATION (Cascades down and expands gracefully like a tidal roll) */
        .curriculum-overlay-map {
            background: rgba(10, 15, 30, 0.97) !important;
            border: 1px solid rgba(6, 182, 212, 0.25) !important;
            border-radius: 24px;
            padding: 35px;
            margin-bottom: 30px;
            box-shadow: 0 15px 50px rgba(0, 0, 0, 0.6), 0 0 40px rgba(6, 182, 212, 0.1);
            
            /* Core ocean curve timing setups */
            transform-origin: top center;
            animation: oceanWaveRoll 0.55s cubic-bezier(0.25, 1, 0.5, 1) forwards;
            will-change: transform, opacity, filter;
        }

        @keyframes oceanWaveRoll {
            0% { 
                transform: translateY(-40px) scaleY(0.4) scaleX(0.96); 
                opacity: 0; 
                filter: blur(8px) brightness(1.5); 
            }
            60% {
                transform: translateY(4px) scaleY(1.02) scaleX(1.01);
                filter: blur(0px) brightness(1.1);
            }
            100% { 
                transform: translateY(0) scaleY(1) scaleX(1); 
                opacity: 1; 
                filter: brightness(1); 
            }
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
