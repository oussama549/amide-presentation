import streamlit as st
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import time

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="Vitamin B₂ | Analytical Chemistry SGD 2026",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# CUSTOM CSS FOR DARK THEME
# ============================================================
st.markdown("""
<style>
    .stApp { background: #060a14; }
    h1, h2, h3 {
        background: linear-gradient(135deg, #00ff88, #00ccff, #7b2ffc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800 !important;
    }
    .subtitle {
        color: #8899bb;
        font-size: 1.2rem;
        font-weight: 300;
        letter-spacing: 2px;
        margin-bottom: 1rem;
    }
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(20px);
        border-radius: 24px;
        padding: 1.8rem 2rem;
        border: 1px solid rgba(255, 255, 255, 0.06);
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        margin-bottom: 1rem;
        color: #c8d6e5;
    }
    .glass-card h3 {
        color: #00ff88 !important;
        -webkit-text-fill-color: #00ff88 !important;
        font-size: 1.2rem;
        margin-bottom: 0.5rem;
    }
    .highlight {
        background: rgba(0, 255, 136, 0.05);
        border-left: 3px solid #00ff88;
        padding: 0.8rem 1.2rem;
        border-radius: 8px;
        color: #c8d6e5;
        margin: 1rem 0;
    }
    .highlight strong { color: #00ff88; }
    .workflow {
        display: flex;
        align-items: center;
        justify-content: center;
        flex-wrap: wrap;
        gap: 0.5rem 1rem;
        padding: 1rem 0;
    }
    .workflow-step {
        background: rgba(0, 255, 136, 0.05);
        border: 1px solid rgba(0, 255, 136, 0.15);
        border-radius: 40px;
        padding: 0.6rem 1.8rem;
        font-weight: 500;
        color: #bbddff;
        display: inline-flex;
        align-items: center;
        gap: 0.6rem;
        font-size: 0.95rem;
    }
    .workflow-arrow {
        color: #00ff88;
        font-size: 1.4rem;
        opacity: 0.4;
    }
    .metric-box {
        background: rgba(0, 0, 0, 0.3);
        border-radius: 16px;
        padding: 1rem 1.5rem;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }
    .metric-box .value {
        font-size: 2rem;
        font-weight: 700;
        color: #00ff88;
    }
    .metric-box .label {
        font-size: 0.8rem;
        color: #667799;
    }
    .footer {
        text-align: center;
        padding: 2rem 0 1rem;
        color: #445566;
        border-top: 1px solid rgba(255, 255, 255, 0.03);
        margin-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR NAVIGATION
# ============================================================
st.sidebar.markdown("""
<div style="text-align:center; padding:1rem 0;">
    <h3 style="color:#00ff88; -webkit-text-fill-color:#00ff88;">🧪 Vitamin B₂</h3>
    <p style="color:#667799; font-size:0.8rem;">Analytical Chemistry SGD 2026</p>
</div>
""", unsafe_allow_html=True)

pages = [
    "🏠 Title",
    "📖 Background", 
    "🔬 UV-Vis Spectroscopy",
    "🧪 HPLC Chromatography",
    "⚙️ Workflow & Team",
    "📚 Conclusion"
]

selected_page = st.sidebar.radio("Navigate", pages, index=0)

# ============================================================
# SLIDE 1: TITLE
# ============================================================
if selected_page == pages[0]:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style="text-align:center; padding:3rem 0;">
            <div style="font-size:4rem; margin-bottom:1rem;">🧪</div>
            <h1 style="font-size:3.5rem;">Analytical Strategies for Vitamin B₂</h1>
            <p class="subtitle" style="font-size:1.4rem;">Riboflavin · API &amp; Multivitamin Tablets</p>
            <p style="color:#667799; font-size:1.1rem; margin-top:1rem;">
                📅 2026 AC II · SGD &nbsp;|&nbsp; 👥 Group X &nbsp;|&nbsp; ⏱ ≤ 8 min
            </p>
        </div>
        """, unsafe_allow_html=True)

