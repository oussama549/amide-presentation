import streamlit as st
import plotly.graph_objects as go
from PIL import Image
import requests
from io import BytesIO

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="Amide Formation | Drug Discovery",
    page_icon="🧬",
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
    <h3 style="color:#00ff88; -webkit-text-fill-color:#00ff88;">🧬 Amide Formation</h3>
    <p style="color:#667799; font-size:0.8rem;">Drug Discovery Presentation</p>
</div>
""", unsafe_allow_html=True)

pages = [
    "🏠 Title",
    "📖 What is Amide Formation?",
    "🔬 The Mechanism",
    "💊 Why Amides in Drugs?",
    "🧪 Real Drug Examples",
    "🚀 Modern Applications",
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
            <div style="font-size:4rem; margin-bottom:1rem;">🧬</div>
            <h1 style="font-size:3.5rem;">The Amide Bond</h1>
            <p class="subtitle" style="font-size:1.4rem;">The Unsung Hero of Modern Medicine</p>
            <p style="color:#667799; font-size:1.1rem; margin-top:1rem;">
                Amide Formation in Organic Synthesis &amp; Drug Discovery
            </p>
            <p style="color:#445566; font-size:0.9rem; margin-top:1.5rem;">
                <i class="fas fa-arrow-right"></i> Select a slide from the sidebar to begin
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
        <div style="display:flex; align-items:center; justify-content:center; background:rgba(0,0,0,0.2); border-radius:20px; border:1px solid rgba(255,255,255,0.05); text-align:center; padding:2rem; min-height:300px;">
            <div>
                <div style="font-size:5rem; color:#00ff88;">🧬</div>
                <p style="color:#8899bb; font-size:1.1rem; margin-top:0.5rem;">
                    <strong style="color:#00ff88;">Amide Bond</strong>
                </p>
                <p style="color:#667799; font-size:0.85rem;">
                    R-C(=O)-NHR'
                </p>
                <div style="margin-top:1rem; display:flex; gap:0.5rem; justify-content:center; flex-wrap:wrap;">
                    <span style="background:rgba(0,255,136,0.05); padding:0.2rem 1rem; border-radius:20px; border:1px solid rgba(0,255,136,0.1); font-size:0.75rem; color:#8899bb;">Stable</span>
                    <span style="background:rgba(0,255,136,0.05); padding:0.2rem 1rem; border-radius:20px; border:1px solid rgba(0,255,136,0.1); font-size:0.75rem; color:#8899bb;">Bioavailable</span>
                    <span style="background:rgba(0,255,136,0.05); padding:0.2rem 1rem; border-radius:20px; border:1px solid rgba(0,255,136,0.1); font-size:0.75rem; color:#8899bb;">Versatile</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ============================================================
# SLIDE 3: THE MECHANISM
# ============================================================
elif selected_page == pages[2]:
    st.markdown("<h1>The Mechanism</h1>", unsafe_allow_html=True)
    st.markdown('<p class="subtitle">How Amides Are Formed</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="glass-card">
            <h3>⚡ Simple Mechanism</h3>
            <p><strong style="color:#00ff88;">Step 1:</strong> Acid chloride + Amine</p>
            <p style="color:#8899bb; font-size:0.95rem; padding-left:1rem;">
                R-COCl + R'-NH₂ → R-CONH-R' + HCl
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="glass-card">
            <h3>🔬 Key Points</h3>
            <ul style="color:#c8d6e5; padding-left:1.2rem;">
                <li>✅ <strong style="color:#00ff88;">Fast</strong> reaction</li>
                <li>✅ <strong style="color:#00ccff;">High yield</strong></li>
                <li>✅ <strong style="color:#ff6b6b;">Versatile</strong> — works with many substrates</li>
                <li>⚠️ Requires <strong style="color:#ffd93d;">base</strong> to neutralize HCl</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        # Reaction mechanism visual (text-based)
        st.markdown("""
        <div style="background:rgba(0,0,0,0.2); border-radius:20px; border:1px solid rgba(255,255,255,0.05); padding:2rem; text-align:center; min-height:300px; display:flex; flex-direction:column; justify-content:center;">
            <div style="font-size:2.5rem; color:#00ff88; margin-bottom:0.5rem;">
                R-COCl
            </div>
            <div style="font-size:2rem; color:#8899bb;">+</div>
            <div style="font-size:2.5rem; color:#00ccff; margin-bottom:0.5rem;">
                R'-NH₂
            </div>
            <div style="font-size:2rem; color:#ffd93d; margin:0.5rem 0;">⬇️</div>
            <div style="font-size:2.5rem; color:#00ff88;">
                R-CONH-R'
            </div>
            <div style="font-size:1.2rem; color:#667799; margin-top:0.5rem;">
                <span style="color:#00ff88;">+</span> HCl
            </div>
            <div style="margin-top:1rem; display:flex; gap:0.5rem; justify-content:center; flex-wrap:wrap;">
                <span style="background:rgba(0,255,136,0.05); padding:0.2rem 1rem; border-radius:20px; border:1px solid rgba(0,255,136,0.1); font-size:0.75rem; color:#8899bb;">🔬 Acid Chloride</span>
                <span style="background:rgba(0,255,136,0.05); padding:0.2rem 1rem; border-radius:20px; border:1px solid rgba(0,255,136,0.1); font-size:0.75rem; color:#8899bb;">🧪 Amine</span>
                <span style="background:rgba(0,255,136,0.05); padding:0.2rem 1rem; border-radius:20px; border:1px solid rgba(0,255,136,0.1); font-size:0.75rem; color:#8899bb;">💊 Amide</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ============================================================
