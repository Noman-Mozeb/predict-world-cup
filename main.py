import streamlit as st
import database as db
import news as nw

st.title("🔮 Predict World Cup")
st.caption("Official Founder: **Noman Ayedh Ali Mozeb** | Co-Managed with Google AI")

lang = st.sidebar.radio("Language / اللغة", ["English", "العربية"])
is_ar = (lang == "العربية")

teams_list = db.TEAMS_DB['Team'].tolist()
col1, col2 = st.columns(2)
with col1: tA = st.selectbox("Team A" if not is_ar else "المنتخب الأول", teams_list, index=0)
with col2: tB = st.selectbox("Team B" if not is_ar else "المنتخب الثاني", teams_list, index=1)

if st.button("Run Simulation" if not is_ar else "تشغيل المحاكاة", use_container_width=True):
    if tA == tB:
        st.error("Error: Select distinct teams." if not is_ar else "خطأ: اختر منتخبين مختلفين.")
    else:
        pA, pB = db.run_poisson_engine(tA, tB)
        st.metric(f"{tA}", f"{pA:.1f}%")
        st.metric(f"{tB}", f"{pB:.1f}%")

st.markdown("---")
st.write("### 📰 News & Blog Feed / آخر أخبار المونديال")
articles = nw.pull_rss_news_stream()
for art in articles:
    st.markdown(f"🔹 **[{art['title']}]({art['link']})** - {art['date']}")