# ============================================================
# SLIDE 2: BACKGROUND
# ============================================================
elif selected_page == pages[1]:
    st.markdown("<h1>1. Background</h1>", unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Why Vitamin B₂ (Riboflavin)?</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="glass-card">
            <h3>🔬 Key Facts</h3>
            <p><strong>Vitamin B₂</strong> is water-soluble and essential for:</p>
            <ul style="color:#c8d6e5; padding-left:1.2rem;">
                <li>⚡ Energy metabolism</li>
                <li>🧴 Skin &amp; mucosal health</li>
                <li>🌱 Growth &amp; development</li>
            </ul>
            <p style="color:#8899bb; margin-top:0.8rem;">Found in animal organs, eggs, milk, green leafy vegetables.</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="highlight">
            <strong>🎯 Goal:</strong> Sample, pretreat, separate, identify &amp; quantify Vitamin B₂ in API and complex multivitamin tablets.
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div style="display:flex; align-items:center; justify-content:center; background:rgba(0,0,0,0.2); border-radius:20px; border:1px solid rgba(255,255,255,0.05); text-align:center; padding:2rem; min-height:300px;">
            <div>
                <div style="font-size:4rem; color:#00ff88;">💊</div>
                <p style="color:#8899bb; font-size:1.1rem; margin-top:0.5rem;">API + Multivitamin Tablets</p>
                <p style="color:#667799; font-size:0.85rem;">C₁₇H₂₀N₄O₆ · MW 376.36</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ============================================================
# SLIDE 3: UV-Vis SPECTROSCOPY (ANIMATED)
# ============================================================
elif selected_page == pages[2]:
    st.markdown("<h1>2. Task A – Spectroscopy</h1>", unsafe_allow_html=True)
    st.markdown('<p class="subtitle">UV-Vis Spectrophotometry for API Identification</p>', unsafe_allow_html=True)

    # --- Animation Controls ---
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        st.markdown("**🎮 Animation Controls**")
        play_anim = st.button("▶️ Play Animation", use_container_width=True)
        reset_anim = st.button("⏹️ Reset", use_container_width=True)

    with col3:
        st.markdown("**🎯 Manual Control**")
        conc = st.slider("Concentration (µg/mL)", 0.0, 10.0, 5.0, 0.1)

    # --- Animation State ---
    if "anim_running" not in st.session_state:
        st.session_state.anim_running = False
        st.session_state.anim_conc = 0.0

    if play_anim:
        st.session_state.anim_running = True
        st.session_state.anim_conc = 0.0

    if reset_anim:
        st.session_state.anim_running = False
        st.session_state.anim_conc = 0.0

    # --- Update concentration ---
    if st.session_state.anim_running:
        st.session_state.anim_conc += 0.15
        if st.session_state.anim_conc > 10.0:
            st.session_state.anim_conc = 10.0
            st.session_state.anim_running = False

    # Use slider if not animating, else use anim value
    if st.session_state.anim_running:
        current_conc = st.session_state.anim_conc
    else:
        current_conc = conc

    absorbance = 0.0485 * current_conc + 0.001

    # --- Create the Plot ---
    fig = go.Figure()

    # Full calibration curve (always visible)
    x_calib = [0, 2, 4, 6, 8, 10]
    y_calib = [0.000, 0.098, 0.195, 0.292, 0.388, 0.485]

    fig.add_trace(go.Scatter(
        x=x_calib,
        y=y_calib,
        mode='markers+lines',
        name='Calibration Curve',
        marker=dict(color='#00ff88', size=10, symbol='diamond'),
        line=dict(color='#00ff88', width=3, dash='dot'),
        hovertemplate='Conc: %{x:.1f} µg/mL<br>Abs: %{y:.3f}<extra></extra>'
    ))

    # Animated sample point (moving)
    fig.add_trace(go.Scatter(
        x=[current_conc],
        y=[absorbance],
        mode='markers',
        name='Your Sample',
        marker=dict(
            color='#ff6b6b',
            size=18,
            symbol='star',
            line=dict(color='white', width=2)
        ),
        hovertemplate='<b>Your Sample</b><br>Conc: %{x:.1f} µg/mL<br>Abs: %{y:.3f}<extra></extra>'
    ))

    # --- Animated Trace: The "Ghost" Path (trail) ---
    if current_conc > 0:
        x_trail = [0, current_conc]
        y_trail = [0.001, absorbance]
        fig.add_trace(go.Scatter(
            x=x_trail,
            y=y_trail,
            mode='lines',
            name='Path',
            line=dict(color='rgba(255, 107, 107, 0.3)', width=2, dash='dash'),
            showlegend=False
        ))

    fig.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis_title='Concentration (µg/mL)',
        yaxis_title='Absorbance',
        xaxis=dict(
            gridcolor='rgba(255,255,255,0.03)',
            range=[-0.5, 10.5],
            zeroline=True,
            zerolinecolor='rgba(255,255,255,0.1)'
        ),
        yaxis=dict(
            gridcolor='rgba(255,255,255,0.03)',
            range=[-0.02, 0.55],
            zeroline=True,
            zerolinecolor='rgba(255,255,255,0.1)'
        ),
        height=400,
        margin=dict(l=50, r=30, t=30, b=50),
        hovermode='closest'
    )

    # --- Display the chart ---
    st.plotly_chart(fig, use_container_width=True, key="uvvis_chart")

    # --- Metrics (with live updates) ---
    col_a, col_b, col_c, col_d = st.columns(4)

    with col_a:
        st.markdown(f"""
        <div class="metric-box">
            <div class="value" style="color:#ff6b6b;">{current_conc:.1f}</div>
            <div class="label">Concentration (µg/mL)</div>
        </div>
        """, unsafe_allow_html=True)

    with col_b:
        st.markdown(f"""
        <div class="metric-box">
            <div class="value" style="color:#00ff88;">{absorbance:.3f}</div>
            <div class="label">Absorbance @ 444 nm</div>
        </div>
        """, unsafe_allow_html=True)

    with col_c:
        st.markdown("""
        <div class="metric-box">
            <div class="value" style="color:#00ccff;">> 0.999</div>
            <div class="label">R² Value</div>
        </div>
        """, unsafe_allow_html=True)

    with col_d:
        st.markdown("""
        <div class="metric-box">
            <div class="value" style="color:#ffd93d;">0.2 µg/mL</div>
            <div class="label">LOD</div>
        </div>
        """, unsafe_allow_html=True)

    # --- Status indicator ---
    if st.session_state.anim_running:
        st.info(f"🎬 Animating... Concentration: {current_conc:.1f} µg/mL | Absorbance: {absorbance:.3f}")
    else:
        if current_conc >= 10:
            st.success("✅ Animation complete! The sample point has reached the top of the calibration curve.")
        else:
            st.info("💡 Click 'Play Animation' to watch the absorbance grow! Or use the slider to control it manually.")

    # --- Explanation ---
    with st.expander("📖 What's happening here?"):
        st.markdown("""
        - **The green curve** is the Beer–Lambert calibration curve.
        - **The red star** is your sample — it moves as concentration changes.
        - **The dashed red line** shows the path from zero to the current point.
        - **R² > 0.999** means the method is linear and accurate.
        - **LOD = 0.2 µg/mL** is the lowest concentration you can detect.
        """)

