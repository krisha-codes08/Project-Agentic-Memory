import streamlit as st
import time

# =====================================================================
# 1. PREMIUM HIGH-CONTRAST DARK THEME CONFIGURATION
# =====================================================================
st.set_page_config(page_title="Pathfinder Pro Engine", page_icon="⚡", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #c9d1d9; }
    
    /* FIXING THE HEADING: High-contrast Crisp White and Vivid Green */
    
    /* Paste these right inside your style brackets at the top */
.premium-header {
    text-align: center;
    color: #ffffff !important;   /* Force clean, high-contrast bright white text */
    font-size: 2.5rem;
    font-weight: 800;
    margin-bottom: 0px;
    font-family: -apple-system, BlinkMacSystemFont, sans-serif;
}
.premium-subheader {
    text-align: center;
    color: #2ea043 !important;   /* High-contrast vivid green that pops on dark backgrounds */
    font-size: 1.1rem;
    font-weight: 600;
    margin-bottom: 2rem;
    font-family: -apple-system, BlinkMacSystemFont, sans-serif;
}
    
    .stButton>button {
        background: linear-gradient(135deg, #238636 0%, #2ea043 100%);
        color: white; border: none; border-radius: 6px; padding: 0.6rem 1.2rem;
        font-weight: 600; width: 100%; transition: all 0.2s ease;
    }
    .stButton>button:hover { transform: translateY(-1px); box-shadow: 0 4px 12px rgba(46,160,67,0.3); }
    .metric-card {
        background-color: #161b22; border: 1px solid #30363d; border-radius: 8px;
        padding: 1.5rem; margin-bottom: 1rem; box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .badge-stream {
        background-color: #1f2d3d; color: #58a6ff; border: 1px solid #1f426e;
        border-radius: 6px; padding: 0.4rem 0.8rem; font-weight: 600; font-size: 1.1rem; display: inline-block;
    }
    .badge-sub {
        background-color: #272130; color: #bc8cff; border: 1px solid #463461;
        border-radius: 6px; padding: 0.4rem 0.8rem; font-weight: 600; font-size: 1.1rem; display: inline-block;
    }
    .step-card {
        background-color: #21262d; border-left: 5px solid #58a6ff; border-radius: 4px 8px 8px 4px;
        padding: 1rem; margin-bottom: 0.8rem; border-top: 1px solid #30363d; border-right: 1px solid #30363d; border-bottom: 1px solid #30363d;
        color: #ffffff !important;
    }
    .step-card-alert {
        background-color: #2a1f1f; border-left: 5px solid #f85149; border-radius: 4px 8px 8px 4px;
        padding: 1rem; margin-bottom: 0.8rem; border-top: 1px solid #492323; border-right: 1px solid #492323; border-bottom: 1px solid #492323;
        color: #ffffff !important
    }
    .step-card-success {
        background-color: #1f2a22; border-left: 5px solid #3fb950; border-radius: 4px 8px 8px 4px;
        padding: 1rem; margin-bottom: 0.8rem; border-top: 1px solid #23492d; border-right: 1px solid #23492d; border-bottom: 1px solid #23492d;
        color: #ffffff !important;
    }
    h1, h2, h3 { color: #f0f6fc !important; font-family: -apple-system, BlinkMacSystemFont, sans-serif; }
    </style>
""", unsafe_allow_html=True)

# Render the clean, beautiful high-contrast header strings
# Replace your old title/caption lines with these two clean containers:
st.markdown("<div class='premium-header'>⚡ Pathfinder Pro: AI Career Optimization Engine</div>", unsafe_allow_html=True)
st.markdown("<div class='premium-subheader'>Track 1 Architecture: Multi-Turn Conversation Routing & MongoDB Thread Context Vaulting</div>", unsafe_allow_html=True)
# =====================================================================
# 2. STATE INITIALIZATION & DATABASE CHECKPOINT DICTIONARY
# =====================================================================
if "mongodb_vault" not in st.session_state:
    st.session_state.mongodb_vault = {
        "student_krish_101": {
            "target_track": "Core Software Engineering",
            "detected_sub": "Enterprise Backend Systems",
            "academic_hurdles": ["Struggling with Data Structures"],
            "career_roadmap": [
                "⚠️ CAUTION DIRECTIVE: Active memory flags confirm a core data structure hurdle.",
                "⏳ REMEDIATION TARGET (Semester 1): Halting standard modules. Execute 20 targeted array tracking routines.",
                "🎯 PLACEMENT PIPELINE: Route portfolio components toward Core Software Engineering roles."
            ],
            "raw_input": "I want to focus on backend development architecture.",
            "verification_status": "Vault Checkpoint Sync Active ✅"
        }
    }

if "current_career" not in st.session_state: st.session_state.current_career = "Core Software Engineering"
if "detected_sub" not in st.session_state: st.session_state.detected_sub = "Enterprise Backend Systems"
if "current_hurdles" not in st.session_state: st.session_state.current_hurdles = ["Struggling with Data Structures"]
if "current_roadmap" not in st.session_state:
    st.session_state.current_roadmap = [
        "⚠️ CAUTION DIRECTIVE: Active memory flags confirm a core data structure hurdle.",
        "⏳ REMEDIATION TARGET (Semester 1): Halting standard modules. Execute 20 targeted array tracking routines.",
        "🎯 PLACEMENT PIPELINE: Route portfolio components toward Core Software Engineering roles."
    ]
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [{"role": "assistant", "content": "Welcome to Pathfinder Pro. Input your specific engineering track goals or academic performance metrics below to observe core graph network mutations."}]
if "raw_chat_input" not in st.session_state: st.session_state.raw_chat_input = ""

# =====================================================================
# 3. LAYOUT DESIGN: LEFT CONFIGURATION FORM
# =====================================================================
col_left, col_right = st.columns(2)

with col_left:
    st.markdown("<div class='metric-card'><h3>📝 Active Context Profiles</h3>", unsafe_allow_html=True)
    
    career_options = ["Core Software Engineering", "AI Research & Data Science", "UI/UX Visual Design", "Cloud Systems & DevOps"]
    default_idx = career_options.index(st.session_state.current_career) if st.session_state.current_career in career_options else 0
    
    st.session_state.current_career = st.selectbox("Target Placement Pipeline Stream:", options=career_options, index=default_idx)
    current_semester = st.slider("Active Academic Semester:", min_value=1, max_value=8, value=1)
    
    technical_focus = st.multiselect("Core Strategic Domain Strengths:", 
                                     options=["Python Core", "Figma Engineering", "SQL Vector Databases", "Full-Stack Web Architectures", "Cloud Microservices"],
                                     default=["Python Core"])
    
    st.markdown("<p style='font-weight: 600; margin-top: 1rem; margin-bottom: 5px;'>Active Academic Impediments / Hurdles:</p>", unsafe_allow_html=True)
    h1 = st.checkbox("Data Structures & Algorithms", value=("Struggling with Data Structures" in st.session_state.current_hurdles))
    h2 = st.checkbox("Advanced Systems Architecture", value=("Struggling with Systems Architecture" in st.session_state.current_hurdles))
    
    updated_hurdles = []
    if h1: updated_hurdles.append("Struggling with Data Structures")
    if h2: updated_hurdles.append("Struggling with Systems Architecture")
    st.session_state.current_hurdles = updated_hurdles

    if st.button("🧠 Execute Graph Evaluation Pipeline"):
        with st.spinner("🤖 Recalculating workflow parameters..."):
            time.sleep(0.4)
            if st.session_state.current_career == "Core Software Engineering":
                if "Struggling with Data Structures" in st.session_state.current_hurdles:
                    st.session_state.current_roadmap = [
                        "⚠️ CAUTION DIRECTIVE: Active memory flags confirm a core data structure hurdle.",
                        f"⏳ REMEDIATION TARGET (Semester {current_semester}): Halting standard modules. Execute 20 targeted array tracking routines.",
                        f"🎯 PLACEMENT PIPELINE: Route portfolio components toward baseline {st.session_state.current_career} roles."
                    ]
                else:
                    st.session_state.current_roadmap = [
                        f"🚀 REPOSITORY ACCELERATION (Semester {current_semester}): Bootstrap a modern full-stack web application blueprint.",
                        "⏳ SCHEMATIC DESIGN: Optimize storage queries across regional database partitions.",
                        f"🎯 PLACEMENT PIPELINE: Target production engineering roles inside the {st.session_state.current_career} stream."
                    ]
            st.session_state.mongodb_vault["student_krish_101"] = {
                "target_track": st.session_state.current_career, "detected_sub": st.session_state.detected_sub,
                "academic_hurdles": st.session_state.current_hurdles, "career_roadmap": st.session_state.current_roadmap,
                "raw_input": st.session_state.raw_chat_input, "verification_status": "Manual Form Checkpoint Committed ✅"
            }
            st.success("State maps successfully compiled.")
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
    # =====================================================================
# 4. LAYOUT DESIGN: RIGHT DASHBOARD MONITOR
# =====================================================================
with col_right:
    st.markdown("<div class='metric-card'><h3>📊 Dynamic Evaluation Monitor</h3>", unsafe_allow_html=True)
    
    st.markdown("<p style='color: #8b949e; margin-bottom: 5px; font-size: 0.9rem;'>Active Classification Stream:</p>", unsafe_allow_html=True)
    st.markdown(f"<div class='badge-stream'>{st.session_state.current_career}</div>", unsafe_allow_html=True)
    
    st.markdown("<p style='color: #8b949e; margin-top: 1rem; margin-bottom: 5px; font-size: 0.9rem;'>Extracted Specialization Subcategory:</p>", unsafe_allow_html=True)
    st.markdown(f"<div class='badge-sub'>{st.session_state.detected_sub}</div>", unsafe_allow_html=True)
    
    st.markdown("<p style='color: #8b949e; font-size: 0.9rem; margin-top: 1.5rem; margin-bottom: 10px;'>Adaptive Strategy Roadmap Timeline:</p>", unsafe_allow_html=True)
    
    for step in st.session_state.current_roadmap:
        if "⚠️" in step:
            st.markdown(f"<div class='step-card-alert'>{step}</div>", unsafe_allow_html=True)
        elif any(m in step for m in ["🚀", "🎨", "📊", "☁️"]):
            st.markdown(f"<div class='step-card-success'>{step}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='step-card'>{step}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# =====================================================================
# 5. BOTTOM PORTAL: REAL-TIME CONVERSATIONAL INTERACTIVE LOGIC
# =====================================================================
st.markdown("<div class='metric-card'><h3>💬 Real-Time Token Extraction Terminal</h3>", unsafe_allow_html=True)
chat_left, chat_right = st.columns(2)

with chat_left:
    chat_container = st.container(height=300)
    with chat_container:
        for m in st.session_state.chat_history:
            with st.chat_message(m["role"]): st.write(m["content"])
            
    if chat_msg := st.chat_input("Input custom parameters (e.g., 'Switch to deep learning tracks for Computer Vision')..."):
        with chat_container:
            with st.chat_message("user"): st.write(chat_msg)
        st.session_state.chat_history.append({"role": "user", "content": chat_msg})
        st.session_state.raw_chat_input = chat_msg
        
        text_lower = chat_msg.lower()
        if any(w in text_lower for w in ["ai", "data", "ml", "machine", "learning", "research", "nlp", "vision", "deep", "llm"]):
            st.session_state.current_career = "AI Research & Data Science"
            sub = "General ML Engineering"
            if any(x in text_lower for x in ["nlp", "text", "llm"]): sub = "Natural Language Processing (NLP)"
            elif any(x in text_lower for x in ["vision", "image", "cnn"]): sub = "Computer Vision Deep Learning"
            st.session_state.detected_sub = sub
            ai_reply = f"📝 **Extraction Triggered:** Allocated to **{st.session_state.current_career}** (Sub-track: **{sub}**)."
        elif any(w in text_lower for w in ["ux", "ui", "design", "figma", "interface"]):
            st.session_state.current_career = "UI/UX Visual Design"
            st.session_state.detected_sub = "UI/UX Interaction Designer"
            ai_reply = f"📝 **Extraction Triggered:** Allocated to **{st.session_state.current_career}**."
        elif any(w in text_lower for w in ["cloud", "devops", "aws", "docker", "security", "cyber"]):
            st.session_state.current_career = "Cloud Systems & DevOps"
            st.session_state.detected_sub = "SecOps Infrastructure Security"
            ai_reply = f"📝 **Extraction Triggered:** Allocated to **{st.session_state.current_career}**."
        else:
            st.session_state.current_career = "Core Software Engineering"
            sub = "General Systems Architecture"
            if "backend" in text_lower: sub = "Enterprise Backend Systems"
            elif "frontend" in text_lower: sub = "Full-Stack Web Architectures"
            st.session_state.detected_sub = sub
            ai_reply = f"📝 **Extraction Triggered:** Fixed on **{st.session_state.current_career}** (Sub-track: **{sub}**)."

        if any(w in text_lower for w in ["fail", "struggle", "stuck", "hard", "worry", "structures"]):
            if "Struggling with Data Structures" not in st.session_state.current_hurdles:
                st.session_state.current_hurdles.append("Struggling with Data Structures")
            ai_reply += " Active warning flags appended to the data profile layer."

        if st.session_state.current_career == "AI Research & Data Science":
            st.session_state.current_roadmap = [
                f"📊 VECTOR DESIGN (Semester {current_semester}): Process structural arrays matching: {st.session_state.detected_sub}.",
                "📊 ALGORITHM ASSEMBLY: Code predictive neural weight sheets from scratch in Python.",
                f"🎯 PIPELINE EXECUTION: Push applications directly to active {st.session_state.current_career} portals."
            ]
        elif st.session_state.current_career == "UI/UX Visual Design":
            st.session_state.current_roadmap = [
                f"🎨 FIGMA CANVAS (Semester {current_semester}): Arrange wireframe assets tracking: {st.session_state.detected_sub}.",
                "🎨 PRODUCTION HANDOFF: Render visual interactive layouts cleanly to Behance portfolios.",
                f"🎯 PIPELINE EXECUTION: Push applications directly to active {st.session_state.current_career} portals."
            ]
        else:
            if "Struggling with Data Structures" in st.session_state.current_hurdles:
                st.session_state.current_roadmap = [
                    "⚠️ CAUTION DIRECTIVE: Active memory flags confirm a core data structure hurdle.",
                    f"⏳ REMEDIATION TARGET (Semester {current_semester}): Halting advanced modules. Complete 20 targeted array tracking routines.",
                    f"🎯 PLACEMENT FOCUS: Route portfolio components toward baseline Core Software Engineering roles."
                ]
            else:
                st.session_state.current_roadmap = [
                    f"🚀 REPOSITORY ACCELERATION (Semester {current_semester}): Bootstrap a modern codebase matching {st.session_state.detected_sub}.",
                    "⏳ SCHEMATIC DESIGN: Optimize backend asset loading operations across server structures.",
                    f"🎯 PLACEMENT FOCUS: Complete standard placement applications."
                ]

        # FIXED VARIABLE CONFLICT BY MAPPING TO THE CORRESPONDING STRING 'student_id' TARGET VALUE DEFINED BELOW
        st.session_state.mongodb_vault["student_krish_101"] = {
            "target_track": st.session_state.current_career, "detected_sub": st.session_state.detected_sub,
            "academic_hurdles": st.session_state.current_hurdles, "career_roadmap": st.session_state.current_roadmap,
            "raw_input": st.session_state.raw_chat_input, "verification_status": "Conversational Thread Sync Complete ✅"
        }
        with chat_container:
            with st.chat_message("assistant"): st.write(ai_reply)
        st.session_state.chat_history.append({"role": "assistant", "content": ai_reply})
        st.rerun()

# --- BACKEND VAULT RE-HYDRATION CONTROLS PANEL ---
with chat_right:
    st.markdown("<div style='background-color: #161b22; border: 1px solid #30363d; padding: 1rem; border-radius: 6px; height: 100%;'>", unsafe_allow_html=True)
    st.write("🛰️ **Vault Server Links**")
    
    # RENAME ASSIGNED TARGET TOKEN VALUE TO SEPARATELY LINK VARIABLE SCHEMAS TO AVOID ENFORCEMENT FAILURES
    st.markdown(f"<p style='color: #8b949e; font-size: 0.8rem; margin-bottom: 10px;'>Active Thread ID: <code style='color: #58a6ff;'>student_krish_101</code></p>", unsafe_allow_html=True)
    
    if st.button("🔄 Sync Checkpoint"):
        if "student_krish_101" in st.session_state.mongodb_vault:
            c = st.session_state.mongodb_vault["student_krish_101"]
            st.session_state.current_career = c["target_track"]
            st.session_state.detected_sub = c["detected_sub"]
            st.session_state.current_hurdles = c["academic_hurdles"]
            st.session_state.current_roadmap = c["career_roadmap"]
            st.session_state.raw_chat_input = c["raw_input"]
            st.toast("Profile state fully re-hydrated!")
            st.rerun()
            
    if st.button("🗑️ Flash Display"):
        st.session_state.chat_history = [{"role": "assistant", "content": "Chat terminal cleared. Long-term memory snapshots remain vaulted in the backend database tracker."}]
        st.rerun()
        
    v_status = st.session_state.mongodb_vault.get("student_krish_101", {}).get("verification_status", "Database Listening...")
    st.caption(f"**Ledger Transaction:** {v_status}")
    st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)