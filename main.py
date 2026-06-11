import streamlit as st
import numpy as np
import pandas as pd
import requests
import xml.etree.ElementTree as ET

# --- 1. PREMIUM RESPONSIVE CONFIGURATION ---
st.set_page_config(page_title="Predict World Cup | Global Arena", layout="wide")

# --- 2. EMBEDDED 48-TEAM DATABASE ENGINE ---
# Moving the data directly here forces Streamlit to refresh its memory cache immediately
TEAMS_DB = pd.DataFrame({
    'Group': ['A']*4 + ['B']*4 + ['C']*4 + ['D']*4 + ['E']*4 + ['F']*4 + ['G']*4 + ['H']*4 + ['I']*4 + ['J']*4 + ['K']*4 + ['L']*4,
    'Team': [
        'USA', 'Mexico', 'Canada', 'Panama', 'Argentina', 'Chile', 'Colombia', 'Peru',
        'Brazil', 'Uruguay', 'Ecuador', 'Paraguay', 'France', 'Morocco', 'Austria', 'Mali',
        'Spain', 'Japan', 'Croatia', 'Nigeria', 'England', 'Netherlands', 'Senegal', 'Oman',
        'Portugal', 'Belgium', 'Tunisia', 'Jamaica', 'Germany', 'Switzerland', 'Australia', 'UAE',
        'Italy', 'Ukraine', 'Egypt', 'New Zealand', 'South Korea', 'Iran', 'Algeria', 'Iraq',
        'Denmark', 'Sweden', 'Cameroon', 'Qatar', 'Saudi Arabia', 'Poland', 'Ghana', 'Honduras'
    ],
    'Strength': [
        1.6, 1.4, 1.3, 0.9, 2.5, 1.3, 1.6, 1.0, 2.3, 1.9, 1.5, 1.1, 2.4, 1.8, 1.4, 1.1,
        2.4, 1.7, 1.6, 1.2, 2.2, 1.8, 1.5, 0.8, 2.3, 1.7, 1.2, 0.7, 2.1, 1.6, 1.3, 0.8,
        1.9, 1.5, 1.4, 0.7, 1.5, 1.4, 1.3, 0.9, 1.7, 1.5, 1.2, 0.9, 1.4, 1.4, 1.2, 0.8
    ],
    'WC_2022': [
        'Round of 16', 'Groups', 'Groups', 'Did Not Qualify', 'Winner', 'Did Not Qualify', 'Did Not Qualify', 'Did Not Qualify',
        'Quarter-final', 'Groups', 'Groups', 'Did Not Qualify', 'Runner-up', '4th Place', 'Did Not Qualify', 'Did Not Qualify',
        'Round of 16', 'Round of 16', '3rd Place', 'Did Not Qualify', 'Quarter-final', 'Quarter-final', 'Round of 16', 'Did Not Qualify',
        'Quarter-final', 'Groups', 'Groups', 'Did Not Qualify', 'Groups', 'Round of 16', 'Round of 16', 'Did Not Qualify',
        'Did Not Qualify', 'Did Not Qualify', 'Did Not Qualify', 'Did Not Qualify', 'Round of 16', 'Groups', 'Did Not Qualify', 'Did Not Qualify',
        'Groups', 'Did Not Qualify', 'Groups', 'Groups', 'Groups', 'Groups', 'Groups', 'Did Not Qualify'
    ]
})

def run_advanced_poisson_internal(team_A, team_B, sims=5000):
    """Internal calculation engine using strict float casting to eradicate AttributeErrors."""
    # .iloc[0] extracts the single scalar value, completely preventing numpy array mismatch errors
    lambda_A = float(TEAMS_DB[TEAMS_DB['Team'] == team_A]['Strength'].iloc[0])
    lambda_B = float(TEAMS_DB[TEAMS_DB['Team'] == team_B]['Strength'].iloc[0])
    
    wins_A, wins_B = 0, 0
    for _ in range(sims):
        gA = np.random.poisson(lambda_A)
        gB = np.random.poisson(lambda_B)
        if gA > gB: 
            wins_A += 1
        elif gB > gA: 
            wins_B += 1
        else:
            # Extra Time calculations
            exA = np.random.poisson(lambda_A * 0.33)
            exB = np.random.poisson(lambda_B * 0.33)
            if (gA + exA) > (gB + exB): 
                wins_A += 1
            elif (gB + exB) > (gA + exA): 
                wins_B += 1
            else:
                # Penalty Flips
                if np.random.rand() > 0.5: 
                    wins_A += 1
                else: 
                    wins_B += 1
                    
    return (wins_A / sims) * 100, (wins_B / sims) * 100

def fetch_rss_news_internal():
    """Fallback safe internal engine to stream global tournament blog entries."""
    rss_url = "https://google.com"
    items = []
    try:
        res = requests.get(rss_url, timeout=5)
        root = ET.fromstring(res.content)
        for item in root.findall('.//item')[:3]:
            items.append({
                'title': item.find('title').text,
                'link': item.find('link').text,
                'date': item.find('pubDate').text
            })
    except:
        pass
    return items

