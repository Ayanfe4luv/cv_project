"""
Bilingual Digital CV/Portfolio - Ayanfeoluwa Alabetutu
Layout: Two-Column Modern (Reference: image_37b51e.png)
Author: Ayanfeoluwa Alabetutu
"""

from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
assets_dir = current_dir / "assets"
cv_ru_file = assets_dir / "CV_RU.pdf"
cv_en_file = assets_dir / "CV_EN.pdf"
profile_pic_path = assets_dir / "profile-pic.png"

# --- BILINGUAL CONTENT ---
CONTENT = {
    "ru": {
        "page_title": "Резюме | Аянфеолува Алабетуту",
        "name": "Аянфеолува Алабетуту",
        "title": "Преподаватель | AI-специалист",
        "profile_header": "О себе",
        "description": """
        Целеустремленный специалист с 9+ годами опыта в преподавании и 3+ годами в переводах. 
        Эксперт в области AI/LLM, специализирующийся на промпт-инжиниринге и создании датасетов. 
        Обладаю навыками построения предиктивных моделей и ML-алгоритмов.
        """,
        "email": "ayanfe4luv@gmail.com",
        "phone": "+7 (987) 509-98-18",
        "location": "Новосибирск, Россия",
        "qualities_header": "Ключевые качества",
        "qualities_bubbles": ["C2 English", "AI/LLM", "Translator", "Researcher"],
        "work_header": "Опыт работы",
        "education_header": "Образование",
        "skills_header": "Навыки",
        "experience": [
            {
                "role": "AI Specialist & Content Dev",
                "company": "UREKA Biotec | Omicslogic Africa",
                "period": "2024 — Наст. время",
                "desc": "Разработка LLM-пайплайнов, промпт-инжиниринг и создание датасетов."
            },
            {
                "role": "Data Scientist (R&D)",
                "company": "SKRIND Biotec",
                "period": "2023 — 2025",
                "desc": "ML-алгоритмы, компьютерное зрение и автоматизация сбора данных."
            },
            {
                "role": "Преподаватель английского",
                "company": "Школа 21, НГПУ, Муниципальные школы",
                "period": "2016 — Наст. время",
                "desc": "Обучение студентов и специалистов, подготовка к экзаменам."
            },
        ],
        "education": [
            {
                "degree": "Ph.D. Кандидат наук",
                "school": "ФИЦ ФТМ, Новосибирск",
                "year": "2022"
            },
            {
                "degree": "Data Science",
                "school": "WorldQuant University, USA",
                "year": "2022"
            }
        ],
        "tech_skills": [
            {"name": "Python / R / SQL", "level": 90},
            {"name": "LLMs & Prompt Eng", "level": 95},
            {"name": "Machine Learning", "level": 80},
            {"name": "Translation (EN-RU)", "level": 100},
        ],
        "downloads_header": "Скачать резюме",
        "contact_header": "Контакты"
    },
    "en": {
        "page_title": "CV | Ayanfeoluwa Alabetutu",
        "name": "Ayanfeoluwa Alabetutu",
        "title": "Teacher | AI Trainer",
        "profile_header": "Profile",
        "description": """
        Purpose-driven professional with 9+ years of teaching and 3+ years in translation. 
        Expert in AI/LLM with hands-on experience in prompt engineering and dataset creation.
        Skilled in building predictive models and ML algorithms.
        """,
        "email": "ayanfe4luv@gmail.com",
        "phone": "+7 (987) 509-98-18",
        "location": "Novosibirsk, Russia",
        "qualities_header": "Key Qualities",
        "qualities_bubbles": ["C2 English", "AI/LLM", "Translator", "Researcher"],
        "work_header": "Work Experience",
        "education_header": "Education",
        "skills_header": "Skills",
        "experience": [
            {
                "role": "AI Specialist & Content Dev",
                "company": "UREKA Biotec | Omicslogic Africa",
                "period": "2024 — Present",
                "desc": "Developing LLM pipelines, prompt engineering, and dataset creation."
            },
            {
                "role": "Data Scientist (R&D)",
                "company": "SKRIND Biotec",
                "period": "2023 — 2025",
                "desc": "Building ML algorithms, computer vision, and automating data workflows."
            },
            {
                "role": "English Teacher",
                "company": "School 21, NSPU, Municipal Schools",
                "period": "2016 — Present",
                "desc": "Teaching students and professionals, exam preparation."
            },
        ],
        "education": [
            {
                "degree": "Ph.D. ",
                "school": "FRC FTM, Novosibirsk",
                "year": " 2022"
            },
            {
                "degree": "Data Science",
                "school": "WorldQuant University, USA",
                "year": "2022"
            }
        ],
        "tech_skills": [
            {"name": "Python / R / SQL", "level": 90},
            {"name": "LLMs & Prompt Eng", "level": 95},
            {"name": "Machine Learning", "level": 80},
            {"name": "Translation (EN-RU)", "level": 100},
        ],
        "downloads_header": "Download CV",
        "contact_header": "Contact Info"
    },
}

SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/ayanfe4luv",
    "HH.ru": "https://novosibirsk.hh.ru/resume/7f1ad8a2ff0b7437110039ed1f706d57796333",
    "GitHub": "https://github.com/Ayanfe4luv/cv_project",
}

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="CV | Ayanfeoluwa Alabetutu",
    page_icon="👨‍🏫",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- LOAD CSS ---
