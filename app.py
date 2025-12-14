"""
Bilingual Digital CV/Portfolio - Ayanfeoluwa Alabetutu
Teacher | Translator | AI Trainer
Russian (Primary) / English

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
        "page_icon": "👨‍🏫",
        "name": "Аянфеолува Алабетуту",
        "title": "Преподаватель | Переводчик | AI-специалист",
        "description": """
        Целеустремленный специалист с 9+ годами опыта в преподавании английского языка 
        и 3+ годами в переводческой деятельности. Эксперт в области AI/LLM с опытом 
        промпт-инжиниринга и создания датасетов для обучения нейросетей.
        """,
        "email": "ayanfe4luv@gmail.com",
        "phone": "+7 (987) 509-98-18",
        "location": "📍 Новосибирск, Россия",
        "download_cv": "📄 Скачать резюме (RU)",
        "download_cv_en": "📄 Download CV (EN)",
        "social_header": "Социальные сети",
        "qualifications_header": "Ключевые квалификации",
        "qualifications": [
            "✓ **Английский язык: C2 (носитель)** — подтверждён сертификатом TEFL",
            "✓ **Опыт письменного перевода: 3+ года** — EN↔RU, EN→FR",
            "✓ **Опыт работы с AI/LLM: 2+ года** — промпт-инжиниринг, датасеты",
            "✓ **Научные публикации** на русском и английском языках",
        ],
        "experience_header": "Опыт работы",
        "skills_header": "Навыки",
        "education_header": "Образование",
        "certifications_header": "Сертификаты",
        "contact_header": "Контакты",
        "ai_experience_header": "🤖 Опыт работы с AI и нейросетями",
        "translation_header": "🌐 Переводческая деятельность",
        "teaching_header": "👨‍🏫 Педагогический опыт",
        "experience": [
            {
                "company": "UREKA Biotec | Omicslogic Africa",
                "role": "AI-специалист | Разработчик контент-пайплайнов",
                "period": "2024 — настоящее время",
                "tasks": [
                    "Разработка многоступенчатых LLM-пайплайнов для генерации контента",
                    "Промпт-инжиниринг и API-оркестрация для обучения нейросетей",
                    "Создание датасетов для машинного перевода и генерации текстов",
                    "Оценка и редактирование AI-генераций — контроль качества",
                ],
            },
            {
                "company": "SKRIND Biotec (R&D)",
                "role": "Data Scientist",
                "period": "Январь 2023 — Май 2025",
                "tasks": [
                    "Построение предиктивных моделей и алгоритмов ML",
                    "Применение компьютерного зрения для анализа данных",
                    "Автоматизация процессов сбора и обработки данных",
                ],
            },
            {
                "company": "Фриланс-переводчик",
                "role": "Переводчик EN↔RU, EN→FR",
                "period": "Июнь 2022 — настоящее время",
                "tasks": [
                    "500+ страниц научных и медицинских текстов",
                    "200+ страниц технической документации (IT, Data Science)",
                    "100+ страниц образовательных материалов",
                ],
            },
        ],
        "teaching_experience": [
            {
                "school": "Школа 21, Новосибирск",
                "role": "Преподаватель английского",
                "period": "2024 — настоящее время",
            },
            {
                "school": "НГПУ",
                "role": "Преподаватель биоинформатики",
                "period": "2024 — 2025",
            },
            {
                "school": "Муниципальная школа №5",
                "role": "Преподаватель английского",
                "period": "2023 — 2024",
            },
            {
                "school": "НГУЭУ",
                "role": "Преподаватель для студентов",
                "period": "2022 — 2023",
            },
            {
                "school": "Rostum Academy, GO! English, Heathrow Schools",
                "role": "Преподаватель английского",
                "period": "2016 — 2021",
            },
        ],
        "education": [
            {
                "degree": "Кандидат наук (в процессе)",
                "school": "ФИЦ ФТМ, НИИ Вирусологии, Новосибирск",
                "year": "2027 (ожидается)",
            },
            {
                "degree": "Data Science",
                "school": "WorldQuant University, США",
                "year": "2022",
            },
            {
                "degree": "Магистр молекулярной биологии и генетики",
                "school": "Пензенский гос. университет",
                "year": "2018",
            },
            {
                "degree": "Бакалавр микробиологии",
                "school": "Университет Лагоса, Нигерия",
                "year": "2014",
            },
        ],
        "certifications": [
            "Professional TEFL Certificate (2023) — уровень C2",
            "Microsoft Certified Educator (2020)",
            "365 Data Science Program",
            "H3ABioNet Pan-African Bioinformatics Training",
        ],
        "languages": {
            "header": "Языки",
            "items": ["🇬🇧 Английский — C2 (носитель)", "🇷🇺 Русский — свободно", "🇫🇷 Французский — хороший уровень"],
        },
        "tech_skills": {
            "header": "Технические навыки",
            "items": [
                "💻 **Программирование:** Python, R, SQL, Perl, Bash",
                "🤖 **AI/ML:** LLMs, Промпт-инжиниринг, NLP, Computer Vision",
                "📊 **Инструменты:** Linux, Streamlit, Translation SDKs",
            ],
        },
        "additional_header": "Дополнительная информация",
        "additional_info": [
            "🌍 **Гражданство:** Россия и Нигерия",
            "💼 **Готовность:** Удалённая работа, гибкий график",
            "🖥️ **Оборудование:** Windows 11, интернет 100+ Мбит/с",
        ],
    },
    "en": {
        "page_title": "CV | Ayanfeoluwa Alabetutu",
        "page_icon": "👨‍🏫",
        "name": "Ayanfeoluwa Alabetutu",
        "title": "Teacher | Translator | AI Trainer",
        "description": """
        Purpose-driven professional with 9+ years of English teaching experience 
        and 3+ years in translation services. Expert in AI/LLM with hands-on experience 
        in prompt engineering and dataset creation for neural network training.
        """,
        "email": "ayanfe4luv@gmail.com",
        "phone": "+7 (987) 509-98-18",
        "location": "📍 Novosibirsk, Russia",
        "download_cv": "📄 Download CV (EN)",
        "download_cv_en": "📄 Скачать резюме (RU)",
        "social_header": "Social Media",
        "qualifications_header": "Key Qualifications",
        "qualifications": [
            "✓ **English: C2 (Native Speaker)** — TEFL Certified",
            "✓ **Translation Experience: 3+ Years** — EN↔RU, EN→FR",
            "✓ **AI/LLM Experience: 2+ Years** — Prompt Engineering, Datasets",
            "✓ **Scientific Publications** in Russian and English",
        ],
        "experience_header": "Work Experience",
        "skills_header": "Skills",
        "education_header": "Education",
        "certifications_header": "Certifications",
        "contact_header": "Contact",
        "ai_experience_header": "🤖 AI & Neural Network Experience",
        "translation_header": "🌐 Translation Experience",
        "teaching_header": "👨‍🏫 Teaching Experience",
        "experience": [
            {
                "company": "UREKA Biotec | Omicslogic Africa",
                "role": "AI Specialist | Content Pipeline Developer",
                "period": "2024 — Present",
                "tasks": [
                    "Developed multi-stage LLM pipelines for personalized content generation",
                    "Prompt engineering and API orchestration for neural network training",
                    "Dataset creation for machine translation and text generation systems",
                    "Evaluating and editing AI-generated outputs — quality control",
                ],
            },
            {
                "company": "SKRIND Biotec (R&D)",
                "role": "Data Scientist",
                "period": "January 2023 — May 2025",
                "tasks": [
                    "Built predictive models and ML algorithms",
                    "Applied computer vision for data analysis",
                    "Automated data collection and processing workflows",
                ],
            },
            {
                "company": "Freelance Translator",
                "role": "Translator EN↔RU, EN→FR",
                "period": "June 2022 — Present",
                "tasks": [
                    "500+ pages of scientific and medical texts",
                    "200+ pages of technical documentation (IT, Data Science)",
                    "100+ pages of educational materials",
                ],
            },
        ],
        "teaching_experience": [
            {
                "school": "School 21, Novosibirsk",
                "role": "English Teacher",
                "period": "2024 — Present",
            },
            {
                "school": "NSPU",
                "role": "Bioinformatics Instructor",
                "period": "2024 — 2025",
            },
            {
                "school": "Municipal School No. 5",
                "role": "English Teacher",
                "period": "2023 — 2024",
            },
            {
                "school": "NSUEM",
                "role": "English Instructor",
                "period": "2022 — 2023",
            },
            {
                "school": "Rostum Academy, GO! English, Heathrow Schools",
                "role": "English Teacher",
                "period": "2016 — 2021",
            },
        ],
        "education": [
            {
                "degree": "Ph.D. Candidate (In Progress)",
                "school": "FRC FTM, Institute of Virology, Novosibirsk",
                "year": "Expected 2027",
            },
            {
                "degree": "Data Science",
                "school": "WorldQuant University, USA",
                "year": "2022",
            },
            {
                "degree": "M.Sc. in Molecular Biology and Genetics",
                "school": "Penza State University",
                "year": "2018",
            },
            {
                "degree": "B.Sc. in Microbiology",
                "school": "University of Lagos, Nigeria",
                "year": "2014",
            },
        ],
        "certifications": [
            "Professional TEFL Certificate (2023) — C2 proficiency",
            "Microsoft Certified Educator (2020)",
            "365 Data Science Program",
            "H3ABioNet Pan-African Bioinformatics Training",
        ],
        "languages": {
            "header": "Languages",
            "items": ["🇬🇧 English — C2 (Native)", "🇷🇺 Russian — Fluent", "🇫🇷 French — Proficient"],
        },
        "tech_skills": {
            "header": "Technical Skills",
            "items": [
                "💻 **Programming:** Python, R, SQL, Perl, Bash",
                "🤖 **AI/ML:** LLMs, Prompt Engineering, NLP, Computer Vision",
                "📊 **Tools:** Linux, Streamlit, Translation SDKs",
            ],
        },
        "additional_header": "Additional Information",
        "additional_info": [
            "🌍 **Citizenship:** Russia & Nigeria",
            "💼 **Availability:** Remote work, flexible schedule",
            "🖥️ **Equipment:** Windows 11, 100+ Mbps internet",
        ],
    },
}

SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/ayanfe4luv",
    "HH.ru": "https://novosibirsk.hh.ru/resume/7f1ad8a2ff0b7437110039ed1f706d57796333",
    "GitHub": "https://github.com",
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

# --- LANGUAGE SELECTION ---
if "lang" not in st.session_state:
    st.session_state.lang = "ru"  # Default to Russian


def switch_language():
    st.session_state.lang = "en" if st.session_state.lang == "ru" else "ru"


# --- LANGUAGE SWITCHER IN TOP RIGHT ---
col_spacer, col_lang = st.columns([6, 1])
with col_lang:
    current_lang = st.session_state.lang
    lang_label = "🇬🇧 EN" if current_lang == "ru" else "🇷🇺 RU"
    if st.button(lang_label, key="lang_switch", help="Switch language / Переключить язык"):
        switch_language()
        st.rerun()

# Get current language content
lang = st.session_state.lang
content = CONTENT[lang]

# --- LOAD CV FILES ---
try:
    with open(cv_ru_file, "rb") as f:
        cv_ru_bytes = f.read()
except FileNotFoundError:
    cv_ru_bytes = None

try:
    with open(cv_en_file, "rb") as f:
        cv_en_bytes = f.read()
except FileNotFoundError:
    cv_en_bytes = None

# --- LOAD PROFILE IMAGE ---
profile_pic = None
if profile_pic_path.exists():
    try:
        profile_pic = Image.open(profile_pic_path)
    except Exception:
        profile_pic = None

# --- HERO SECTION ---
st.markdown('<div class="hero-section">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 2], gap="large")

with col1:
    if profile_pic:
        st.image(profile_pic, width=250)
    else:
        st.markdown(
            """
            <div style="width:200px;height:200px;background:linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius:50%;display:flex;align-items:center;justify-content:center;margin:auto;">
            <span style="font-size:80px;">👨‍🏫</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

