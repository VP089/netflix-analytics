import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from analytics import NetflixAnalyticsEngine
import sys

st.set_page_config(page_title="Netflix Strateji Analitika Mərkəzi", page_icon="🍿", layout="wide")

# NETFLIX PREMIUM TÜND MÖVZUSU VƏ XÜSUSİ STİL CSS-İ
st.markdown("""
    <style>
    .stApp {
        background-color: #141414;
        color: #FFFFFF;
    }
    
    /* ƏSAS BAŞLIQ */
    .main-title {
        color: #E50914 !important;
        font-size: 38px;
        font-weight: 900;
        margin-bottom: 5px;
        text-shadow: 0px 0px 14px rgba(229, 9, 20, 0.6);
    }
    
    /* KPI KARTLARI */
    .kpi-card {
        background: linear-gradient(145deg, #1f1f1f, #141414);
        border: 2px solid #E50914;
        border-radius: 12px;
        padding: 18px 15px;
        text-align: center;
        box-shadow: 0px 4px 15px rgba(229, 9, 20, 0.35);
        margin-bottom: 10px;
    }
    
    .kpi-title {
        color: #B3B3B3;
        font-size: 14px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        margin-bottom: 8px;
    }
    
    .kpi-value {
        color: #E50914 !important;
        font-size: 34px;
        font-weight: 800;
        text-shadow: 0px 0px 12px rgba(229, 9, 20, 0.5);
    }

    .red-header {
        color: #E50914 !important;
        font-weight: 800;
        font-size: 24px;
        margin-bottom: 12px;
        text-shadow: 0px 0px 8px rgba(229, 9, 20, 0.4);
    }

    /* POSTER MƏLUMAT KART CƏDVƏLİ */
    .poster-info-box {
        background-color: #1f1f1f;
        border: 1px solid #333333;
        border-radius: 8px;
        padding: 8px;
        text-align: center;
        margin-top: 5px;
        margin-bottom: 20px;
    }
    .poster-title-text {
        font-size: 13px;
        font-weight: 800;
        color: #FFFFFF;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }
    .poster-meta {
        display: flex;
        justify-content: space-around;
        align-items: center;
        margin-top: 5px;
        font-size: 11px;
        font-weight: 700;
    }
    .meta-rating { color: #FFD700; }
    .meta-roi { color: #46D369; }

    /* STRATEJİ QƏRAR BLOKLARI */
    .strategy-card-success {
        background-color: rgba(46, 213, 115, 0.1);
        border: 2px solid #2ed573;
        border-radius: 10px;
        padding: 15px;
        margin-top: 15px;
        color: #2ed573;
        font-weight: bold;
    }
    
    .strategy-card-warning {
        background-color: rgba(255, 215, 0, 0.1);
        border: 2px solid #ffd700;
        border-radius: 10px;
        padding: 15px;
        margin-top: 15px;
        color: #ffd700;
        font-weight: bold;
    }

    /* SİMULYASİYA NƏTİCƏLƏRİ - QALIN TÜND AĞ */
    [data-testid="stMetricValue"] {
        color: #FFFFFF !important;
        font-weight: 900 !important;
        font-size: 32px !important;
        text-shadow: 0px 0px 8px rgba(255, 255, 255, 0.6);
    }
    [data-testid="stMetricLabel"] {
        color: #E0E0E0 !important;
        font-weight: 700 !important;
    }

    /* MƏLUMATLARI CSV KİMİ YÜKLƏ DÜYMƏSİ (AÇIQ QARA / TÜND BOZ DÜYMƏ) */
    .stDownloadButton > button {
        background-color: #2b2b2b !important;
        color: #FFFFFF !important;
        border: 1px solid #444444 !important;
        border-radius: 8px !important;
        font-weight: 800 !important;
        font-size: 15px !important;
        padding: 10px 20px !important;
        transition: all 0.3s ease !important;
    }
    .stDownloadButton > button:hover {
        background-color: #3d3d3d !important;
        border-color: #E50914 !important;
        color: #FFFFFF !important;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.5);
    }

    /* EXCEL CƏDVƏL STİLİ */
    .excel-table-container {
        max-height: 520px;
        overflow-y: auto;
        border: 2px solid #217346;
        border-radius: 6px;
        background-color: #ffffff;
    }
    .excel-table {
        width: 100%;
        border-collapse: collapse;
        color: #000000 !important;
        font-size: 13px;
    }
    .excel-table th {
        background-color: #217346 !important;
        color: #ffffff !important;
        font-weight: 700;
        padding: 9px 12px;
        position: sticky;
        top: 0;
    }
    .excel-table td {
        padding: 8px 12px;
        border: 1px solid #d4d4d4;
        color: #000000 !important;
    }

    /* STANDART DÜYMƏ (RED) */
    .stButton>button {
        background-color: #E50914;
        color: white;
        border-radius: 6px;
        font-weight: bold;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🍿 Netflix Strateji Monetizasiya və Analitika Mərkəzi</div>', unsafe_allow_html=True)
st.caption("Qlobal İzlənmə, Məzmun İnvestisiyaları və ROI Proqnozlaşdırılmasının Ağıllı İdarəetmə Paneli")

@st.cache_resource(ttl=1)
def load_engine():
    return NetflixAnalyticsEngine()

with st.spinner("Netflix Analitika Baza Platforması Yüklənir..."):
    engine = load_engine()

df = engine.df

# YAN PANELDƏKİ FİLTRLƏR
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/0/08/Netflix_2015_logo.svg", width=160)
st.sidebar.header("🎯 Analitik Filtrlər")

selected_genres = st.sidebar.multiselect(
    "Janrları Seçin:",
    options=df['genre'].unique(),
    default=df['genre'].unique()
)

min_rating, max_rating = st.sidebar.slider(
    "Reytinq Diapazonu:",
    float(df['vote_average'].min()), 
    10.0, 
    (float(df['vote_average'].min()), 10.0)
)

filtered_df = df[
    (df['genre'].isin(selected_genres)) & 
    (df['vote_average'] >= min_rating) & 
    (df['vote_average'] <= max_rating)
]

tab1, tab2, tab3 = st.tabs([
    "📈 İcraçı Xülasəsi", 
    "📊 Dərin Analiz və Məlumat İxracı", 
    "💡 İnvestisiya və ROI Simulyatoru"
])

# ================= TAB 1: İCRAÇI XÜLASƏSİ =================
with tab1:
    st.subheader("📌 Əsas Performans Göstəriciləri (Qlobal KPİ-lar)")
    
    if filtered_df.empty:
        st.warning("⚠️ Seçilmiş reytinq və ya janr filtrinə uyğun heç bir film tapılmadı. Zəhmət olmasa filtrləri genişləndirin.")
    else:
        k1, k2, k3, k4 = st.columns(4)
        with k1:
            st.markdown(f'<div class="kpi-card"><div class="kpi-title">🎬 Analiz Edilən Filmlər</div><div class="kpi-value">{len(filtered_df)}</div></div>', unsafe_allow_html=True)
        with k2:
            st.markdown(f'<div class="kpi-card"><div class="kpi-title">💵 Ümumi Təxmini Gəlir</div><div class="kpi-value">${round(filtered_df["est_revenue_m"].sum(), 1)}M</div></div>', unsafe_allow_html=True)
        with k3:
            st.markdown(f'<div class="kpi-card"><div class="kpi-title">📈 Ortalama ROI %</div><div class="kpi-value">{round(filtered_df["roi_percent"].mean(), 1)}%</div></div>', unsafe_allow_html=True)
        with k4:
            st.markdown(f'<div class="kpi-card"><div class="kpi-title">⏱️ Ortalama İzlənmə</div><div class="kpi-value">{round(filtered_df["view_hours_millions"].mean(), 1)}M <span style="font-size:18px;">Saat</span></div></div>', unsafe_allow_html=True)
        
        st.divider()
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("💰 Janrlar üzrə Gəlir və İstehsal Xərcləri")
            fig_finance = px.bar(
                filtered_df.groupby('genre')[['production_cost_m', 'est_revenue_m']].mean().reset_index(),
                x='genre', y=['production_cost_m', 'est_revenue_m'],
                barmode='group',
                labels={'value': 'Milyon USD ($)', 'genre': 'Janr', 'variable': 'Göstərici'},
                color_discrete_sequence=['#464646', '#E50914'],
                template="plotly_dark"
            )
            fig_finance.for_each_trace(lambda t: t.update(name = "İstehsal Xərci ($M)" if t.name == "production_cost_m" else "Təxmini Gəlir ($M)"))
            st.plotly_chart(fig_finance, use_container_width=True)

        with col2:
            st.subheader("⚡ ROI % və İzlənmə Effektivliyi")
            fig_bubble = px.scatter(
                filtered_df, x='content_efficiency', y='roi_percent',
                size='production_cost_m', color='genre', hover_name='movie_title',
                labels={'content_efficiency': 'Effektivlik İndeksi', 'roi_percent': 'ROI %', 'genre': 'Janr', 'production_cost_m': 'İstehsal Xərci ($M)'},
                template="plotly_dark"
            )
            st.plotly_chart(fig_bubble, use_container_width=True)

        # TOP 10 MƏZMUN QALEREYASI (10 REAL POSTER 2 SƏTİRDƏ)
        st.subheader("🎬 Top 10 Məzmun Qalereyası (Poster Vizualizasiyası)")
        
        top_10_df = filtered_df.sort_values(by='vote_average', ascending=False).head(10)
        gallery_items = top_10_df.to_dict('records')

        fallback_url = "https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=500&auto=format&fit=crop"

        if gallery_items:
            for row in range(0, len(gallery_items), 5):
                cols = st.columns(min(5, len(gallery_items) - row))
                for i, col in enumerate(cols):
                    item = gallery_items[row + i]
                    title = str(item.get('movie_title', 'Film'))
                    poster = str(item.get('poster_url', '')).strip()
                    
                    img_to_show = poster if poster.startswith('http') else fallback_url

                    with col:
                        st.image(img_to_show, use_container_width=True)
                        st.markdown(f"""
                            <div class="poster-info-box">
                                <div class="poster-title-text" title="{title}">{title}</div>
                                <div class="poster-meta">
                                    <span class="meta-rating">⭐ {item['vote_average']}</span>
                                    <span class="meta-roi">🚀 {item['roi_percent']}% ROI</span>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)