if css_file.exists():
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- HELPER: LANGUAGE ---
if "lang" not in st.session_state:
    st.session_state.lang = "ru"

def switch_language():
    st.session_state.lang = "en" if st.session_state.lang == "ru" else "ru"

# Top Right Language Switcher
lang_col1, lang_col2 = st.columns([8, 1])
with lang_col2:
    if st.button("🇬🇧 / 🇷🇺", help="Switch Language"):
        switch_language()
        st.rerun()

c = CONTENT[st.session_state.lang]

# --- LOAD ASSETS ---
profile_pic = None
if profile_pic_path.exists():
    profile_pic = Image.open(profile_pic_path)

# Load PDF Files
cv_ru_bytes = None
cv_en_bytes = None
try:
    with open(cv_ru_file, "rb") as f:
        cv_ru_bytes = f.read()
except FileNotFoundError:
    pass

try:
    with open(cv_en_file, "rb") as f:
        cv_en_bytes = f.read()
except FileNotFoundError:
    pass


# =================================================================
# MAIN LAYOUT: 2 COLUMNS (Left Sidebar Look | Right Main Content)
# =================================================================

col_left, col_right = st.columns([1, 2.2], gap="large")

# --- LEFT COLUMN (The "Sidebar" from the image) ---
with col_left:
    # 1. Profile Picture
    if profile_pic:
        st.markdown('<div class="profile-img-container">', unsafe_allow_html=True)
        st.image(profile_pic, width=180)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # 2. Name & Title
    st.markdown(f"<h1>{c['name']}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center; font-weight:600; color:#d33682;'>{c['title']}</p>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    # 3. Contact Info
    st.markdown(f"## {c['contact_header']}")
    st.markdown(f"""
    <div class="contact-item">
        <span class="contact-icon">📍</span> {c['location']}
    </div>
    <div class="contact-item">
        <span class="contact-icon">📧</span> {c['email']}
    </div>
    <div class="contact-item">
        <span class="contact-icon">📞</span> {c['phone']}
    </div>
    """, unsafe_allow_html=True)

    # Socials
    st.markdown("<br>", unsafe_allow_html=True)
    cols_social = st.columns(len(SOCIAL_MEDIA))
    for i, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        with cols_social[i]:
            st.markdown(f"[{platform}]({link})")
    
    # 4. Key Qualities (Bubbles)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"## {c['qualities_header']}")
    
    bubbles_html = '<div class="qualities-container">'
    for quality in c['qualities_bubbles']:
        bubbles_html += f'<div class="quality-bubble">{quality}</div>'
    bubbles_html += '</div>'
    st.markdown(bubbles_html, unsafe_allow_html=True)

    # 5. Download Buttons (Showing BOTH languages)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"## {c['downloads_header']}")
    
    dl_col1, dl_col2 = st.columns(2)
    with dl_col1:
        if cv_ru_bytes:
            st.download_button(
                label="📄 RU PDF",
                data=cv_ru_bytes,
                file_name="Alabetutu_CV_RU.pdf",
                mime="application/pdf",
                key="btn_ru"
            )
    with dl_col2:
        if cv_en_bytes:
            st.download_button(
                label="📄 EN PDF",
                data=cv_en_bytes,
                file_name="Alabetutu_CV_EN.pdf",
                mime="application/pdf",
                key="btn_en"
            )


# --- RIGHT COLUMN (Main Content from the image) ---
with col_right:
    
    # 1. Profile / About
    st.markdown(f"## {c['profile_header']}")
    st.markdown('<div class="section-line"></div>', unsafe_allow_html=True)
    st.markdown(c['description'])
    
    # 2. Skills (Progress Bars)
    st.markdown(f"## {c['skills_header']}")
    st.markdown('<div class="section-line"></div>', unsafe_allow_html=True)
    
    # Split skills into 2 small columns for better density
    s_col1, s_col2 = st.columns(2)
    for i, skill in enumerate(c['tech_skills']):
        col = s_col1 if i % 2 == 0 else s_col2
        with col:
            st.markdown(f"""
            <div class="skill-container">
                <div class="skill-label">
                    <span>{skill['name']}</span>
                </div>
                <div class="progress-bg">
                    <div class="progress-fill" style="width: {skill['level']}%;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # 3. Work Experience (Timeline)
    st.markdown(f"## {c['work_header']}")
    st.markdown('<div class="section-line"></div>', unsafe_allow_html=True)
    
    for job in c['experience']:
        st.markdown(f"""
        <div class="timeline-block">
            <div class="timeline-dot"></div>
            <span class="date-range">{job['period']}</span>
            <div class="role-title">{job['role']}</div>
            <div class="company-name">@ {job['company']}</div>
            <p>{job['desc']}</p>
        </div>
        """, unsafe_allow_html=True)

    # 4. Education
    st.markdown(f"## {c['education_header']}")
    st.markdown('<div class="section-line"></div>', unsafe_allow_html=True)
    
    for edu in c['education']:
        st.markdown(f"""
        <div class="timeline-block" style="border:none; padding-bottom:0;">
            <div class="timeline-dot" style="background:#6b7280;"></div>
            <span class="date-range" style="color:#6b7280;">{edu['year']}</span>
            <div class="role-title">{edu['degree']}</div>
            <div class="company-name">{edu['school']}</div>
        </div>
        """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("---")
st.markdown(
    "<center><p style='font-size:0.8rem; color:#aaa;'>Designed with Streamlit & CSS</p></center>", 
    unsafe_allow_html=True
)