with col2:
    st.markdown(f"# {content['name']}")
    st.markdown(f"### {content['title']}")
    st.markdown(content["description"])

    # Contact info
    st.markdown(f"📧 {content['email']} &nbsp;&nbsp; 📞 {content['phone']}")
    st.markdown(content["location"])

    # Download buttons
    btn_col1, btn_col2, btn_col3 = st.columns(3)
    with btn_col1:
        if cv_ru_bytes:
            st.download_button(
                label="📄 CV (RU)",
                data=cv_ru_bytes,
                file_name="Alabetutu_CV_RU.pdf",
                mime="application/pdf",
                key="dl_ru",
            )
    with btn_col2:
        if cv_en_bytes:
            st.download_button(
                label="📄 CV (EN)",
                data=cv_en_bytes,
                file_name="Alabetutu_CV_EN.pdf",
                mime="application/pdf",
                key="dl_en",
            )

st.markdown("</div>", unsafe_allow_html=True)

# --- SOCIAL LINKS ---
st.markdown("---")
cols = st.columns(len(SOCIAL_MEDIA))
for idx, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    with cols[idx]:
        st.markdown(f"[🔗 {platform}]({link})")

# --- KEY QUALIFICATIONS ---
st.markdown("---")
st.markdown(f"## {content['qualifications_header']}")
qual_cols = st.columns(2)
for idx, qual in enumerate(content["qualifications"]):
    with qual_cols[idx % 2]:
        st.markdown(qual)

