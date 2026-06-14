import streamlit as st

def apply_semiconductor_theme():
    """
    Injects a real-time mathematical physics engine canvas calculating 
    universal falling sand/grain drift dynamically behind the interface.
    """
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;800&family=JetBrains+Mono:wght@300;500&display=swap');

        /* FORCE STREAMLIT TRANSPARENCY: Allows the canvas math layer to peek through everywhere */
        html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], [data-testid="stSidebar"] {
            background: transparent !important;
            color: #f3f4f6 !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
        }

        /* Fixed Background Wrapper Layer */
        .math-universe-bg {
            position: fixed;
            top: 0; left: 0;
            width: 100vw; height: 100vh;
            background-color: #02040a; /* True deep space silicon black baseline */
            z-index: -3;
        }
        
        #MainMenu, footer, header {visibility: hidden;}

        /* Matte Obsidian Glass Panel Container */
        .glass-panel {
            background: rgba(10, 15, 30, 0.78);
            border: 1px solid rgba(255, 255, 255, 0.07);
            border-radius: 24px;
            padding: 40px;
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            box-shadow: 0 25px 55px rgba(0, 0, 0, 0.6);
            margin-bottom: 30px;
            z-index: 1;
        }

        /* Architectural Phase Selection Cards */
        .silicon-vector-card {
            background: linear-gradient(145deg, rgba(17, 24, 39, 0.6), rgba(31, 41, 55, 0.3));
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

        /* Monospace Command Evaluation Terminal Console */
        .terminal-box {
            background: rgba(1, 3, 9, 0.9);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 20px;
            padding: 24px;
            font-family: 'JetBrains Mono', monospace;
            margin-bottom: 15px;
            box-shadow: inset 0 4px 20px rgba(0,0,0,0.9);
        }

        /* Solid Luxury Interface Buttons */
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

        /* Sidebar Glass Styling Override */
        [data-testid="stSidebar"] {
            background-color: rgba(4, 7, 15, 0.85) !important;
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

        <div class="math-universe-bg">
            <canvas id="sandMatrixCanvas" style="position:fixed; top:0; left:0; width:100vw; height:100vh; z-index:-2; pointer-events:none;"></canvas>
        </div>

        <script>
        (function() {
            const canvas = document.getElementById('sandMatrixCanvas');
            const ctx = canvas.getContext('2d');
            
            function resize() {
                canvas.width = window.innerWidth;
                canvas.height = window.innerHeight;
            }
            window.addEventListener('resize', resize);
            resize();

            // Mathematical Physics Constants: Density, acceleration drift vectors
            const grainCount = 130;
            const gravitationalPull = 0.015;
            const windDriftFactor = -0.04;
            const grains = [];

            // Instantiate randomized matrix node variables (Coordinates and densities)
            for (let i = 0; i < grainCount; i++) {
                grains.push({
                    x: Math.random() * canvas.width,
                    y: Math.random() * canvas.height,
                    size: 1 + Math.random() * 2,
                    terminalVelocity: 0.4 + Math.random() * 1.1,
                    massAlpha: 0.15 + Math.random() * 0.35,
                    colorBand: Math.random() > 0.4 ? 'rgba(59, 130, 246,' : 'rgba(14, 165, 233,'
                });
            }

            function processPhysicsEngine() {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                
                for (let i = 0; i < grainCount; i++) {
                    let g = grains[i];
                    
                    // Render particle node coordinate vectors
                    ctx.beginPath();
                    ctx.fillStyle = g.colorBand + g.massAlpha + ')';
                    ctx.arc(g.x, g.y, g.size, 0, Math.PI * 2, true);
                    ctx.fill();
                    
                    // Apply kinematic delta additions over time loop step
                    g.y += g.terminalVelocity;
                    g.x += windDriftFactor;
                    g.terminalVelocity += gravitationalPull;

                    // Bound limit resetting loops: regenerates particle back at y=0 when boundary breaks
                    if (g.y > canvas.height) {
                        g.x = Math.random() * canvas.width;
                        g.y = -10;
                        g.terminalVelocity = 0.4 + Math.random() * 1.1;
                    }
                }
                requestAnimationFrame(processPhysicsEngine);
            }
            processPhysicsEngine();
        })();
        </script>
    """, unsafe_allow_html=True)