# ================= TAB 2: DƏRİN ANALİZ VƏ MƏLUMAT İXRACI =================
with tab2:
    if filtered_df.empty:
        st.warning("⚠️ Məlumat bazasında seçilən şərtlərə uyğun film tapılmadı.")
    else:
        st.markdown(f'<div class="red-header">🔍 Analitik Məlumat Bazası ({len(filtered_df)} Film)</div>', unsafe_allow_html=True)
        st.write("Aşağıdakı cədvəldən filmlərin bütün göstəricilərini araşdıra və yükləyə bilərsiniz.")
        
        csv_data = filtered_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label=f"📥 Məlumatları CSV Kimi Yüklə ({len(filtered_df)} Film)",
            data=csv_data,
            file_name='netflix_analitika_hesabati_100.csv',
            mime='text/csv'
        )
        
        display_df = filtered_df[['movie_title', 'genre', 'runtime', 'vote_average', 'production_cost_m', 'est_revenue_m', 'net_profit_m', 'roi_percent']].copy()
        display_df.insert(0, '№', range(1, len(display_df) + 1))
        display_df.columns = ['№', 'Film Adı', 'Janr', 'Müddət (dəq)', 'Reytinq', 'İstehsal Xərci ($M)', 'Təxmini Gəlir ($M)', 'Xalis Mənfəət ($M)', 'ROI %']
        
        table_html = display_df.to_html(classes='excel-table', index=False)
        st.markdown(f'<div class="excel-table-container">{table_html}</div>', unsafe_allow_html=True)