# --- AI/ML EXPERIENCE ---
st.markdown("---")
st.markdown(f"## {content['ai_experience_header']}")

for exp in content["experience"][:2]:  # First 2 are AI-related
    with st.container():
        st.markdown(f"### {exp['company']}")
        st.markdown(f"**{exp['role']}** | *{exp['period']}*")
        for task in exp["tasks"]:
            st.markdown(f"- {task}")
        st.markdown("")

# --- TRANSLATION EXPERIENCE ---
st.markdown("---")
st.markdown(f"## {content['translation_header']}")

exp = content["experience"][2]  # Translation experience
st.markdown(f"### {exp['company']}")
st.markdown(f"**{exp['role']}** | *{exp['period']}*")

volume_header = "Объём выполненных работ:" if lang == "ru" else "Volume of Work Completed:"
st.markdown(f"**{volume_header}**")
for task in exp["tasks"]:
    st.markdown(f"- {task}")

# --- TEACHING EXPERIENCE ---
st.markdown("---")
st.markdown(f"## {content['teaching_header']}")

years_text = "9+ лет опыта" if lang == "ru" else "9+ years of experience"
st.markdown(f"*{years_text}*")

for teaching in content["teaching_experience"]:
    col_t1, col_t2 = st.columns([3, 1])
    with col_t1:
        st.markdown(f"**{teaching['school']}** — {teaching['role']}")
    with col_t2:
        st.markdown(f"*{teaching['period']}*")

