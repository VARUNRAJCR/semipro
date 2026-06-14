import streamlit as st

def inject_premium_ui():
    """Injects premium styling, typography, and mathematical canvas background."""
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;800&family=JetBrains+Mono:wght@300;500&display=swap');

        html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
            background-color: #030712 !important;
            color: #f3f4f6 !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
        }
        
        #MainMenu, footer, header {visibility: hidden;}

        .glass-panel {
            background: rgba(17, 24, 39, 0.7);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 24px;
            padding: 40px;
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.4);
            margin-bottom: 30px;
        }

        .vector-card {
            background: rgba(31, 41, 55, 0.4);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 16px;
            padding: 32px;
            transition: all 0.5s cubic-bezier(0.25, 1, 0.5, 1);
            height: 240px;
            margin-bottom: 20px;
        }

        .vector-card:hover {
            border-color: rgba(59, 130, 246, 0.5);
            background: rgba(31, 41, 55, 0.6);
            box-shadow: 0 10px 30px rgba(59, 130, 246, 0.15);
            transform: translateY(-4px);
        }

        .vector-card h3 {
            font-weight: 600;
            font-size: 1.35rem;
            color: #ffffff;
            margin-bottom: 12px;
        }

        .vector-card p {
            color: #9ca3af;
            font-size: 0.95rem;
            line-height: 1.6;
        }

        .terminal-box {
            background: #020617;
            border: 1px solid rgba(255, 255, 255, 0.06);
            border-radius: 16px;
            padding: 24px;
            font-family: 'JetBrains Mono', monospace;
        }

        .stButton>button {
            background: #ffffff !important;
            color: #030712 !important;
            border: none !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-weight: 600 !important;
            border-radius: 12px !important;
            padding: 12px 24px !important;
            transition: all 0.3s ease !important;
        }

        .stButton>button:hover {
            transform: scale(1.02) !important;
            box-shadow: 0 0 20px rgba(255, 255, 255, 0.25) !important;
        }

        [data-testid="stSidebar"] {
            background-color: #090d16 !important;
            border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
        }
        </style>

        <canvas id="semiconductorCanvas" style="position:fixed; top:0; left:0; width:100vw; height:100vh; z-index:-1; pointer-events:none;"></canvas>

        <script>
        (function() {
            const canvas = document.getElementById('semiconductorCanvas');
            const ctx = canvas.getContext('2d');
            function resize() { canvas.width = window.innerWidth; canvas.height = window.innerHeight; }
            window.addEventListener('resize', resize); resize();

            const phaseShiftSpeed = 0.01 + Math.random() * 0.015;
            const carrierFrequency = 0.002 + Math.random() * 0.003;
            const amplitudeFactor = 40 + Math.random() * 30;
            const nodeDensity = 5;
            let timeStep = 0;

            function renderSemiconductorField() {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                timeStep += phaseShiftSpeed;
                ctx.lineWidth = 1;
                ctx.strokeStyle = 'rgba(59, 130, 246, 0.08)';
                ctx.beginPath();
                for (let x = 0; x < canvas.width; x += 5) {
                    let y = (canvas.height * 0.5) + Math.sin(x * carrierFrequency + timeStep) * amplitudeFactor;
                    if (x === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
                }
                ctx.stroke();
                requestAnimationFrame(renderSemiconductorField);
            }
            renderSemiconductorField();
        })();
        </script>
        """, unsafe_allow_html=True)
