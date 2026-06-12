import streamlit as st
import numpy as np
import pandas as pd
import io
import time

# --- 1. ENTERPRISE VIEWPORT INITIALIZATION ---
st.set_page_config(page_title="Predict World Cup | Global Sports Network", layout="wide")

# --- 2. MULTILINGUAL DICTIONARY MATRIX (10 LANGUAGES) ---
LANGUAGES = ["English", "العربية", "Español", "Français", "Português", "Deutsch", "Italiano", "日本語", "한국어", "Русский"]
selected_lang = st.sidebar.selectbox("🌐 System Language Selector", LANGUAGES)

# --- 3. 48-TEAM CORE PREDICTIVE DATABASE ---
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
        'Round of 16', 'Groups', 'Groups', 'DNQ', 'Winner', 'DNQ', 'DNQ', 'DNQ',
        'Quarter-final', 'Groups', 'Groups', 'DNQ', 'Runner-up', '4th Place', 'DNQ', 'DNQ',
        'Round of 16', 'Round of 16', '3rd Place', 'DNQ', 'Quarter-final', 'Quarter-final', 'Round of 16', 'DNQ',
        'Quarter-final', 'Groups', 'Groups', 'DNQ', 'Groups', 'Round of 16', 'Round of 16', 'DNQ',
        'DNQ', 'DNQ', 'DNQ', 'DNQ', 'Round of 16', 'Groups', 'DNQ', 'DNQ',
        'Groups', 'DNQ', 'Groups', 'Groups', 'Groups', 'Groups', 'Groups', 'DNQ'
    ]
})

# --- 4. PERSISTENT MEMORY STORAGE ---
if 'chat_data' not in st.session_state:
    st.session_state.chat_data = [{"user": "Noman_Mozeb_👑", "msg": "Ecosystem initialized successfully."}]
if 'feature_votes' not in st.session_state:
    st.session_state.feature_votes = {"Live API Integration": 520, "Injury Report Updates": 310}

# --- 5. GOOGLE ADSENSE PLACEMENT FUNCTION ---
def show_adsense_banner(label, target_type="Global Dynamic"):
    st.markdown(
        f"""
        <div style="background: repeating-linear-gradient(45deg, #111A2E, #111A2E 10px, #172442 10px, #172442 20px); border: 2px dashed #00F5D4; padding: 15px; text-align: center; border-radius: 8px; margin: 15px 0;">
            <span style="color: #00F5D4; font-size: 0.8em; font-weight: bold; letter-spacing: 2px;">⚡ GOOGLE ADSENSE CODE SLOT: {label.upper()}</span>
            <br><span style="color: #A0AEC0; font-size: 0.75em;">Target Profile Vector: {target_type}</span>
        </div>
        """, unsafe_allow_html=True
    )

# --- 6. CORE PLATFORM BRANDING HEADER ---
st.markdown(
    """
    <div style="background: linear-gradient(135deg, #1A2238 0%, #0B132B 100%); padding: 30px; border-radius: 12px; border-bottom: 4px solid #00F5D4; text-align: center; margin-bottom: 25px;">
        <h1 style="color: #FFFFFF; font-size: 2.8em; margin: 0; font-weight: 800; letter-spacing: 1px;">🔮 PREDICT WORLD CUP</h1>
        <p style="color: #00F5D4; font-size: 1.1em; font-weight: 600; margin: 5px 0 0 0;">The Miracle AI Engine of Noman Ayedh Ali Mozeb × Google Collaboration</p>
    </div>
    """, unsafe_allow_html=True
)

# --- 7. MASTER SIDEBAR DIRECTORY CONFIGURATION ---
# Clean, exact names for the directory selector
DEPARTMENTS = [
    "7. Dashboard",
    "10. Match Center",
    "3. Sports News",
    "26. Website Blog",
    "3. Services: Website Building & Ad Design",
    "3. Products: Sportswear, Shoes & Equipment",
    "3. Products: Nutritional Supplements",
    "3. App Downloads (Google Play & Apple Store)",
    "4. Google Cloud & Domains Selling",
    "5. GitHub Hostings",
    "6. Sports Data API (Opta & Sportradar Matrix)",
    "8. Gamification Arena",
    "9. Competitions & Prizes for Winners",
    "11. Multimedia & Video Hub",
    "12. Sponsored Content Portal",
    "13. Advanced Filtering (My Feed)",
    "14. Monetization & Ad Spaces Directory",
    "15. Smart Ad Placement Engine",
    "16. Geo-Ads Panel (Local, Regional, International)",
    "17. Splash Screen & Loader Ads Config",
    "18. Feed Embedded Ads Display",
    "19. Opta / Sportradar Integration Console",
    "20. Marketing & Growth Dashboard",
    "21. Affiliate & Commission Engine",
    "22. Sponsored Match Stat Analyzer",
    "23. Tournament Sponsorship (World Cup 2026)",
    "24. Push Notifications Dispatcher",
    "25. Payments & Premium Subscriptions",
    "26. Useful Quick Links (All URLs Hub)",
    "27. Sports Analysis & Technical Columns",
    "28. Advanced Analytics Predictor Engine",
    "29. User Comments Board",
    "3. About Us (Platform Introduction)",
    "3. Contact Information (Social Media Hub)",
    "30. Privacy Policy & Terms of Service"
]