# --- EDUCATION ---
st.markdown("---")
st.markdown(f"## {content['education_header']}")

for edu in content["education"]:
    col_e1, col_e2 = st.columns([3, 1])
    with col_e1:
        st.markdown(f"**{edu['degree']}**")
        st.markdown(f"*{edu['school']}*")
    with col_e2:
        st.markdown(f"**{edu['year']}**")
    st.markdown("")

# --- SKILLS ---
st.markdown("---")
st.markdown(f"## {content['skills_header']}")

skill_col1, skill_col2 = st.columns(2)

with skill_col1:
    st.markdown(f"### {content['languages']['header']}")
    for item in content["languages"]["items"]:
        st.markdown(f"- {item}")

with skill_col2:
    st.markdown(f"### {content['tech_skills']['header']}")
    for item in content["tech_skills"]["items"]:
        st.markdown(item)

# --- CERTIFICATIONS ---
st.markdown("---")
st.markdown(f"## {content['certifications_header']}")

cert_cols = st.columns(2)
for idx, cert in enumerate(content["certifications"]):
    with cert_cols[idx % 2]:
        st.markdown(f"🏆 {cert}")

# --- ADDITIONAL INFO ---
st.markdown("---")
st.markdown(f"## {content['additional_header']}")

for info in content["additional_info"]:
    st.markdown(info)

# --- FOOTER ---
st.markdown("---")
footer_text = (
    "© 2024 Ayanfeoluwa Alabetutu | Сделано с ❤️ на Streamlit"
    if lang == "ru"
    else "© 2024 Ayanfeoluwa Alabetutu | Made with ❤️ using Streamlit"
)
st.markdown(f"<p style='text-align: center; color: #888;'>{footer_text}</p>", unsafe_allow_html=True)