# ================= TAB 3: İNVESTİSİYA VƏ ROI SİMULYATORU =================
with tab3:
    st.subheader("💡 'Ehtimal' Məzmun İnvestisiyası və ROI Simulyatoru")
    s1, s2, s3, s4 = st.columns(4)
    with s1:
        sim_genre = st.selectbox("Film Janrı:", df['genre'].unique())
    with s2:
        sim_runtime = st.slider("Müddət (Dəqiqə):", 70, 180, 110)
    with s3:
        sim_rating = st.slider("Hədəflənən Reytinq:", 1.0, 10.0, 7.8)
    with s4:
        sim_cost = st.number_input("İstehsal Büdcəsi ($M):", min_value=5.0, max_value=200.0, value=45.0)

    if st.button("İnvestisiya Analizini Başlat 🚀"):
        res = engine.predict_simulation(sim_genre, sim_runtime, sim_rating, sim_cost)
        
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Təxmini İzlənmə", f"{res['view_hours']}M Saat")
        m2.metric("Təxmini Gəlir", f"${res['revenue']}M")
        m3.metric("Xalis Mənfəət", f"${res['net_profit']}M")
        m4.metric("Gözlənilən ROI", f"{res['roi']}%")

        st.markdown("### 🎯 Strateji Qərar")
        
        if res['roi'] >= 100:
            st.markdown(f"""
                <div class="strategy-card-success">
                    ✅ <b>Uğurlu Uyğunluq:</b> Bu layihə yüksək mənfəət potenasialına malikdir (Gözlənilən ROI: {res['roi']}%). İnvestisiya edilməsi tövsiyə olunur!
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class="strategy-card-warning">
                    ⚠️ <b>Uyğunsuzluq (Məhdud ROI):</b> Bu layihənin ROI göstəricisi ({res['roi']}%) nisbətən aşağıdır. İstehsal büdcəsini azaltmaq və ya hədəf reytinqini qaldırmaq tövsiyə olunur.
                </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    if not st.runtime.exists():
        from streamlit.web import cli as stcli
        sys.argv = ["streamlit", "run", __file__]
        sys.exit(stcli.main())