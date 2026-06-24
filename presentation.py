<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>Amide Bond | Interactive Drug Discovery</title>
    
    <!-- 3Dmol.js for interactive molecules -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/3Dmol/2.0.2/3Dmol-min.js">
    </script>
    
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #060a14;
            color: #e0e6ed;
            overflow: hidden;
            height: 100vh;
            width: 100vw;
        }

        .slides-wrapper {
            display: flex;
            flex-direction: column;
            height: 100vh;
            width: 100vw;
            transition: transform 0.8s cubic-bezier(0.77, 0, 0.18, 1);
        }

        .slide {
            flex: 0 0 100vh;
            width: 100vw;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 2rem 3rem;
            position: relative;
            overflow: hidden;
        }

        .slide-content {
            max-width: 1200px;
            width: 100%;
            z-index: 10;
            opacity: 0;
            transform: translateY(50px) scale(0.95);
            transition: all 0.8s cubic-bezier(0.77, 0, 0.18, 1);
        }

        .slide.active .slide-content {
            opacity: 1;
            transform: translateY(0) scale(1);
        }

        .slide-title {
            font-size: 3.5rem;
            font-weight: 800;
            background: linear-gradient(135deg, #00ff88, #00ccff, #7b2ffc);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
            letter-spacing: -1px;
        }

        .slide-subtitle {
            font-size: 1.4rem;
            color: #8899bb;
            margin-bottom: 1.5rem;
            font-weight: 300;
            letter-spacing: 2px;
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
            font-size: 1.2rem;
            margin-bottom: 0.5rem;
        }

        .grid-2 {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 2.5rem;
            width: 100%;
        }

        .grid-3 {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 1.5rem;
            width: 100%;
        }

        .molecule-viewer {
            width: 100%;
            height: 400px;
            border-radius: 16px;
            background: rgba(0, 0, 0, 0.3);
            border: 1px solid rgba(255, 255, 255, 0.05);
            cursor: grab;
        }

        .molecule-viewer:active {
            cursor: grabbing;
        }

        .highlight {
            background: rgba(0, 255, 136, 0.05);
            border-left: 3px solid #00ff88;
            padding: 0.8rem 1.2rem;
            border-radius: 8px;
            color: #c8d6e5;
            margin: 1rem 0;
        }

        .highlight strong {
            color: #00ff88;
        }

        .nav-controls {
            position: fixed;
            bottom: 2rem;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            gap: 0.8rem;
            align-items: center;
            z-index: 100;
            background: rgba(6, 10, 20, 0.7);
            backdrop-filter: blur(20px);
            padding: 0.5rem 1.5rem;
            border-radius: 60px;
            border: 1px solid rgba(255, 255, 255, 0.05);
        }

        .nav-btn {
            background: transparent;
            border: none;
            color: #667799;
            font-size: 1.2rem;
            cursor: pointer;
            padding: 0.3rem 0.8rem;
            border-radius: 40px;
            transition: all 0.3s ease;
        }

        .nav-btn:hover {
            color: #00ff88;
            background: rgba(0, 255, 136, 0.08);
        }

        .nav-dots {
            display: flex;
            gap: 0.5rem;
            padding: 0 0.5rem;
        }

        .nav-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: #1f2a40;
            border: none;
            cursor: pointer;
            transition: all 0.4s ease;
        }

        .nav-dot.active {
            background: #00ff88;
            width: 24px;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0, 255, 136, 0.3);
        }

        .slide-counter {
            color: #445566;
            font-size: 0.75rem;
            min-width: 35px;
            text-align: center;
            font-weight: 300;
        }

        @media (max-width: 768px) {
            .slide {
                padding: 1.2rem;
            }
            .slide-title {
                font-size: 2.2rem;
            }
            .grid-2,
            .grid-3 {
                grid-template-columns: 1fr;
                gap: 1.2rem;
            }
            .molecule-viewer {
                height: 250px;
            }
            .nav-controls {
                padding: 0.3rem 1rem;
                bottom: 1rem;
            }
        }
    </style>