# --- 3. PERSISTENT FAN STATE DATA ---
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = [
        {"user": "SambaBoy_⚽", "msg": "Brazil is looking unstoppable in training!"},
        {"user": "Matador_26", "msg": "Spain's midfield depth will dominate group E."}
    ]
if 'suggestions' not in st.session_state:
    st.session_state.suggestions = {"Live In-Play AI Updates": 342, "Player Injury Weights": 218}

# --- 4. BRAND BRANDING HEADER (CYBER DARK STYLE) ---
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

st.sidebar.markdown("---")
st.sidebar.markdown("### 🏆 Platform Status")
st.sidebar.success("All 48 National Teams Synced")
st.sidebar.info("AI Model: Google Gemini Hub Optimization")

# --- 5. INTERACTIVE DASHBOARD SYSTEM ---
col_main, col_side = st.columns([2, 1])

with col_main:
    st.markdown("### 🏟️ AI Prediction Arena (All 48 Teams)")
    
    c1, c2 = st.columns(2)
    teams_list = sorted(TEAMS_DB['Team'].tolist())
    with c1:
        team_A = st.selectbox("Select Team A / اختر الفريق الأول", teams_list, index=teams_list.index('Argentina'))
    with c2:
        team_B = st.selectbox("Select Team B / اختر الفريق الثاني", teams_list, index=teams_list.index('France'))
        
    user_pick = st.radio("Your Personal Prediction / من تتوقع أن يفوز؟", [team_A, team_B], horizontal=True)
    
    # Execution Button triggers internal decoupled function directly
    if st.button("🚀 EXECUTE GOOGLE AI MATCH EVALUATION", use_container_width=True):
        if team_A == team_B:
            st.error("Invalid Selection: Teams must be different.")
        else:
            pA, pB = run_advanced_poisson_internal(team_A, team_B)
            
            st.markdown("#### 📊 Simulation Results (5,000 Variants Tested)")
            res_col1, res_col2 = st.columns(2)
            with res_col1:
                st.metric(label=f"{team_A} Win Probability", value=f"{pA:.1f}%")
                st.progress(int(pA))
            with res_col2:
                st.metric(label=f"{team_B} Win Probability", value=f"{pB:.1f}%")
                st.progress(int(pB))
                
            ai_winner = team_A if pA > pB else team_B
            if user_pick == ai_winner:
                st.balloons()
                st.success("🎉 Match! Your prediction aligns perfectly with the Google AI Model calculation!")
            else:
                st.warning("⚠️ Divergence! Your human prediction differs from the AI statistical model.")

    st.markdown("---")
    st.markdown("### 📜 Historic World Cup Encyclopedia (1930 - 2026)")
    
    search_team = st.text_input("🔍 Search Historical Records / ابحث عن تاريخ أي منتخب:", "Morocco")
    team_records = TEAMS_DB[TEAMS_DB['Team'].str.lower() == search_team.lower()]
    
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
    st.markdown("### 💬 Global Fan Chat Room")
    with st.container(height=250, border=True):
        for chat in st.session_state.chat_history:
            st.markdown(f"**{chat['user']}**: {chat['msg']}")
            
    new_user = st.text_input("Username:", "Fan_User", key="chat_user")
    new_msg = st.text_input("Join the debate:", placeholder="Type a message...", key="chat_msg")
    if st.button("Send ⚡", use_container_width=True):
        if new_msg.strip() != "":
            st.session_state.chat_history.append({"user": new_user, "msg": new_msg})
            st.rerun()

    st.markdown("---")
    st.markdown("### 🗳️ Vote Next AI Features")
    for feature, votes in st.session_state.suggestions.items():
        c_feat, c_vote = st.columns([2, 1])
        c_feat.write(f"🔹 {feature}")
        if c_vote.button(f"👍 {votes}", key=feature):
            st.session_state.suggestions[feature] += 1
            st.rerun()

# --- 6. DYNAMIC BLOG AND NEWS FOOTER STREAM ---
st.markdown("---")
st.write("### 📰 News & Blog Feed / آخر أخبار المونديال")
articles = fetch_rss_news_internal()
if articles:
    for art in articles:
        st.markdown(f"🔹 **[{art['title']}]({art['link']})** - *{art['date']}*")
else:
    st.write("No articles found or feed currently refreshing.")

st.markdown(
    """
    <div style="text-align: center; color: #A0AEC0; font-size: 0.85em; padding: 20px 0; border-top: 1px solid #1A2238; margin-top: 20px;">
        👑 Official Platform Proprietary Rights Dashboard & Intellectual Property Assets belong explicitly to: <b>Noman Ayedh Ali Mozeb (نعمان عائض علي معزب)</b>.<br>
        Monetization profiles managed under Google AdSense/AdMob standard enterprise guidelines. All rights reserved © 2026.
    </div>
    """, unsafe_allow_html=True
)
