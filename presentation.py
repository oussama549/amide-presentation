import streamlit as st
import plotly.graph_objects as go
import numpy as np
import pandas as pd

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="Amide Bond | Drug Discovery",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# CUSTOM CSS
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
    .footer {
        text-align: center;
        padding: 2rem 0 1rem;
        color: #445566;
        border-top: 1px solid rgba(255, 255, 255, 0.03);
        margin-top: 2rem;
    }
    .drug-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
        margin: 1rem 0;
    }
    .drug-card {
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.06);
        border-radius: 16px;
        padding: 1rem;
        text-align: center;
        color: #c8d6e5;
        transition: all 0.3s ease;
    }
    .drug-card:hover {
        border-color: #00ff88;
        transform: translateY(-3px);
    }
    .drug-card .name {
        font-size: 1.2rem;
        font-weight: 700;
        color: #00ff88;
        margin-bottom: 0.3rem;
    }
    .drug-card .use {
        font-size: 0.85rem;
        color: #667799;
    }
    .amide-structure {
        font-family: 'Courier New', monospace;
        color: #00ff88;
        font-size: 1.1rem;
        background: rgba(0,0,0,0.3);
        padding: 0.8rem 1rem;
        border-radius: 12px;
        text-align: center;
        border: 1px solid rgba(0,255,136,0.1);
        margin: 0.5rem 0;
        line-height: 1.8;
        letter-spacing: 0.5px;
    }
    .amide-structure .highlight-o { color: #ff6b6b; }
    .amide-structure .highlight-n { color: #00ccff; }
    .amide-structure .highlight-c { color: #ffd93d; }
    .amide-structure .highlight-h { color: #ffffff; }
</style>
""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR NAVIGATION
# ============================================================
st.sidebar.markdown("""
<div style="text-align:center; padding:1rem 0;">
    <h3 style="color:#00ff88; -webkit-text-fill-color:#00ff88;">🧬 Amide Bond</h3>
    <p style="color:#667799; font-size:0.8rem;">Drug Discovery Presentation</p>
</div>
""", unsafe_allow_html=True)

pages = [
    "🏠 Title",
    "📖 What is Amide Formation?",
    "💊 Why Amides in Drugs?",
    "🧪 Real Drug Examples",
    "🚀 Modern Applications",
    "📚 Conclusion"
]

selected_page = st.sidebar.radio("Navigate", pages, index=0)

# ============================================================
# 3D MOLECULE GENERATOR (PLOTLY)
# ============================================================
def generate_molecule_3d(atom_positions, bonds, atom_colors=None, atom_labels=None, title=""):
    """
    Generate a 3D molecule plot using Plotly.
    
    atom_positions: list of [x, y, z] coordinates
    bonds: list of [i, j] indices connecting atoms
    atom_colors: list of colors for each atom
    atom_labels: list of labels for each atom
    """
    
    if atom_colors is None:
        atom_colors = ['#00ff88'] * len(atom_positions)
    if atom_labels is None:
        atom_labels = [''] * len(atom_positions)
    
    # Create atom traces
    atom_x = [p[0] for p in atom_positions]
    atom_y = [p[1] for p in atom_positions]
    atom_z = [p[2] for p in atom_positions]
    
    atom_trace = go.Scatter3d(
        x=atom_x,
        y=atom_y,
        z=atom_z,
        mode='markers+text',
        marker=dict(
            size=12,
            color=atom_colors,
            opacity=0.9,
            line=dict(width=2, color='white')
        ),
        text=atom_labels,
        textposition='top center',
        textfont=dict(color='white', size=10),
        hoverinfo='text',
        name='Atoms'
    )
    
    # Create bond traces
    bond_traces = []
    for i, j in bonds:
        bond_trace = go.Scatter3d(
            x=[atom_positions[i][0], atom_positions[j][0]],
            y=[atom_positions[i][1], atom_positions[j][1]],
            z=[atom_positions[i][2], atom_positions[j][2]],
            mode='lines',
            line=dict(color='rgba(255,255,255,0.5)', width=4),
            hoverinfo='none',
            showlegend=False
        )
        bond_traces.append(bond_trace)
    
    # Combine all traces
    traces = [atom_trace] + bond_traces
    
    # Layout
    layout = go.Layout(
        title=title,
        scene=dict(
            xaxis=dict(showticklabels=False, showgrid=False, zeroline=False, title=''),
            yaxis=dict(showticklabels=False, showgrid=False, zeroline=False, title=''),
            zaxis=dict(showticklabels=False, showgrid=False, zeroline=False, title=''),
            camera=dict(
                eye=dict(x=1.5, y=1.5, z=1.5)
            ),
            bgcolor='rgba(0,0,0,0)'
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0, r=0, t=30, b=0),
        height=350,
        hovermode='closest'
    )
    
    fig = go.Figure(data=traces, layout=layout)
    return fig

# ============================================================
# AMIDE MOLECULE DATA
# ============================================================
def get_amide_data():
    """Amide structure: paracetamol-like"""
    atoms = [
        [0.0, 0.0, 0.0],   # C
        [1.2, 0.0, 0.0],   # C
        [1.8, 1.2, 0.0],   # C
        [1.2, 2.4, 0.0],   # C
        [0.0, 2.4, 0.0],   # C
        [-0.6, 1.2, 0.0],  # C
        [1.8, -1.2, 0.0],  # C=O
        [1.2, -2.4, 0.0],  # N
        [1.8, -3.6, 0.0],  # C
        [0.6, -2.4, 0.0],  # H
        [2.0, 3.0, 0.0],   # O
        [2.6, 4.2, 0.0],   # C
        [3.8, 4.2, 0.0],   # C
        [4.4, 5.4, 0.0],   # C
        [3.8, 6.6, 0.0],   # C
        [2.6, 6.6, 0.0],   # C
        [2.0, 5.4, 0.0],   # C
    ]
    
    bonds = [
        [0,1], [1,2], [2,3], [3,4], [4,5], [5,0],
        [1,6], [6,7], [7,8], [7,9], [3,10],
        [10,11], [11,12], [12,13], [13,14], [14,15], [15,16], [16,11]
    ]
    
    colors = ['#00ff88'] * len(atoms)
    labels = [''] * len(atoms)
    
    return atoms, bonds, colors, labels

# ============================================================
# SLIDE 1: TITLE
# ============================================================
if selected_page == pages[0]:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style="text-align:center; padding:3rem 0;">
            <div style="font-size:4rem; margin-bottom:1rem;">🧬</div>
            <h1 style="font-size:3.5rem;">The Amide Bond</h1>
            <p class="subtitle" style="font-size:1.4rem;">The Unsung Hero of Modern Medicine</p>
            <p style="color:#667799; font-size:1.1rem; margin-top:1rem;">
                Amide Formation in Organic Synthesis &amp; Drug Discovery
            </p>
            <p style="color:#445566; font-size:0.9rem; margin-top:1.5rem;">
                <i class="fas fa-arrow-right"></i> Select a slide from the sidebar
            </p>
        </div>
        """, unsafe_allow_html=True)

# ============================================================
# SLIDE 2: WHAT IS AMIDE FORMATION? (MODIFIED)
# ============================================================
elif selected_page == pages[1]:
    st.markdown("<h1>What is Amide Formation?</h1>", unsafe_allow_html=True)
    st.markdown('<p class="subtitle">The Chemical Bond That Connects Medicine</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="glass-card">
            <h3>🔬 Simple Definition</h3>
            <p>An <strong style="color:#00ff88;">amide</strong> is formed when a <strong style="color:#00ccff;">carboxylic acid</strong> reacts with an <strong style="color:#ff6b6b;">amine</strong>.</p>
            <p style="margin-top:0.8rem; color:#8899bb; font-size:0.95rem;">
                R-COOH + R'-NH₂ → R-CONH-R' + H₂O
            </p>
        </div>
        """, unsafe_allow_html=True)

        # ===== AMIDE STRUCTURE DISPLAY =====
        st.markdown("""
        <div class="glass-card">
            <h3>🧬 Amide Bond Structure</h3>
            <div class="amide-structure">
                <span style="color:#ffd93d;">R</span> — <span style="color:#ff6b6b;">C</span> <span style="color:#ff6b6b;">=</span> <span style="color:#ff6b6b;">O</span><br>
                <span style="padding-left:1.8rem;">|</span><br>
                <span style="padding-left:1.5rem; color:#00ccff;">N</span> — <span style="color:#ffffff;">H</span><br>
                <span style="padding-left:1.5rem;">|</span><br>
                <span style="padding-left:1.2rem; color:#ffd93d;">R'</span>
            </div>
            <p style="color:#8899bb; font-size:0.85rem; margin-top:0.3rem; text-align:center;">
                <span style="color:#ff6b6b;">●</span> Carbonyl carbon (C=O) &nbsp;·&nbsp;
                <span style="color:#00ccff;">●</span> Nitrogen (N) &nbsp;·&nbsp;
                <span style="color:#ffd93d;">●</span> Carbon (C) &nbsp;·&nbsp;
                <span style="color:#ffffff;">●</span> Hydrogen (H)
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="glass-card">
            <h3>💡 Why Is It Important?</h3>
            <ul style="color:#c8d6e5; padding-left:1.2rem;">
                <li>🧬 Found in <strong style="color:#00ff88;">>25% of FDA-approved drugs</strong></li>
                <li>🔗 Forms the backbone of <strong style="color:#00ccff;">peptides and proteins</strong></li>
                <li>💊 Used in <strong style="color:#ff6b6b;">drug discovery</strong> to create new medicines</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="glass-card" style="text-align:center;">
            <h3>🧬 Interactive Amide Structure</h3>
            <p style="color:#8899bb; font-size:0.85rem; margin-bottom:0.5rem;">
                🖱️ Drag to rotate · Scroll to zoom
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # 3D molecule using Plotly
        atoms, bonds, colors, labels = get_amide_data()
        fig = generate_molecule_3d(atoms, bonds, colors, labels, title="Amide Structure")
        st.plotly_chart(fig, use_container_width=True)

# ============================================================
# SLIDE 3: WHY AMIDES IN DRUGS?
# ============================================================
elif selected_page == pages[2]:
    st.markdown("<h1>Why Amides in Drugs?</h1>", unsafe_allow_html=True)
    st.markdown('<p class="subtitle">The "Smart" Reason Behind Their Popularity</p>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="glass-card">
            <h3>✅ Stability</h3>
            <p>Amide bonds are <strong style="color:#00ff88;">stable</strong> — they don't break easily in the body.</p>
            <p style="color:#8899bb; font-size:0.9rem; margin-top:0.5rem;">Drugs <strong>last longer</strong> in the body.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="glass-card">
            <h3>🧬 Bioavailability</h3>
            <p>Amides can be designed to <strong style="color:#00ccff;">cross cell membranes</strong>.</p>
            <p style="color:#8899bb; font-size:0.9rem; margin-top:0.5rem;">Drugs <strong>reach their targets</strong>.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="glass-card">
            <h3>🔬 Versatility</h3>
            <p>Amides can be <strong style="color:#ff6b6b;">tuned</strong> by changing the groups attached to them.</p>
            <p style="color:#8899bb; font-size:0.9rem; margin-top:0.5rem;">Chemists can <strong>design better drugs</strong>.</p>
        </div>
        """, unsafe_allow_html=True)

# ============================================================
# SLIDE 4: REAL DRUG EXAMPLES
# ============================================================
elif selected_page == pages[3]:
    st.markdown("<h1>Real Drug Examples</h1>", unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Amide Bonds in Medicines You Know</p>', unsafe_allow_html=True)

    st.markdown("""
    <div class="drug-grid">
        <div class="drug-card">
            <div class="name">💊 Paracetamol</div>
            <div class="use">Painkiller · Fever reducer</div>
            <p style="color:#667799; font-size:0.75rem; margin-top:0.3rem;">Contains an amide bond</p>
        </div>
        <div class="drug-card">
            <div class="name">🧪 Penicillin</div>
            <div class="use">Antibiotic</div>
            <p style="color:#667799; font-size:0.75rem; margin-top:0.3rem;">Contains an amide bond</p>
        </div>
        <div class="drug-card">
            <div class="name">❤️ Atorvastatin</div>
            <div class="use">Cholesterol drug (Lipitor)</div>
            <p style="color:#667799; font-size:0.75rem; margin-top:0.3rem;">Contains an amide bond</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 3D molecules for drugs
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("#### 💊 Paracetamol")
        atoms, bonds, colors, labels = get_amide_data()  # Using same for simplicity
        fig = generate_molecule_3d(atoms, bonds, colors, labels, title="Paracetamol")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown("#### 🧪 Penicillin")
        # Slightly different structure for penicillin
        atoms2 = [[p[0] + 3, p[1] + 2, p[2] + 1] for p in atoms[:10]]  # Offset for visual difference
        fig2 = generate_molecule_3d(atoms2, bonds[:10], colors[:10], labels[:10], title="Penicillin")
        st.plotly_chart(fig2, use_container_width=True)

    with col3:
        st.markdown("#### ❤️ Atorvastatin")
        atoms3 = [[p[0] + 6, p[1] + 4, p[2] + 2] for p in atoms[:10]]
        fig3 = generate_molecule_3d(atoms3, bonds[:10], colors[:10], labels[:10], title="Atorvastatin")
        st.plotly_chart(fig3, use_container_width=True)

# ============================================================
# SLIDE 5: MODERN APPLICATIONS
# ============================================================
elif selected_page == pages[4]:
    st.markdown("<h1>Modern Applications</h1>", unsafe_allow_html=True)
    st.markdown('<p class="subtitle">How Amide Formation Is Used in Drug Discovery Today</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="glass-card">
            <h3>🔬 Peptide Synthesis</h3>
            <p>Amide formation is used to <strong style="color:#00ff88;">connect amino acids</strong> into peptides.</p>
            <p style="color:#8899bb; font-size:0.9rem; margin-top:0.5rem;">Peptides are <strong style="color:#00ccff;">the future of medicine</strong>.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="glass-card">
            <h3>🧪 Drug Libraries</h3>
            <p>Amide coupling creates <strong style="color:#ff6b6b;">thousands of drug candidates</strong> quickly.</p>
            <p style="color:#8899bb; font-size:0.9rem; margin-top:0.5rem;">This is called <strong style="color:#ffd93d;">combinatorial chemistry</strong>.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="glass-card">
            <h3>💊 Lead Optimization</h3>
            <p>Amide formation is used to <strong style="color:#00ccff;">modify</strong> promising compounds.</p>
            <p style="color:#8899bb; font-size:0.9rem; margin-top:0.5rem;">This is how <strong style="color:#00ff88;">drugs get improved</strong>.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="glass-card">
            <h3>🧬 Targeted Therapies</h3>
            <p>Amide bonds create <strong style="color:#ff6b6b;">targeted therapies</strong> that attack only cancer cells.</p>
            <p style="color:#8899bb; font-size:0.9rem; margin-top:0.5rem;">This is the <strong style="color:#ffd93d;">future of medicine</strong>.</p>
        </div>
        """, unsafe_allow_html=True)

# ============================================================
# SLIDE 6: CONCLUSION
# ============================================================
elif selected_page == pages[5]:
    st.markdown("<h1>Conclusion</h1>", unsafe_allow_html=True)
    st.markdown('<p class="subtitle">The Amide Bond — The Unsung Hero of Modern Medicine</p>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div class="glass-card">
            <h3>📌 Key Takeaways</h3>
            <ul style="color:#c8d6e5; padding-left:1.2rem;">
                <li>🧬 Found in <strong style="color:#00ff88;">>25% of all drugs</strong></li>
                <li>💊 Used in <strong style="color:#00ccff;">drug discovery</strong> to create new medicines</li>
                <li>🔬 The foundation of <strong style="color:#ff6b6b;">peptides and proteins</strong></li>
                <li>🚀 The <strong style="color:#ffd93d;">future of medicine</strong></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="highlight" style="font-size:1.1rem; padding:1.2rem 1.5rem; text-align:center;">
            <strong>🧪 The amide bond is not just a chemical bond —</strong><br>
            <span style="color:#00ff88;">it's the connection between chemistry and medicine.</span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="text-align:center; padding:1rem 0; color:#667799;">
            <p>🧬 Thank you for your attention</p>
            <p style="font-size:0.85rem; color:#445566; margin-top:0.5rem;">Questions?</p>
        </div>
        """, unsafe_allow_html=True)

# ============================================================
# FOOTER
# ============================================================
st.markdown("""
<div class="footer">
    <p>🧬 Amide Formation · Drug Discovery Presentation</p>
</div>
""", unsafe_allow_html=True)
