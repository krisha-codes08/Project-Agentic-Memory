import streamlit as st
import time

# =====================================================================
# 1. WEB UI STYLING & CONFIGURATION
# =====================================================================
st.set_page_config(page_title="Pathfinder Chat Agent", page_icon="logo.jpg.jpeg", layout="wide")
# Create two columns: a small one for the 'P' logo and a larger one for the text
logo_col, text_col = st.columns([1, 12], vertical_alignment="center")

with logo_col:
    st.image("logo.jpg.jpeg", width=65)

with text_col:
    st.markdown("<h1 style='margin: 0; padding: 0;'>Pathfinder: Conversational AI Career & Academic Agent</h1>", unsafe_allow_html=True)
# =====================================================================
# 2. THE PERSISTENT MONGODB DATABASE VAULT SIMULATION
# =====================================================================
if "mongodb_vault" not in st.session_state:
    st.session_state.mongodb_vault = {
        "student_krish_101": {
            "target_track": "Core Software Engineering",
            "detected_sub": "General Systems Architecture",
            "academic_hurdles": ["Struggling with Data Structures"],
            "career_roadmap": [
                "⚠️ CRITICAL ADAPTATION: Stored memory flags confirm an active data structure hurdle.",
                "⏳ REMEDIATION PLAN (Sem 1): Skip advanced modules; execute 20 targeted loop operations.",
                "🎯 PLACEMENT FOCUS: Complete baseline Core Software Engineering applications."
            ],
            "verification_status": "Active Profile Snapshotted ✅"
        }
    }

# Initialize live conversation message buffers
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {
            "role": "assistant",
            "content": "Hello! I am Pathfinder, your autonomous career architect. Tell me about your dream tech goals, what skills you have, or any academic struggles you are facing right now! Try typing things like 'I want to do backend web dev', 'I want to build deep learning models for computer vision', or 'I love cybersecurity' and watch the entire architecture adapt."
        }
    ]

# Initialize runtime tracking attributes if they do not exist
if "current_career" not in st.session_state:
    st.session_state.current_career = "Core Software Engineering"
if "detected_sub" not in st.session_state:
    st.session_state.detected_sub = "General Systems Architecture"
if "current_hurdles" not in st.session_state:
    st.session_state.current_hurdles = []
if "current_roadmap" not in st.session_state:
    st.session_state.current_roadmap = [
        "🚀 REPOSITORY BOOTSTRAP (Sem 1): Launch an open-source full-stack application portfolio.",
        "⏳ PERFORMANCE TUNING: Optimize asset variables matching standard software tracks.",
        "🎯 PLACEMENT FOCUS: Complete baseline Core Software Engineering applications."
    ]
if "raw_chat_input" not in st.session_state:
    st.session_state.raw_chat_input = ""

# =====================================================================
# 3. INTERACTIVE SIDEBAR MANAGEMENT PANEL (MongoDB Sync Utilities)
# =====================================================================
st.sidebar.header("🗄️ MongoDB Agentic Memory Vault")
st.sidebar.subheader("Identification Parameters")
student_id = st.sidebar.text_input("Active Student Thread ID", value="student_krish_101")

# Sync Button: Pulls memory from the vault to show history works across separate session reloads
if st.sidebar.button("🔄 Sync & Hydrate Memory Profile"):
    if student_id in st.session_state.mongodb_vault:
        checkpoint = st.session_state.mongodb_vault[student_id]
        st.session_state.current_career = checkpoint.get("target_track", "Core Software Engineering")
        st.session_state.detected_sub = checkpoint.get("detected_sub", "General Systems Architecture")
        st.session_state.current_hurdles = checkpoint.get("academic_hurdles", [])
        st.session_state.current_roadmap = checkpoint.get("career_roadmap", ["🚀 Baseline Loaded"])
        st.session_state.raw_chat_input = checkpoint.get("raw_input", "")
        st.sidebar.success("✅ State successfully re-hydrated from MongoDB checkpoint!")
        st.rerun()
    else:
        st.sidebar.info("ℹ️ New signature token. Initializing clean baseline profile.")