# SLIDE 4: WHY AMIDES IN DRUGS?
# ============================================================
elif selected_page == pages[3]:
    st.markdown("<h1>Why Amides in Drugs?</h1>", unsafe_allow_html=True)
    st.markdown('<p class="subtitle">The "Smart" Reason Behind Their Popularity</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="glass-card">
            <h3>✅ Stability</h3>
            <p>Amide bonds are <strong style="color:#00ff88;">stable</strong> — they don't break easily in the body.</p>
            <p style="color:#8899bb; font-size:0.9rem; margin-top:0.5rem;">This means drugs <strong>last longer</strong> in the body.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="glass-card">
            <h3>🧬 Bioavailability</h3>
            <p>Amides can be designed to <strong style="color:#00ccff;">cross cell membranes</strong> and reach their targets.</p>
            <p style="color:#8899bb; font-size:0.9rem; margin-top:0.5rem;">This means drugs <strong>work better</strong>.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="glass-card">
            <h3>🔬 Versatility</h3>
            <p>Amides can be <strong style="color:#ff6b6b;">tuned</strong> by changing the groups attached to them.</p>
            <p style="color:#8899bb; font-size:0.9rem; margin-top:0.5rem;">This means chemists can <strong>design better drugs</strong>.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="glass-card">
            <h3>💊 Drug Discovery</h3>
            <p>Medicinal chemists use <strong style="color:#ffd93d;">amide coupling</strong> to create new drug candidates.</p>
            <p style="color:#8899bb; font-size:0.9rem; margin-top:0.5rem;">This is <strong>one of the most common reactions</strong> in drug discovery.</p>
        </div>
        """, unsafe_allow_html=True)

# ============================================================
# SLIDE 5: REAL DRUG EXAMPLES
# ============================================================
elif selected_page == pages[4]:
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
        <div class="drug-card">
            <div class="name">🧬 Nirmatrelvir</div>
            <div class="use">COVID-19 antiviral (Paxlovid)</div>
            <p style="color:#667799; font-size:0.75rem; margin-top:0.3rem;">Contains an amide bond</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="highlight">
        <strong>📊 Did You Know?</strong> Over <strong style="color:#00ff88;">25%</strong> of all FDA-approved drugs contain an amide bond.
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# SLIDE 6: MODERN APPLICATIONS
# ============================================================
elif selected_page == pages[5]:
    st.markdown("<h1>Modern Applications</h1>", unsafe_allow_html=True)
    st.markdown('<p class="subtitle">How Amide Formation Is Used in Drug Discovery Today</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="glass-card">
            <h3>🔬 Peptide Synthesis</h3>
            <p>Amide formation is used to <strong style="color:#00ff88;">connect amino acids</strong> into peptides.</p>
            <p style="color:#8899bb; font-size:0.9rem; margin-top:0.5rem;">Peptides are <strong style="color:#00ccff;">the future of medicine</strong> — they're more specific and have fewer side effects.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="glass-card">
            <h3>🧪 Drug Libraries</h3>
            <p>Medicinal chemists use amide coupling to create <strong style="color:#ff6b6b;">thousands of drug candidates</strong> quickly.</p>
            <p style="color:#8899bb; font-size:0.9rem; margin-top:0.5rem;">This is called <strong style="color:#ffd93d;">combinatorial chemistry</strong>.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="glass-card">
            <h3>💊 Lead Optimization</h3>
            <p>Once a promising compound is found, amide formation is used to <strong style="color:#00ccff;">modify it</strong> and make it better.</p>
            <p style="color:#8899bb; font-size:0.9rem; margin-top:0.5rem;">This is how <strong style="color:#00ff88;">drugs get improved</strong>.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="glass-card">
            <h3>🧬 Targeted Therapies</h3>
            <p>Amide bonds are used to create <strong style="color:#ff6b6b;">targeted therapies</strong> — drugs that only attack cancer cells.</p>
            <p style="color:#8899bb; font-size:0.9rem; margin-top:0.5rem;">This is the <strong style="color:#ffd93d;">future of medicine</strong>.</p>
        </div>
        """, unsafe_allow_html=True)

# ============================================================
# SLIDE 7: CONCLUSION
# ============================================================
elif selected_page == pages[6]:
    st.markdown("<h1>Conclusion</h1>", unsafe_allow_html=True)
    st.markdown('<p class="subtitle">The Amide Bond — The Unsung Hero of Modern Medicine</p>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div class="glass-card">
            <h3>📌 Key Takeaways</h3>
            <ul style="color:#c8d6e5; padding-left:1.2rem;">
                <li>🧬 The amide bond is <strong style="color:#00ff88;">one of the most important bonds</strong> in organic chemistry</li>
                <li>💊 It is found in <strong style="color:#00ccff;">>25% of all drugs</strong></li>
                <li>🔬 It is used in <strong style="color:#ff6b6b;">drug discovery</strong> to create new medicines</li>
                <li>🧪 It is the foundation of <strong style="color:#ffd93d;">peptides and proteins</strong></li>
                <li>🚀 It is the <strong style="color:#00ff88;">future of medicine</strong></li>
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
