import streamlit as st

def inject_premium_ui():
    """Injects premium styling, typography, and a mathematical falling particle sand canvas."""
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;800&family=JetBrains+Mono:wght@300;500&display=swap');

        html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
            background-color: #02040a !important;
            color: #f3f4f6 !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
        }
        
        #MainMenu, footer, header {visibility: hidden;}

        .glass-panel {
            background: rgba(10, 15, 30, 0.75);
            border: 1px solid rgba(255, 255, 255, 0.06);
            border-radius: 24px;
            padding: 40px;
            backdrop-filter: blur(25px);
            -webkit-backdrop-filter: blur(25px);
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
            margin-bottom: 30px;
        }

        .vector-card {
            background: rgba(22, 28, 45, 0.4);
            border: 1px solid rgba(255, 255, 255, 0.04);
            border-radius: 16px;
            padding: 32px;
            transition: all 0.5s cubic-bezier(0.25, 1, 0.5, 1);
            height: 240px;
            margin-bottom: 20px;
        }

        .vector-card:hover {
            border-color: rgba(59, 130, 246, 0.4);
            background: rgba(22, 28, 45, 0.65);
            box-shadow: 0 15px 35px rgba(59, 130, 246, 0.15);
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
            background: #010307;
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 16px;
            padding: 24px;
            font-family: 'JetBrains Mono', monospace;
        }

        .stButton>button {
            background: #ffffff !important;
            color: #02040a !important;
            border: none !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-weight: 600 !important;
            border-radius: 12px !important;
            padding: 12px 24px !important;
            transition: all 0.3s ease !important;
        }

        .stButton>button:hover {
            transform: scale(1.02) !important;
            box-shadow: 0 0 25px rgba(255, 255, 255, 0.3) !important;
        }

        [data-testid="stSidebar"] {
            background-color: #050814 !important;
            border-right: 1px solid rgba(255, 255, 255, 0.04) !important;
        }
        </style>

        <canvas id="sandUniverseCanvas" style="position:fixed; top:0; left:0; width:100vw; height:100vh; z-index:-1; pointer-events:none;"></canvas>

        <script>
        (function() {
            const canvas = document.getElementById('sandUniverseCanvas');
            const ctx = canvas.getContext('2d');
            
            function resize() {
                canvas.width = window.innerWidth;
                canvas.height = window.innerHeight;
            }
            window.addEventListener('resize', resize);
            resize();

            // Mutate physics boundaries uniquely on every execution cycle
            const particleCount = 120 + Math.floor(Math.random() * 80);
            const gravitationalPull = 0.02 + Math.random() * 0.03;
            const horizontalDrift = 0.1 - Math.random() * 0.2;
            
            const particles = [];

            // Instantiate structural quantum grain properties
            for (let i = 0; i < particleCount; i++) {
                particles.push({
                    x: Math.random() * canvas.width,
                    y: Math.random() * canvas.height - canvas.height,
                    radius: 1 + Math.random() * 2,
                    densitySpeed: 0.5 + Math.random() * 1.5,
                    opacity: 0.1 + Math.random() * 0.4,
                    colorShift: Math.random() > 0.5 ? 'rgba(59, 130, 246,' : 'rgba(14, 165, 233,'
                });
            }

            function animateSandUniverse() {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                
                for (let i = 0; i < particleCount; i++) {
                    let p = particles[i];
                    
                    // Render individual grain node elements
                    ctx.beginPath();
                    ctx.fillStyle = p.colorShift + p.opacity + ')';
                    ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2, true);
                    ctx.fill();
                    
                    // Process vector physics alterations
                    p.y += p.densitySpeed;
                    p.x += horizontalDrift;
                    p.densitySpeed += gravitationalPull;

                    // Reset trajectory boundaries smoothly once silicon grain exits viewport
                    if (p.y > canvas.height) {
                        p.x = Math.random() * canvas.width;
                        p.y = -20;
                        p.densitySpeed = 0.5 + Math.random() * 1.5;
                    }
                    
                    // Wrap horizontal paths around edge boundaries safely
                    if (p.x > canvas.width) p.x = 0;
                    else if (p.x < 0) p.x = canvas.width;
                }
                
                requestAnimationFrame(animateSandUniverse);
            }
            animateSandUniverse();
        })();
        </script>
        """, unsafe_allow_html=True)
