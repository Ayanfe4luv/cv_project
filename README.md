# 🌐 Двуязычное Цифровое Резюме | Bilingual Digital CV

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)

---

## 🇷🇺 Русский

### Описание

Профессиональное цифровое резюме/портфолио, созданное на Streamlit с поддержкой двух языков (русский и английский). Идеально подходит для специалистов, работающих на международном рынке.

### Возможности

- ✅ **Двуязычный интерфейс** — переключение RU/EN одной кнопкой
- ✅ **Скачивание CV** — PDF версии на обоих языках
- ✅ **Адаптивный дизайн** — отлично выглядит на всех устройствах
- ✅ **Современный UI** — профессиональный внешний вид
- ✅ **Простое развёртывание** — готов к Streamlit Cloud

### Структура проекта

```
digital-cv/
├── app.py                 # Основное приложение
├── requirements.txt       # Зависимости Python
├── Procfile              # Для развёртывания
├── .streamlit/
│   └── config.toml       # Настройки Streamlit
├── assets/
│   ├── profile-pic.png   # Фото профиля
│   ├── CV_RU.pdf         # Резюме (рус.)
│   └── CV_EN.pdf         # CV (англ.)
└── styles/
    └── main.css          # Стили CSS
```

### Установка и запуск

```bash
# Клонируйте репозиторий
git clone https://github.com/YOUR_USERNAME/digital-cv.git
cd digital-cv

# Создайте виртуальное окружение
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или venv\Scripts\activate  # Windows

# Установите зависимости
pip install -r requirements.txt

# Запустите приложение
streamlit run app.py
```

### Развёртывание на Streamlit Cloud

1. Загрузите репозиторий на GitHub
2. Перейдите на [share.streamlit.io](https://share.streamlit.io)
3. Нажмите "New app"
4. Выберите репозиторий и ветку
5. Укажите `app.py` как главный файл
6. Нажмите "Deploy"

---

## 🇬🇧 English

### Description

Professional digital CV/portfolio built with Streamlit featuring bilingual support (Russian and English). Perfect for professionals working in international markets.

### Features

- ✅ **Bilingual Interface** — RU/EN toggle with one click
- ✅ **CV Downloads** — PDF versions in both languages
- ✅ **Responsive Design** — looks great on all devices
- ✅ **Modern UI** — professional appearance
- ✅ **Easy Deployment** — Streamlit Cloud ready

### Project Structure

```
digital-cv/
├── app.py                 # Main application
├── requirements.txt       # Python dependencies
├── Procfile              # For deployment
├── .streamlit/
│   └── config.toml       # Streamlit settings
├── assets/
│   ├── profile-pic.png   # Profile photo
│   ├── CV_RU.pdf         # Resume (Russian)
│   └── CV_EN.pdf         # CV (English)
└── styles/
    └── main.css          # CSS styles
```

### Installation & Running

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/digital-cv.git
cd digital-cv

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

### Deploying to Streamlit Cloud

1. Push repository to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click "New app"
4. Select your repository and branch
5. Set `app.py` as the main file
6. Click "Deploy"

---

## 📝 Customization | Кастомизация

### Adding Your Photo | Добавление фото

Place your profile photo as `assets/profile-pic.png` (recommended size: 400x400px).

### Updating Content | Обновление контента

Edit the `CONTENT` dictionary in `app.py` to update your information in both languages.

### Changing Colors | Изменение цветов

Modify `.streamlit/config.toml` and `styles/main.css` to customize the color scheme.

---

## 👤 Author | Автор

**Ayanfeoluwa Alabetutu**
- 📧 Email: ayanfe4luv@gmail.com
- 💼 LinkedIn: [linkedin.com/in/ayanfe4luv](https://linkedin.com/in/ayanfe4luv)

---

## 📄 License | Лицензия

This project is open source and available under the [MIT License](LICENSE).

---

<p align="center">
  Made with ❤️ using Streamlit<br>
  Сделано с ❤️ на Streamlit
</p>