</head>
<body>

    <div class="slides-wrapper" id="slidesWrapper">

        <!-- ============================================================ -->
        <!-- SLIDE 1: TITLE -->
        <!-- ============================================================ -->
        <section class="slide active" data-index="0">
            <div class="slide-content" style="text-align:center;">
                <div style="font-size:4rem; margin-bottom:1rem;">🧬</div>
                <h1 class="slide-title">The Amide Bond</h1>
                <p class="slide-subtitle">The Unsung Hero of Modern Medicine</p>
                <p style="color:#667799; font-size:1.1rem;">Amide Formation in Organic Synthesis &amp; Drug Discovery</p>
                <p style="color:#334466; margin-top:2rem; font-size:0.9rem; letter-spacing:2px;">
                    <i class="fas fa-arrow-right"></i> Press <strong style="color:#00ff88;">→</strong> or click to explore
                </p>
            </div>
        </section>

        <!-- ============================================================ -->
        <!-- SLIDE 2: WHAT IS AMIDE FORMATION? -->
        <!-- ============================================================ -->
        <section class="slide" data-index="1">
            <div class="slide-content">
                <h1 class="slide-title">What is Amide Formation?</h1>
                <p class="slide-subtitle">The Chemical Bond That Connects Medicine</p>
                <div class="grid-2">
                    <div>
                        <div class="glass-card">
                            <h3>🔬 Simple Definition</h3>
                            <p>An <strong style="color:#00ff88;">amide</strong> is formed when a <strong style="color:#00ccff;">carboxylic acid</strong> reacts with an <strong style="color:#ff6b6b;">amine</strong>.</p>
                            <p style="margin-top:0.8rem; color:#8899bb; font-size:0.95rem;">
                                R-COOH + R'-NH₂ → R-CONH-R' + H₂O
                            </p>
                        </div>
                        <div class="highlight" style="margin-top:1rem;">
                            <strong>💡 Did You Know?</strong> Over <strong style="color:#00ff88;">25%</strong> of FDA-approved drugs contain an amide bond.
                        </div>
                    </div>
                    <div>
                        <div class="glass-card" style="text-align:center;">
                            <h3>🧬 Interactive Amide Structure</h3>
                            <p style="color:#8899bb; font-size:0.85rem; margin-bottom:0.8rem;">
                                🖱️ Drag to rotate · Scroll to zoom
                            </p>
                            <div id="amideViewer" class="molecule-viewer"></div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ============================================================ -->
        <!-- SLIDE 3: WHY AMIDES IN DRUGS? -->
        <!-- ============================================================ -->
        <section class="slide" data-index="2">
            <div class="slide-content">
                <h1 class="slide-title">Why Amides in Drugs?</h1>
                <p class="slide-subtitle">The "Smart" Reason Behind Their Popularity</p>
                <div class="grid-3">
                    <div class="glass-card">
                        <h3>✅ Stability</h3>
                        <p>Amide bonds are <strong style="color:#00ff88;">stable</strong> — they don't break easily in the body.</p>
                        <p style="color:#8899bb; font-size:0.9rem; margin-top:0.5rem;">Drugs <strong>last longer</strong> in the body.</p>
                    </div>
                    <div class="glass-card">
                        <h3>🧬 Bioavailability</h3>
                        <p>Amides can be designed to <strong style="color:#00ccff;">cross cell membranes</strong>.</p>
                        <p style="color:#8899bb; font-size:0.9rem; margin-top:0.5rem;">Drugs <strong>reach their targets</strong>.</p>
                    </div>
                    <div class="glass-card">
                        <h3>🔬 Versatility</h3>
                        <p>Amides can be <strong style="color:#ff6b6b;">tuned</strong> by changing the groups attached to them.</p>
                        <p style="color:#8899bb; font-size:0.9rem; margin-top:0.5rem;">Chemists can <strong>design better drugs</strong>.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- ============================================================ -->
        <!-- SLIDE 4: REAL DRUG EXAMPLES -->
        <!-- ============================================================ -->
        <section class="slide" data-index="3">
            <div class="slide-content">
                <h1 class="slide-title">Real Drug Examples</h1>
                <p class="slide-subtitle">Amide Bonds in Medicines You Know</p>
                <div class="grid-3">
                    <div class="glass-card" style="text-align:center;">
                        <h3>💊 Paracetamol</h3>
                        <div id="paracetamolViewer" class="molecule-viewer" style="height:200px;"></div>
                        <p style="color:#8899bb; font-size:0.85rem; margin-top:0.5rem;">Painkiller · Contains amide bond</p>
                    </div>
                    <div class="glass-card" style="text-align:center;">
                        <h3>🧪 Penicillin</h3>
                        <div id="penicillinViewer" class="molecule-viewer" style="height:200px;"></div>
                        <p style="color:#8899bb; font-size:0.85rem; margin-top:0.5rem;">Antibiotic · Contains amide bond</p>
                    </div>
                    <div class="glass-card" style="text-align:center;">
                        <h3>❤️ Atorvastatin</h3>
                        <div id="atorvastatinViewer" class="molecule-viewer" style="height:200px;"></div>
                        <p style="color:#8899bb; font-size:0.85rem; margin-top:0.5rem;">Cholesterol drug · Contains amide bond</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- ============================================================ -->
        <!-- SLIDE 5: MODERN APPLICATIONS -->
        <!-- ============================================================ -->
        <section class="slide" data-index="4">
            <div class="slide-content">
                <h1 class="slide-title">Modern Applications</h1>
                <p class="slide-subtitle">How Amide Formation Is Used in Drug Discovery Today</p>
                <div class="grid-2">
                    <div>
                        <div class="glass-card">
                            <h3>🔬 Peptide Synthesis</h3>
                            <p>Amide formation is used to <strong style="color:#00ff88;">connect amino acids</strong> into peptides.</p>
                            <p style="color:#8899bb; font-size:0.9rem; margin-top:0.5rem;">Peptides are <strong style="color:#00ccff;">the future of medicine</strong>.</p>
                        </div>
                        <div class="glass-card" style="margin-top:1rem;">
                            <h3>🧪 Drug Libraries</h3>
                            <p>Amide coupling creates <strong style="color:#ff6b6b;">thousands of drug candidates</strong> quickly.</p>
                        </div>
                    </div>
                    <div>
                        <div class="glass-card">
                            <h3>💊 Lead Optimization</h3>
                            <p>Amide formation is used to <strong style="color:#00ccff;">modify</strong> promising compounds.</p>
                            <p style="color:#8899bb; font-size:0.9rem; margin-top:0.5rem;">This is how <strong style="color:#00ff88;">drugs get improved</strong>.</p>
                        </div>
                        <div class="glass-card" style="margin-top:1rem;">
                            <h3>🧬 Targeted Therapies</h3>
                            <p>Amide bonds create <strong style="color:#ff6b6b;">targeted therapies</strong> that attack only cancer cells.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ============================================================ -->
        <!-- SLIDE 6: CONCLUSION -->
        <!-- ============================================================ -->
        <section class="slide" data-index="5">
            <div class="slide-content" style="text-align:center;">
                <h1 class="slide-title">Conclusion</h1>
                <p class="slide-subtitle">The Amide Bond — The Unsung Hero of Modern Medicine</p>
                <div style="max-width:700px; margin:0 auto;">
                    <div class="glass-card">
                        <h3>📌 Key Takeaways</h3>
                        <ul style="color:#c8d6e5; text-align:left; padding-left:1.2rem;">
                            <li>🧬 Found in <strong style="color:#00ff88;">>25% of all drugs</strong></li>
                            <li>💊 Used in <strong style="color:#00ccff;">drug discovery</strong> to create new medicines</li>
                            <li>🔬 The foundation of <strong style="color:#ff6b6b;">peptides and proteins</strong></li>
                            <li>🚀 The <strong style="color:#ffd93d;">future of medicine</strong></li>
                        </ul>
                    </div>
                    <div class="highlight" style="font-size:1.1rem; padding:1.2rem 1.5rem; text-align:center;">
                        <strong>🧪 The amide bond is not just a chemical bond —</strong><br>
                        <span style="color:#00ff88;">it's the connection between chemistry and medicine.</span>
                    </div>
                    <p style="margin-top:1.5rem; color:#667799;">🧬 Thank you for your attention · Questions?</p>
                </div>
            </div>
        </section>

    </div>

    <!-- ============================================================ -->
    <!-- NAVIGATION -->
    <!-- ============================================================ -->
    <div class="nav-controls">
        <button class="nav-btn" id="prevBtn"><i class="fas fa-chevron-left"></i></button>
        <div class="nav-dots" id="navDots"></div>
        <span class="slide-counter" id="slideCounter">1 / 6</span>
        <button class="nav-btn" id="nextBtn"><i class="fas fa-chevron-right"></i></button>
    </div>

    <!-- ============================================================ -->
    <!-- JAVASCRIPT -->
    <!-- ============================================================ -->
    <script>
        // ============================================================
        // SLIDE NAVIGATION
        // ============================================================
        const slides = document.querySelectorAll('.slide');
        const totalSlides = slides.length;
        let currentSlide = 0;
        const wrapper = document.getElementById('slidesWrapper');
        const dotsContainer = document.getElementById('navDots');
        const counter = document.getElementById('slideCounter');

        for (let i = 0; i < totalSlides; i++) {
            const dot = document.createElement('button');
            dot.className = 'nav-dot' + (i === 0 ? ' active' : '');
            dot.addEventListener('click', () => goToSlide(i));
            dotsContainer.appendChild(dot);
        }

        const dots = document.querySelectorAll('.nav-dot');

        function goToSlide(index) {
            if (index < 0) index = 0;
            if (index >= totalSlides) index = totalSlides - 1;
            currentSlide = index;
            wrapper.style.transform = 'translateY(-' + currentSlide * 100 + 'vh)';
            dots.forEach((d, i) => d.classList.toggle('active', i === currentSlide));
            counter.textContent = (currentSlide + 1) + ' / ' + totalSlides;
            slides.forEach((s, i) => s.classList.toggle('active', i === currentSlide));
            // Re-render molecules after slide change (fixes rendering issues)
            setTimeout(renderMolecules, 100);
        }

        document.getElementById('nextBtn').addEventListener('click', () => goToSlide(currentSlide + 1));
        document.getElementById('prevBtn').addEventListener('click', () => goToSlide(currentSlide - 1));

        document.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowRight' || e.key === 'ArrowDown' || e.key === ' ') {
                e.preventDefault();
                goToSlide(currentSlide + 1);
            } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
                e.preventDefault();
                goToSlide(currentSlide - 1);
            }
        });

        // ============================================================
        // 3D MOLECULE VIEWERS
        // ============================================================
        function renderMolecules() {
            // Amide structure
            const amideContainer = document.getElementById('amideViewer');
            if (amideContainer) {
                const viewer = $3Dmol.createViewer(amideContainer, {
                    backgroundColor: '0x0a0a1a'
                });
                viewer.addModel("COC(=O)Nc1ccc(cc1)O", "smiles");
                viewer.setStyle({}, { stick: {}, sphere: { scale: 0.3 } });
                viewer.zoomTo();
                viewer.rotate(90);
                viewer.render();
            }

            // Paracetamol
            const paraContainer = document.getElementById('paracetamolViewer');
            if (paraContainer) {
                const viewer = $3Dmol.createViewer(paraContainer, {
                    backgroundColor: '0x0a0a1a'
                });
                viewer.addModel("CC(=O)Nc1ccc(cc1)O", "smiles");
                viewer.setStyle({}, { stick: {}, sphere: { scale: 0.3 } });
                viewer.zoomTo();
                viewer.render();
            }

            // Penicillin
            const penContainer = document.getElementById('penicillinViewer');
            if (penContainer) {
                const viewer = $3Dmol.createViewer(penContainer, {
                    backgroundColor: '0x0a0a1a'
                });
                viewer.addModel("CC1(C)SC2C(NC(=O)Cc3ccccc3)C(=O)N2C1C(=O)O", "smiles");
                viewer.setStyle({}, { stick: {}, sphere: { scale: 0.3 } });
                viewer.zoomTo();
                viewer.render();
            }

            // Atorvastatin
            const atorContainer = document.getElementById('atorvastatinViewer');
            if (atorContainer) {
                const viewer = $3Dmol.createViewer(atorContainer, {
                    backgroundColor: '0x0a0a1a'
                });
                viewer.addModel("CC(C)c1c(C(=O)Nc2ccc(cc2)F)c(Cc3ccccc3)c(C(=O)O)c(n1)C(C)C", "smiles");
                viewer.setStyle({}, { stick: {}, sphere: { scale: 0.3 } });
                viewer.zoomTo();
                viewer.render();
            }
        }

        // Initial render
        setTimeout(renderMolecules, 500);

        // Re-render on window resize
        window.addEventListener('resize', renderMolecules);
    </script>

    <!-- Font Awesome (for icons) -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" />

</body>
</html>