# ============================================================
# SLIDE 4: HPLC CHROMATOGRAPHY
# ============================================================
elif selected_page == pages[3]:
    st.markdown("<h1>3. Task B – Chromatography</h1>", unsafe_allow_html=True)
    st.markdown('<p class="subtitle">HPLC-UV for Multivitamin Tablets</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="glass-card">
            <h3>🧪 Sample Pretreatment</h3>
            <ul style="color:#c8d6e5; padding-left:1.2rem;">
                <li>Crush tablets in phosphate buffer (pH 6.8)</li>
                <li>SPE (C18) for clean-up</li>
                <li>0.45 µm filtration</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="glass-card">
            <h3>⚙️ HPLC Conditions</h3>
            <ul style="color:#c8d6e5; padding-left:1.2rem;">
                <li><strong>Column:</strong> C18 (150 × 4.6 mm, 5 µm)</li>
                <li><strong>Mobile phase:</strong> Methanol : buffer (30:70), pH 6.8</li>
                <li><strong>Flow:</strong> 1.0 mL/min · UV @ 444 nm</li>
                <li><strong>Run time:</strong> 10 min</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="highlight">
            <strong>🧩 Matrix Interferences:</strong> Other vitamins (B1, B3, B6, B12) separated by retention time. SPE removes non-polar interferences.
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown('<p style="color:#8899bb; font-size:0.9rem;">HPLC-UV chromatogram · Riboflavin @ ~5.2 min</p>', unsafe_allow_html=True)
        time = np.linspace(0, 10, 200)
        signal = 0.02 + 0.9 * np.exp(-((time - 5.2)**2) / 0.15) + 0.08 * np.exp(-((time - 3.5)**2) / 0.5) + 0.05 * np.exp(-((time - 7.0)**2) / 0.4)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=time,
            y=signal,
            mode='lines',
            name='Chromatogram',
            line=dict(color='#00ccff', width=2.5)
        ))
        fig.add_vline(x=5.2, line_dash="dash", line_color="#00ff88", annotation_text="Vitamin B₂", annotation_position="top right")
        fig.update_layout(
            template='plotly_dark',
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis_title='Time (min)',
            yaxis_title='Response (mAU)',
            height=350,
            margin=dict(l=40, r=20, t=40, b=40)
        )
        st.plotly_chart(fig, use_container_width=True)
        
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            st.markdown("""
            <div class="metric-box">
                <div class="value">> 95%</div>
                <div class="label">Recovery</div>
            </div>
            """, unsafe_allow_html=True)
        with col_b:
            st.markdown("""
            <div class="metric-box">
                <div class="value">< 2%</div>
                <div class="label">RSD</div>
            </div>
            """, unsafe_allow_html=True)
        with col_c:
            st.markdown("""
            <div class="metric-box">
                <div class="value">5.2 min</div>
                <div class="label">Retention Time</div>
            </div>
            """, unsafe_allow_html=True)

