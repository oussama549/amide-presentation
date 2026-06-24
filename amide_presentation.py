import streamlit as st
import streamlit.components.v1 as components
import plotly.graph_objects as go
import numpy as np

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
# 3D MOLECULE VIEWER (USING HTML COMPONENT)
# ============================================================
def render_3d_molecule(smiles, height=350):
    """Render a 3D molecule from SMILES using py3Dmol"""
    html_code = f"""
    <div id="molViewer" style="width:100%; height:{height}px; border-radius:16px; background:#0a0a1a; border:1px solid rgba(255,255,255,0.05);"></div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/3Dmol/2.0.2/3Dmol-min.js">
    </script>
    <script>
        document.addEventListener('DOMContentLoaded', function() {{
            var viewer = $3Dmol.createViewer('molViewer', {{
                backgroundColor: '0x0a0a1a'
            }});
            viewer.addModel("{smiles}", "smiles");
            viewer.setStyle({{}}, {{ stick: {{}}, sphere: {{ scale: 0.3 }} }});
            viewer.zoomTo();
            viewer.rotate(90);
            viewer.render();
        }});
    </script>
    """
    return components.html(html_code, height=height + 20)

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
# SLIDE 2: WHAT IS AMIDE FORMATION?
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
        render_3d_molecule("COC(=O)Nc1ccc(cc1)O", height=320)

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
        render_3d_molecule("CC(=O)Nc1ccc(cc1)O", height=200)

    with col2:
        st.markdown("#### 🧪 Penicillin")
        render_3d_molecule("CC1(C)SC2C(NC(=O)Cc3ccccc3)C(=O)N2C1C(=O)O", height=200)

    with col3:
        st.markdown("#### ❤️ Atorvastatin")
        render_3d_molecule("CC(C)c1c(C(=O)Nc2ccc(cc2)F)c(Cc3ccccc3)c(C(=O)O)c(n1)C(C)C", height=200)

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
