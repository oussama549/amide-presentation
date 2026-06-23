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
        hovermode='closest',
        updatemenus=[{
            'type': 'buttons',
            'showactive': False,
            'buttons': [{
                'label': '▶️ Play',
                'method': 'animate',
                'args': [None, {'frame': {'duration': 50, 'redraw': True}, 'fromcurrent': True}]
            }]
        }]
    )

    # --- Animate using frames (Plotly's built-in animation) ---
    if st.session_state.anim_running:
        frames = []
        for i in range(0, 21):
            c = i * 0.5
            a = 0.0485 * c + 0.001
            frames.append(go.Frame(
                data=[
                    go.Scatter(
                        x=[c],
                        y=[a],
                        mode='markers',
                        marker=dict(color='#ff6b6b', size=18, symbol='star')
                    ),
                    go.Scatter(
                        x=[0, c],
                        y=[0.001, a],
                        mode='lines',
                        line=dict(color='rgba(255, 107, 107, 0.3)', width=2, dash='dash')
                    )
                ],
                traces=[1, 2]
            ))
        fig.frames = frames

    # --- Display the chart ---
    chart = st.plotly_chart(fig, use_container_width=True, key="uvvis_chart")

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