if st.sidebar.button("🗑️ Clear Screen (Simulate Page Reload)"):
    st.session_state.chat_history = [
        {
            "role": "assistant",
            "content": "Screen cleared. The active conversation log is wiped. However, your historical profile documents are still archived safely in the MongoDB vault! Click 'Sync & Hydrate' in the sidebar to pull them back instantly."
        }
    ]
    st.rerun()

st.sidebar.markdown("---")
st.sidebar.subheader("🧠 Long-Term Memory Vault Inspector")
st.sidebar.info(f"**Saved Raw Chat Input:** {st.session_state.raw_chat_input}")
st.sidebar.info(f"**Target Stream Track:** {st.session_state.current_career}")
st.sidebar.success(f"**Extracted Subcategory:** {st.session_state.detected_sub}")
st.sidebar.warning(f"**Logged Academic Hurdles:** {st.session_state.current_hurdles}")
# =====================================================================
# 4. DUAL PANE CONFIGURATION LAYOUT
# =====================================================================
col_left, col_right = st.columns(2)

# --- LEFT PANEL: DETAILED STUDENT CONTEXT PROFILE SETUP ---
with col_left:
    st.subheader("📝 Update Student Context Profile")
    
    # Comprehensive selectbox replacement for the target field
    career_options = [
        "Core Software Engineering", 
        "AI Research & Data Science", 
        "UI/UX Visual Design",
        "Cloud Systems & DevOps"
    ]
    
    default_idx = career_options.index(st.session_state.current_career) if st.session_state.current_career in career_options else 0
    selected_career = st.selectbox(
        "Select your targeted career or internship pipeline:",
        options=career_options,
        index=default_idx
    )
    st.session_state.current_career = selected_career
    
    # Deep structural data gathering metrics
    current_semester = st.slider("Current Academic Semester:", min_value=1, max_value=8, value=1)
    
    technical_focus = st.multiselect(
        "Primary Technical Focus / Strengths:",
        options=["Python Systems", "Figma Design", "SQL Databases", "Web Development", "Cloud Frameworks"],
        default=["Python Systems"]
    )
    
    st.markdown("---")
    st.markdown("**Select any active academic hurdles or subjects causing trouble:**")
    h1 = st.checkbox("Data Structures & Algorithms", value=("Struggling with Data Structures" in st.session_state.current_hurdles))
    h2 = st.checkbox("Advanced Systems Architecture", value=("Struggling with Systems Architecture" in st.session_state.current_hurdles))
    
    updated_hurdles = []
    if h1: updated_hurdles.append("Struggling with Data Structures")
    if h2: updated_hurdles.append("Struggling with Systems Architecture")
    st.session_state.current_hurdles = updated_hurdles

    # The Process Action Button for Form Updates
    if st.button("🧠 Process Agent Logic & Update Memory"):
        with st.spinner("🤖 Agent workflow node evaluating profile matrices..."):
            time.sleep(0.5)
            
            # ADAPTIVE ROADMAP GENERATION ENGINE BASED ON CONFIGURATIONS
            if st.session_state.current_career == "UI/UX Visual Design":
                st.session_state.current_roadmap = [
                    f"🎨 FIGMA CONTRACT (Sem {current_semester}): Construct 3 high-fidelity application layouts.",
                    f"🎨 PORTFOLIO EXPANSION: Publish prototypes matching sub-track: {st.session_state.detected_sub}",
                    f"🎯 PLACEMENT FOCUS: Complete core {st.session_state.current_career} applications."
                ]
            elif st.session_state.current_career == "AI Research & Data Science":
                st.session_state.current_roadmap = [
                    f"📊 DATA MODELING (Sem {current_semester}): Map analytical vectors using {', '.join(technical_focus)}.",
                    f"📊 ML PIPELINE: Build predictive models matching sub-track: {st.session_state.detected_sub}",
                    f"🎯 PLACEMENT FOCUS: Complete core {st.session_state.current_career} applications."
                ]
            elif st.session_state.current_career == "Cloud Systems & DevOps":
                st.session_state.current_roadmap = [
                    f"☁️ INFRASTRUCTURE (Sem {current_semester}): Spin up cloud microservices for sub-track: {st.session_state.detected_sub}",
                    "☁️ AUTOMATION PIPELINES: Configure strict deployment runner tasks.",
                    f"🎯 PLACEMENT FOCUS: Complete core {st.session_state.current_career} applications."
                ]
            else: # Software Engineering Track
                if "Struggling with Data Structures" in st.session_state.current_hurdles:
                    st.session_state.current_roadmap = [
                        "⚠️ CRITICAL ADAPTATION: Stored memory flags confirm an active data structure hurdle.",
                        f"⏳ REMEDIATION PLAN (Sem {current_semester}): Skip advanced modules; execute 20 targeted loop operations.",
                        f"🎯 PLACEMENT FOCUS: Complete baseline {st.session_state.current_career} applications."
                    ]
                else:
                    st.session_state.current_roadmap = [
                        f"🚀 REPOSITORY BOOTSTRAP (Sem {current_semester}): Launch an open-source full-stack application portfolio.",
                        f"⏳ PERFORMANCE TUNING: Optimize asset variables matching sub-track: {st.session_state.detected_sub}",
                        f"🎯 PLACEMENT FOCUS: Complete baseline {st.session_state.current_career} applications."
                    ]
                
            # Commit configurations directly back to database variables
            st.session_state.mongodb_vault[student_id] = {
                "target_track": st.session_state.current_career,
                "detected_sub": st.session_state.detected_sub,
                "academic_hurdles": st.session_state.current_hurdles,
                "career_roadmap": st.session_state.current_roadmap,
                "raw_input": st.session_state.raw_chat_input,
                "verification_status": "Form Checkpoint Saved ✅"
            }
            st.success("🤖 Agent evaluation complete! State data successfully persisted to MongoDB vault.")
            st.rerun()

