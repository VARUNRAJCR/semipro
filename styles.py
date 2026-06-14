import streamlit as st

def apply_semiconductor_theme():
    """
    Injects high-end matte obsidian glassmorphic styles, a mathematical canvas setup,
    and an attractive pulsing floating trigger wave to toggle the custom navigation drawer.
    """
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;800&family=JetBrains+Mono:wght@300;500&display=swap');

        /* Force layout transparency for math canvas visibility */
        html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
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

        /* ATTRACTIVE GLOWING WAVE FLOATING TRIGGER BUTTON */
        .floating-trigger {
            position: fixed;
            top: 25px;
            left: 25px;
            background: linear-gradient(135deg, #1e40af, #3b82f6);
            color: #ffffff !important;
            padding: 12px 24px;
            border-radius: 50px;
            font-weight: 600;
            font-size: 0.95rem;
            cursor: pointer;
            z-index: 999999;
            box-shadow: 0 0 0 0 rgba(59, 130, 246, 0.7);
            animation: pulseWaveEffect 2s infinite cubic-bezier(0.66, 0, 0, 1);
            border: 1px solid rgba(255, 255, 255, 0.2);
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .floating-trigger:hover {
            transform: scale(1.05);
            background: linear-gradient(135deg, #2563eb, #60a5fa);
        }

        /* GIF/Kinetic Motion Pulse Wave Effect */
        @keyframes pulseWaveEffect {
            0% {
                box-shadow: 0 0 0 0 rgba(59, 130, 246, 0.7);
            }
            70% {
                box-shadow: 0 0 0 18px rgba(59, 130, 246, 0);
            }
            100% {
                box-shadow: 0 0 0 0 rgba(59, 130, 246, 0);
            }
        }

        /* Premium Glass Panel Container */
        .glass-panel {
            background: rgba(15, 23, 42, 0.8) !important;
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

        /* High-End Vector Track Layout Cards */
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

        /* OVERRIDE STREAMLIT SIDEBAR TO BE A SLIDE-OUT LEFT DRAWER */
        [data-testid="stSidebar"] {
            background-color: rgba(10, 15, 30, 0.95) !important;
            border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
            backdrop-filter: blur(25px);
            z-index: 99999 !important;
        }
        
        textarea {
            background-color: rgba(30, 41, 59, 0.4) !important;
            border: 1px solid rgba(255, 255, 255, 0.08) !important;
            color: #f3f4f6 !important;
            border-radius: 12px !important;
        }
        </style>
    """, unsafe_allow_html=True)
