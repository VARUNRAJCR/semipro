import streamlit as st

def apply_semiconductor_theme():
    """
    Injects high-end matte obsidian glassmorphic styles and structural 
    layout overrides to force native layout canvas compliance.
    """
    st.markdown("""
        <style>
        /* Base typography setup */
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;800&family=JetBrains+Mono:wght@300;500&display=swap');

        /* Force transparency across default content sheets so canvas shows behind them */
        html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], [data-testid="stSidebar"] {
            background: transparent !important;
            color: #f3f4f6 !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
        }

        /* Fixed Math Engine Layer Blueprint */
        .math-universe-bg {
            position: fixed;
            top: 0; left: 0;
            width: 100vw; height: 100vh;
            background-color: #02040a;
            z-index: -3;
        }
        
        #MainMenu, footer, header {visibility: hidden;}

        /* Matte Obsidian Glass Panel Containers */
        .glass-panel {
            background: rgba(10, 15, 30, 0.82);
            border: 1px solid rgba(255, 255, 255, 0.07);
            border-radius: 24px;
            padding: 40px;
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            box-shadow: 0 25px 55px rgba(0, 0, 0, 0.6);
            margin-bottom: 30px;
            z-index: 1;
        }

        /* Industrial Interactive Phase Layout Cards */
        .silicon-vector-card {
            background: linear-gradient(145deg, rgba(17, 24, 39, 0.65), rgba(31, 41, 55, 0.35));
            border: 1px solid rgba(255, 255, 255, 0.04);
            border-radius: 20px;
            padding: 28px;
            transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
            height: 210px;
            margin-bottom: 20px;
        }

        .silicon-vector-card:hover {
            border-color: rgba(59, 130, 246, 0.45);
            background: linear-gradient(145deg, rgba(17, 24, 39, 0.75), rgba(31, 41, 55, 0.45));
            box-shadow: 0 15px 35px rgba(59, 130, 246, 0.2);
            transform: translateY(-5px);
        }

        .silicon-vector-card h3 {
            font-weight: 600;
            font-size: 1.35rem;
            color: #ffffff;
            margin-top: 0;
            margin-bottom: 12px;
            letter-spacing: -0.5px;
        }

        .silicon-vector-card p {
            color: #9ca3af;
            font-size: 0.95rem;
            line-height: 1.6;
        }

        /* Monospace AI Terminal Box */
        .terminal-box {
            background: rgba(1, 3, 9, 0.92);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 20px;
            padding: 24px;
            font-family: 'JetBrains Mono', monospace;
            margin-bottom: 15px;
            box-shadow: inset 0 4px 20px rgba(0,0,0,0.9);
        }

        /* Solid Interface Action Buttons */
        .stButton>button {
            background: #ffffff !important;
            color: #02040a !important;
            border: none !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-weight: 600 !important;
            border-radius: 14px !important;
            padding: 14px 28px !important;
            transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1) !important;
        }

        .stButton>button:hover {
            transform: scale(1.015) !important;
            box-shadow: 0 12px 30px rgba(255, 255, 255, 0.3) !important;
        }

        /* Persistent Sidebar Masking Configuration */
        [data-testid="stSidebar"] {
            background-color: rgba(4, 7, 15, 0.9) !important;
            border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
            backdrop-filter: blur(15px);
        }
        
        textarea {
            background-color: rgba(17, 24, 39, 0.5) !important;
            border: 1px solid rgba(255, 255, 255, 0.08) !important;
            color: #f3f4f6 !important;
            border-radius: 12px !important;
        }
        </style>
    """, unsafe_allow_html=True)