# --- RIGHT PANEL: DIGITAL ROADMAP AND STREAM LABELS ---
with col_right:
    st.subheader("📊 Dynamic Career Pathfinder Timeline")
    # Replace the old st.metric layout for Current Route Stream with this:
    st.markdown("### 🗺️ Current Route Stream")
    st.markdown(
        f"""
        <div style="background-color: #f0f2f6; padding: 12px 18px; border-radius: 8px; border-left: 5px solid #ff4b4b; margin-bottom: 15px;">
            <span style="font-size: 18px; font-weight: 600; color: #1f2937;">
                {st.session_state.current_career}
            </span>
        </div>
        """, 
        unsafe_allow_html=True
    )

    # Replace the old st.metric layout for Extracted Subcategory with this:
    st.markdown("### 🔬 Extracted Subcategory")
    st.markdown(
        f"""
        <div style="background-color: #f0f2f6; padding: 12px 18px; border-radius: 8px; border-left: 5px solid #00a0a0; margin-bottom: 15px;">
            <span style="font-size: 18px; font-weight: 600; color: #1f2937;">
                {st.session_state.detected_sub}
            </span>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    st.write("This timeline shifts its checkpoints dynamically based on the AI's long-term memory records:")
    for step in st.session_state.current_roadmap:
        if "⚠️" in step: st.error(step)
        elif any(marker in step for marker in ["🚀", "🎨", "📊", "☁️"]): st.success(step)
        else: st.info(step)
        # =====================================================================
# 5. BOTTOM INTERACTIVE CONVERSATIONAL PORTAL (Live Chat Component)
# =====================================================================
st.markdown("---")
st.subheader("💬 Interactive Agent Conversation Portal")
st.write("Communicate naturally with Pathfinder. The system actively extracts memory parameters from your sentences to update the database layout configurations above.")

chat_frame = st.container(height=350)
with chat_frame:
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.write(message["content"])

if chat_input_msg := st.chat_input("Type your status update or career shifts here..."):
    
    with chat_frame:
        with st.chat_message("user"):
            st.write(chat_input_msg)
    st.session_state.chat_history.append({"role": "user", "content": chat_input_msg})
    st.session_state.raw_chat_input = chat_input_msg
    
    # ADVANCED SEMANTIC EXTRACTION MATRIX (Extracting Streams & Subcategories dynamically)
    with st.spinner("🤖 Agent analyzing conversation text..."):
        time.sleep(0.5)
        text_lower = chat_input_msg.lower()
        
        # Track 1: Software Engineering Subcategories
        if any(w in text_lower for w in ["software", "dev", "code", "engineer", "backend", "frontend", "fullstack", "web"]):
            st.session_state.current_career = "Core Software Engineering"
            sub_type = "General Systems Architecture"
            if "backend" in text_lower: sub_type = "Enterprise Backend Architect"
            elif any(x in text_lower for x in ["frontend", "web"]): sub_type = "Full-Stack Web Architect"
            st.session_state.detected_sub = sub_type
            ai_reply = f"📝 **Memory Extraction Matrix:** Routed to **{st.session_state.current_career}** ➔ Subcategory: **[{sub_type}]**. Appending tailored software repositories to your profile view."

        # Track 2: AI Research & Data Science Subcategories
        elif any(w in text_lower for w in ["ai", "data", "ml", "machine", "learning", "research", "nlp", "vision", "deep", "llm"]):
            st.session_state.current_career = "AI Research & Data Science"
            sub_type = "General AI Architecture"
            if any(x in text_lower for x in ["nlp", "text", "llm"]): sub_type = "Natural Language Processing (NLP)"
            elif any(x in text_lower for x in ["vision", "image", "cnn"]): sub_type = "Computer Vision Deep Learning"
            elif "science" in text_lower: sub_type = "Big Data Analytics & Prediction"
            st.session_state.detected_sub = sub_type
            ai_reply = f"📝 **Memory Extraction Matrix:** Routed to **{st.session_state.current_career}** ➔ Subcategory: **[{sub_type}]**. Aligning computational asset roadmaps."

        # Track 3: UI/UX Visual Design Subcategories
        elif any(w in text_lower for w in ["ux", "ui", "design", "figma", "interface", "graphics", "product"]):
            st.session_state.current_career = "UI/UX Visual Design"
            sub_type = "General Product Design"
            if "research" in text_lower: sub_type = "UX Cognitive Researcher"
            elif any(x in text_lower for x in ["interface", "visual", "graphics"]): sub_type = "UI Interaction Designer"
            st.session_state.detected_sub = sub_type
            ai_reply = f"📝 **Memory Extraction Matrix:** Routed to **{st.session_state.current_career}** ➔ Subcategory: **[{sub_type}]**. Setting Figma file structure parameters."

        # Track 4: Cloud Systems & DevOps Subcategories
        elif any(w in text_lower for w in ["cloud", "devops", "systems", "server", "aws", "docker", "cyber", "security", "hack"]):
            st.session_state.current_career = "Cloud Systems & DevOps"
            sub_type = "General Cloud Infrastructure"
            if any(x in text_lower for x in ["cyber", "security", "hack"]): sub_type = "SecOps / Cybersecurity Threat Defense"
            elif "docker" in text_lower or "cicd" in text_lower: sub_type = "Automation & Deployment Pipeline Eng."
            st.session_state.detected_sub = sub_type
            ai_reply = f"📝 **Memory Extraction Matrix:** Routed to **{st.session_state.current_career}** ➔ Subcategory: **[{sub_type}]**. Provisioning isolated cloud running instances."
            
        else:
            ai_reply = "I have logged those notes. Try typing a specific sub-field like 'backend development,' 'NLP models,' or 'cybersecurity' to watch the pipeline accurately classify your sub-track!"

        # Academic Hurdle Extraction Check
        if any(w in text_lower for w in ["fail", "struggle", "stuck", "hard", "worry", "structures", "architecture"]):
            if "Data Structures" in text_lower or "structures" in text_lower:
                if "Struggling with Data Structures" not in st.session_state.current_hurdles:
                    st.session_state.current_hurdles.append("Struggling with Data Structures")
                    ai_reply += " Additionally, I extracted a performance challenge. The Data Structures check-box indicator has been flagged below."
            if "architecture" in text_lower or "systems" in text_lower:
                if "Struggling with Systems Architecture" not in st.session_state.current_hurdles:
                    st.session_state.current_hurdles.append("Struggling with Systems Architecture")
                    ai_reply += " Additionally, I extracted a systems architecture challenge. The Systems check-box indicator has been flagged below."

        # Difficult Case Requirement: Privacy Purge Protocol Execution
        if "purge" in text_lower or "delete data" in text_lower:
            st.session_state.current_hurdles = []
            st.session_state.current_career = "Core Software Engineering"
            st.session_state.detected_sub = "General Systems Architecture"
            st.session_state.raw_chat_input = ""
            st.session_state.current_roadmap = ["🚀 STEP 1: Input your aspirations to synthesize a custom career strategy."]
            st.session_state.chat_history = [{"role": "assistant", "content": "🚨 PRIVACY DIRECTIVE ENFORCED: Wiped all long-term metrics safely from MongoDB vault snapshots."}]
            st.session_state.mongodb_vault[student_id] = {"target_track": "Core Software Engineering", "detected_sub": "General Systems Architecture", "academic_hurdles": [], "career_roadmap": [], "raw_input": "", "verification_status": "Vault Profile Purged 🗑️"}
            st.sidebar.error("🗑️ Vault Checkpoint Purged")
            st.rerun()

        # Regenerate Timeline Roadmap dynamically for conversational changes
        if st.session_state.current_career == "UI/UX Visual Design":
            st.session_state.current_roadmap = [f"🎨 FIGMA TASK (Sem {current_semester}): Build 3 layouts for {st.session_state.detected_sub}.", "🎨 Publish vector prototype workflows to Behance.", f"🎯 PLACEMENT FOCUS: Complete core {st.session_state.current_career} applications."]
        elif st.session_state.current_career == "AI Research & Data Science":
            st.session_state.current_roadmap = [f"📊 DATASETS (Sem {current_semester}): Train tracking vectors for {st.session_state.detected_sub}.", "📊 Implement modeling scripts cleanly in Python.", f"🎯 PLACEMENT FOCUS: Complete core {st.session_state.current_career} applications."]
        elif st.session_state.current_career == "Cloud Systems & DevOps":
            st.session_state.current_roadmap = [f"☁️ DEV INSTANCE (Sem {current_semester}): Deploy spaces for {st.session_state.detected_sub}.", "☁️ Configure automated testing script runners.", f"🎯 PLACEMENT FOCUS: Complete core {st.session_state.current_career} applications."]
        else:
            if "Struggling with Data Structures" in st.session_state.current_hurdles:
                st.session_state.current_roadmap = ["⚠️ CRITICAL PATH ADAPTATION: Core structure vulnerability detected.", f"⏳ REMEDIATION (Sem {current_semester}): Skip standard projects; complete 20 array operations.", f"🎯 PLACEMENT FOCUS: Complete baseline {st.session_state.current_career} applications."]
            else:
                st.session_state.current_roadmap = [f"🚀 REPO CREATE (Sem {current_semester}): Launch codebases optimized for {st.session_state.detected_sub}.", "⏳ Tune performance loading asset parameters.", f"🎯 PLACEMENT FOCUS: Complete baseline {st.session_state.current_career} applications."]

    # Commit synchronized chat updates back into our central database vault dictionary snapshot
    st.session_state.mongodb_vault[student_id] = {
        "target_track": st.session_state.current_career,
        "detected_sub": st.session_state.detected_sub,
        "academic_hurdles": st.session_state.current_hurdles,
        "career_roadmap": st.session_state.current_roadmap,
        "raw_input": st.session_state.raw_chat_input,
        "verification_status": "Chat Ingestion Sync Complete ✅"
    }

    with chat_frame:
        with st.chat_message("assistant"):
            st.write(ai_reply)
    st.session_state.chat_history.append({"role": "assistant", "content": ai_reply})
    st.rerun()

    st.divider()
st.subheader("🗺️ Dynamic Agentic Memory Roadmap Blueprint")
st.info("💡 The blueprint below automatically recalibrates its milestones based on the active memory states captured by the agent above.")

# Create 3 clean tabs to separate the guidance systematically
tab1, tab2, tab3 = st.tabs(["🚀 Internship Milestones", "🎓 Academic Hurdle Tracker", "🐙 Repository Optimization"])

with tab1:
    st.markdown(f"### Target Pathway: **{st.session_state.get('current_career', 'Core Software Engineering')}**")
    st.write("---")
    if "web" in str(st.session_state.get('detected_sub', '')).lower() or "frontend" in str(st.session_state.get('detected_sub', '')).lower():
        st.markdown("""
        **Phase 1: Portfolio Building (Weeks 1-4)**
        * Build responsive single-page applications utilizing modern asynchronous data fetching.
        * Core Focus: Master DOM optimization, event loop handling, and state preservation.

        **Phase 2: Target Internship Funnel (Weeks 5-8)**
        * Target Roles: Frontend Intern, Associate Full-Stack Engineer, UI Platform Intern.
        * Strategy: Practice system design interviews for web applications (Caching, CDNs, Load Balancing).
        """)
    else:
        st.markdown("""
        **Phase 1: Foundation (Weeks 1-4)**
        * Focus on baseline computing concepts, memory layouts, and algorithmic runtime optimization.
        
        **Phase 2: Application Pipeline (Weeks 5-8)**
        * Optimize your active LinkedIn profile and structure resume bullet points utilizing the STAR method matrix.
        """)

with tab2:
    st.markdown("### 📚 Active Academic Mitigation Plan")
    st.write("---")
    
    # 🕵️‍♂️ Safe Inspection Trick: Build a collection check based on what is actively selected
    active_remediations = []
    
    # Check if the session states for the checkboxes are explicitly True
    if st.session_state.get('Data Structures & Algorithms') == True or st.session_state.get('dsa') == True:
        active_remediations.append("Data Structures & Algorithms")
    if st.session_state.get('Advanced Systems Architecture') == True or st.session_state.get('asa') == True:
        active_remediations.append("Advanced Systems Architecture")
        
    # Extra safety guardrail: if the checkboxes list variable contains the elements
    current_hurdles_list = st.session_state.get('academic_hurdles', st.session_state.get('selected_hurdles', []))
    if current_hurdles_list:
        for item in current_hurdles_list:
            if item not in active_remediations:
                active_remediations.append(item)

    # Render the tailored roadmap modules dynamically based on the verified selections
    if active_remediations:
        for hurdle in active_remediations:
            st.markdown(f"#### 🛑 Action Plan for: **{hurdle}**")
            if "Data Structures" in str(hurdle):
                st.markdown("""
                * **Core Focus:** Spend 45 minutes daily implementing Graph Traversals (BFS/DFS) and Hash Tables manually without core language libraries.
                * **Remediation Task:** Map your current data structure hurdle directly into memory tracking vectors.
                * **Career Alignment:** This directly patterns into standard technical interview vetting protocols used by tier-1 internship pathways.
                """)
                st.write("")
            elif "Advanced Systems" in str(hurdle) or "Architecture" in str(hurdle):
                st.markdown("""
                * **Core Focus:** Study microservice communication patterns, system load balancing methods, and low-level caching layers.
                * **Remediation Task:** Execute target performance loops and benchmark structural data layouts.
                * **Career Alignment:** Prepares your background profile explicitly for advanced Systems Engineering placement rounds.
                """)
                st.write("")
    else:
        # Fallback check to catch any other custom string input arrays silently
        st.markdown("#### 🛑 Active Remediation Blueprint")
        st.markdown("""
        * **Current Focus:** Stored memory profiles flag an active core data structure hurdle.
        * **Remediation Plan:** Skip baseline modular assignments; execute 20 targeted loop runtime tracking procedures.
        * **Placement Action:** Direct development efforts toward Core Software Engineering applications.
        """)
with tab3:
    st.markdown("### 🛠️ Continuous Repository Guidance")
    st.write("---")
    st.markdown(f"**Current Context Target:** `{st.session_state.get('detected_sub', 'General Systems Architecture')}`")
    st.markdown(f"""
    * **Immediate Project Goal:** {st.session_state.get('repo_action_text', 'Launch codebases optimized for your active pathway.')}
    * **Quality Check Action:** Integrate automated unit testing frameworks and explicit configuration logs into your latest project directories to impress repo auditors.
    """)

    st.write("---")
# Collect all current states to compile into a neat file layout string
download_text = f"""PATHFINDER AGENTIC ROADMAP REPORT
=================================
Target Career Track: {st.session_state.get('current_career', 'Core Software Engineering')}
Subcategory focus: {st.session_state.get('detected_sub', 'General Systems Architecture')}
Active Tracked Hurdles: {', '.join(st.session_state.get('academic_hurdles', st.session_state.get('selected_hurdles', ['None logged'])))}

Generated dynamically by Pathfinder Agentic Memory Core.
"""

st.download_button(
    label="📥 Download My Tailored Roadmap (.txt)",
    data=download_text,
    file_name="pathfinder_career_blueprint.txt",
    mime="text/plain"
)