# ============================================================
# SLIDE 5: WORKFLOW & TEAM
# ============================================================
elif selected_page == pages[4]:
    st.markdown("<h1>4. Workflow &amp; Team</h1>", unsafe_allow_html=True)
    st.markdown('<p class="subtitle">From Sample to Result</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="workflow">
        <span class="workflow-step">🧪 Sample</span>
        <span class="workflow-arrow">→</span>
        <span class="workflow-step">🧹 SPE</span>
        <span class="workflow-arrow">→</span>
        <span class="workflow-step">🧫 Filtration</span>
        <span class="workflow-arrow">→</span>
        <span class="workflow-step">📊 HPLC</span>
        <span class="workflow-arrow">→</span>
        <span class="workflow-step" style="border-color:#00ff88;">✅ Result</span>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="glass-card">
            <h3>👥 Team Roles</h3>
            <div style="display:flex; flex-wrap:wrap; gap:0.5rem; margin-top:0.5rem;">
                <span style="background:rgba(0,255,136,0.05); padding:0.3rem 1.2rem; border-radius:30px; border:1px solid rgba(0,255,136,0.1); color:#c8d6e5; font-size:0.85rem;">🔬 Spectroscopy</span>
                <span style="background:rgba(0,255,136,0.05); padding:0.3rem 1.2rem; border-radius:30px; border:1px solid rgba(0,255,136,0.1); color:#c8d6e5; font-size:0.85rem;">🧪 Chromatography</span>
                <span style="background:rgba(0,255,136,0.05); padding:0.3rem 1.2rem; border-radius:30px; border:1px solid rgba(0,255,136,0.1); color:#c8d6e5; font-size:0.85rem;">📊 Data Analysis</span>
                <span style="background:rgba(0,255,136,0.05); padding:0.3rem 1.2rem; border-radius:30px; border:1px solid rgba(0,255,136,0.1); color:#c8d6e5; font-size:0.85rem;">📋 Sample Prep</span>
                <span style="background:rgba(0,255,136,0.05); padding:0.3rem 1.2rem; border-radius:30px; border:1px solid rgba(0,255,136,0.1); color:#c8d6e5; font-size:0.85rem;">🎤 Presentation</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="glass-card">
            <h3>⭐ Evaluation</h3>
            <ul style="color:#c8d6e5; padding-left:1.2rem; margin-top:0.2rem; font-size:0.95rem;">
                <li><strong style="color:#00ff88;">40%</strong> Scientific rigor &amp; logic</li>
                <li><strong style="color:#00ff88;">40%</strong> Method design (spectroscopy + chromatography)</li>
                <li><strong style="color:#00ff88;">20%</strong> Teamwork &amp; individual contribution</li>
            </ul>
            <div class="highlight" style="margin-top:0.8rem;">
                💡 <span style="color:#8899bb;">Active contribution → higher individual mark</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ============================================================
# SLIDE 6: CONCLUSION
# ============================================================
elif selected_page == pages[5]:
    st.markdown("<h1>5. Conclusion</h1>", unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Thank you for your attention!</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div class="glass-card">
            <h3>📚 Key References</h3>
            <ul style="color:#c8d6e5; padding-left:1.2rem;">
                <li>USP-NF Monograph: Riboflavin</li>
                <li>European Pharmacopoeia (Ph. Eur.) – Vitamin B₂</li>
                <li>AOAC International – HPLC methods for vitamins</li>
                <li>Skoog, D. A. et al. <em>Principles of Instrumental Analysis</em></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="highlight" style="font-size:1.1rem; padding:1.2rem 1.5rem;">
            <strong>🧪 Take-home:</strong> UV-Vis + HPLC provide a robust analytical strategy for Vitamin B₂ in both API and complex matrices.
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div style="text-align:center; padding:1rem 0; color:#667799;">
            <p>👥 Group X · 2026 AC II · SGD</p>
        </div>
        """, unsafe_allow_html=True)

# ============================================================
# FOOTER
# ============================================================
st.markdown("""
<div class="footer">
    <p>🧪 Analytical Chemistry SGD 2026 · Group X</p>
</div>
""", unsafe_allow_html=True)