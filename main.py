import streamlit as st
import database as db
import news as nw

# Page configuration forcing premium responsive viewport scaling
st.set_page_config(page_title="Predict World Cup | Global Arena", layout="wide")

# Persistent State Engines for Chat and Suggestions
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = [
        {"user": "SambaBoy_⚽", "msg": "Brazil is looking unstoppable in training!"},
        {"user": "Matador_26", "msg": "Spain's midfield depth will dominate group E."}
    ]
if 'suggestions' not in st.session_state:
    st.session_state.suggestions = {"Live In-Play AI Updates": 342, "Player Injury Weights": 218}

# --- HEADER SECTION ---
st.markdown(
    """
    <div style="background: linear-gradient(135deg, #1A2238 0%, #0B132B 100%); padding: 30px; border-radius: 15px; border-bottom: 4px solid #00F5D4; text-align: center; margin-bottom: 25px;">
        <h1 style="color: #FFFFFF; font-size: 2.8em; margin: 0; font-weight: 800; letter-spacing: 1px;">🔮 PREDICT WORLD CUP</h1>
        <p style="color: #00F5D4; font-size: 1.1em; font-weight: 600; margin: 5px 0 0 0;">The Miracle AI Engine of Noman Ayedh Ali Mozeb × Google Collaboration</p>
    </div>
    """, 
    unsafe_allow_html=True
)

# App Navigation / Language Router
lang = st.sidebar.radio("🌐 Select Interface Language", ["English", "العربية"])
is_ar = (lang == "العربية")

# Sidebar Platform Specs
st.sidebar.markdown("---")
st.sidebar.markdown("### 🏆 Platform Status")
st.sidebar.success("All 48 National Teams Synced")
st.sidebar.info("AI Model: Google Gemini Hub Optimization")

# --- MAIN DASHBOARD LAYOUT (GRID SPLIT) ---
col_main, col_side = st.columns([2, 1])

with col_main:
    # --- MODULE 1: THE PREDICTION ARENA ---
    st.markdown("### 🏟️ AI Prediction Arena (All 48 Teams)")
    
    c1, c2 = st.columns(2)
    teams_list = sorted(db.TEAMS_DB['Team'].tolist())
    with c1:
        team_A = st.selectbox("Select Team A / اختر الفريق الأول", teams_list, index=teams_list.index('Argentina'))
    with c2:
        team_B = st.selectbox("Select Team B / اختر الفريق الثاني", teams_list, index=teams_list.index('France'))
        
    user_pick = st.radio("Your Personal Prediction / من تتوقع أن يفوز؟", [team_A, team_B], horizontal=True)
    
    if st.button("🚀 EXECUTE GOOGLE AI MATCH EVALUATION", use_container_width=True):
        if team_A == team_B:
            st.error("Invalid Selection: Teams must be different.")
        else:
            pA, pB = db.run_advanced_poisson(team_A, team_B)
            
            # Premium Visual Analytics Cards
            st.markdown("#### 📊 Simulation Results (5,000 Variants Tested)")
            res_col1, res_col2 = st.columns(2)
            with res_col1:
                st.metric(label=f"{team_A} Win Probability", value=f"{pA:.1f}%")
                st.progress(int(pA))
            with res_col2:
                st.metric(label=f"{team_B} Win Probability", value=f"{pB:.1f}%")
                st.progress(int(pB))
                
            # User vs AI Verification Algorithm
            ai_winner = team_A if pA > pB else team_B
            if user_pick == ai_winner:
                st.balloons()
                st.success("🎉 Match! Your prediction aligns perfectly with the Google AI Model calculation!")
            else:
                st.warning("⚠️ Divergence! Your human prediction differs from the AI statistical model.")

    # --- MODULE 2: REVENUE-READY CONTENT & COMPREHENSIVE HISTORIC DATABASE ---
    st.markdown("---")
    st.markdown("### 📜 Historic World Cup Encyclopedia (1930 - 2026)")
    
    search_team = st.text_input("🔍 Search Historical Records / ابحث عن تاريخ أي منتخب:", "Morocco")
    team_records = db.TEAMS_DB[db.TEAMS_DB['Team'].str.lower() == search_team.lower()]
    
    if not team_records.empty:
        st.markdown(
            f"""
            <div style="background-color: #1A2238; padding: 15px; border-radius: 10px; border-left: 4px solid #FFD700;">
                <h4 style="margin: 0; color: #FFFFFF;">Historical Metadata: {search_team}</h4>
                <p style="margin: 5px 0 0 0; color: #A0AEC0;"> Qatar 2022 Performance Placement: <b>{team_records['WC_2022'].values[0]}</b></p>
                <p style="margin: 2px 0 0 0; color: #A0AEC0;"> Base Power Rating Index: <b>{team_records['Strength'].values[0]}</b></p>
            </div>
            """, unsafe_allow_html=True
        )
    else:
        st.info("Enter any valid World Cup team name to parse archive metrics.")

with col_side:
    # --- MODULE 3: FAN INTERACTION CHAT ROOM ---
    st.markdown("### 💬 Global Fan Chat Room")
    with st.container(height=250, border=True):
        for chat in st.session_state.chat_history:
            st.markdown(f"**{chat['user']}**: {chat['msg']}")
            
    new_user = st.text_input("Username:", "Fan_User", key="chat_user")
    new_msg = st.text_input("Join the debate / شارك في النقاش:", placeholder="Type a message...", key="chat_msg")
    if st.button("Send ⚡", use_container_width=True):
        if new_msg.strip() != "":
            st.session_state.chat_history.append({"user": new_user, "msg": new_msg})
            st.rerun()

    # --- MODULE 4: DYNAMIC FEATURE SUGGESTION LAB ---
    st.markdown("---")
    st.markdown("### 🗳️ Vote Next AI Features")
    for feature, votes in st.session_state.suggestions.items():
        c_feat, c_vote = st.columns([3, 1])
        c_feat.write(f"🔹 {feature}")
        if c_vote.button(f"👍 {votes}", key=feature):
            st.session_state.suggestions[feature] += 1
            st.rerun()

# --- FOOTER & LEGAL ---
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: #A0AEC0; font-size: 0.85em; padding: 20px 0;">
        👑 Official Platform Proprietary Rights Dashboard & Intellectual Property Assets belong explicitly to: <b>Noman Ayedh Ali Mozeb (نعمان عائض علي معزب)</b>.<br>
        Monetization profiles managed under Google AdSense/AdMob standard enterprise guidelines. All rights reserved © 2026.
    </div>
    """, unsafe_allow_html=True
)