selected_page = st.sidebar.selectbox("🗂️ Platform Department Directory (30 Modules)", DEPARTMENTS)

# Strategic Cloud Partner Panel Links
st.sidebar.markdown("---")
st.sidebar.markdown("### 🤝 Strategic Cloud Partners")
st.sidebar.markdown("🔗 **[Google Cloud Servers](https://google.com)**")
st.sidebar.markdown("🔗 **[Google Domains Registry](https://domains.google)**")
st.sidebar.markdown("🔗 **[GitHub Production Hosting](https://github.com)**")

# --- 8. PERMANENT INTERACTIVE LAYOUT STRATEGY ---
col_left, col_right = st.columns([2, 1])

with col_left:
    # CORE REQUIREMENT: The prediction match tools are anchored at the top of the application layout
    st.markdown("### 🏟️ AI Match Prediction Engine")
    
    all_teams = sorted(TEAMS_DB['Team'].tolist())
    box1, box2 = st.columns(2)
    with box1:
        team_1 = st.selectbox("Select First Team:", all_teams, index=all_teams.index('Argentina'))
    with box2:
        team_2 = st.selectbox("Select Second Team:", all_teams, index=all_teams.index('France'))
        
    user_choice = st.radio("Who is your chosen winner?", [team_1, team_2], horizontal=True)
    
    if st.button("🚀 RUN GOOGLE AI MODEL SIMULATION", use_container_width=True):
        if team_1 == team_2:
            st.error("Error: Teams must be distinct selections.")
        else:
            # Clear float calculations using local index positions
            l1 = float(TEAMS_DB[TEAMS_DB['Team'] == team_1]['Strength'].iloc[0])
            l2 = float(TEAMS_DB[TEAMS_DB['Team'] == team_2]['Strength'].iloc[0])
            
            w1, w2 = 0, 0
            for _ in range(1000):
                if np.random.poisson(l1) > np.random.poisson(l2): w1 += 1
                else: w2 += 1
                
            p1 = (w1 / 1000) * 100
            p2 = (w2 / 1000) * 100
            
            st.markdown("#### 📊 Simulation Complete (1,000 Analytics Scenarios Executed)")
            res1, res2 = st.columns(2)
            res1.metric(f"{team_1} Win Probability", f"{p1:.1f}%")
            res2.metric(f"{team_2} Win Probability", f"{p2:.1f}%")
            
            ai_verdict = team_1 if p1 > p2 else team_2
            if user_choice == ai_verdict:
                st.balloons()
                st.success("🎉 Correct Match! Points added to user profile.")
            else:
                st.warning("⚠️ Variance recorded against AI computational matrix.")

    # REQUIREMENT 2: Integrated Excel Data Download Module
    st.markdown("#### 📥 Export Data Hub")
    xlsx_buffer = io.BytesIO()
    with pd.ExcelWriter(xlsx_buffer, engine='openpyxl') as writer:
        TEAMS_DB.to_excel(writer, index=False, sheet_name="Predictive Strength Indexes")
    st.download_button(
        label="Download Full 48-Team Predictive Table (Excel)",
        data=xlsx_buffer.getvalue(),
        file_name="Predict_World_Cup_Data.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        use_container_width=True
    )

    st.markdown("---")
    # --- DYNAMIC STRUCTURAL DEPARTMENT VIEWS ---
    st.markdown(f"## 📁 Section: {selected_page}")

    if selected_page == "7. Dashboard":
        st.write("Welcome to the Master Admin Traffic and System Analytics Dashboard.")
        show_adsense_banner("Dashboard Banner Node", "Local Node Profile Targeting")

    elif selected_page == "10. Match Center":
        st.write("Live scores, active fixtures, standings, and tournament group updates.")
        st.dataframe(TEAMS_DB[['Group', 'Team']], use_container_width=True)

    elif selected_page == "3. Sports News":
        st.write("### 📢 Top Headlines")
        st.markdown("- **Breaking:** Real-time data adjustments track strong training metrics for Group E.\n- **Analysis:** High-density analytics favor wing-back field coverage arrays.")

    elif selected_page == "26. Website Blog":
        st.write("Insights, thought pieces, and technical documentation regarding the deployment of sports analytics models.")

    elif selected_page == "3. Services: Website Building & Ad Design":
        st.write("Our technology stack offers professional services to global sports brands:")
        st.info("💻 **Website Building:** Fast, fully responsive sports portals.\n\n🎨 **Ad Design:** Optimized banners to maximize Google AdSense click-through rates.")

    elif selected_page == "3. Products: Sportswear, Shoes & Equipment":
        st.write("Browse professional sportswear, performance shoes, and official match equipment.")
        st.markdown("- 👟 *Elite Performance Vault Cleats*\n- 👕 *Official Stadium Training Kit Jerseys*")

    elif selected_page == "3. Products: Nutritional Supplements":
