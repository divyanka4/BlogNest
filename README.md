# BlogNest

**BlogNest** is a modern Django-powered blogging web app where you can read, write, and share personal stories, connect with others, and enjoy interactive features like social sharing, newsletter subscriptions, and user profiles.

## 🚀 Features

- Clean, responsive UI (Bootstrap 5, Font Awesome)
- User registration, login, and profile update
- Create, edit, and delete blog posts (only by post author)
- Social share buttons for Twitter, Facebook, LinkedIn
- Email subscription with confirmation via Gmail SMTP
- Contact form: send messages, viewed in Django admin
- Admin dashboard for full content control
- Open Graph meta tags for better link sharing

## 🛠️ Getting Started (Development)

### 1. Clone the repo

```bash
git clone https://github.com/YOUR-USERNAME/BlogNest.git
cd BlogNest
```

### 2. Create virtual environment and install requirements

```bash
python -m venv venv
source venv/bin/activate          # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Database Migrations

```bash
python manage.py migrate
```

### 4. Create Superuser

```bash
python manage.py createsuperuser
```

### 5. Configure `.env` or `settings.py`

Set your secret key and email/Social Auth settings in a `.env` file or directly in `settings.py`.  
**SMTP example for Gmail:**
```
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL=your-email@gmail.com
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view it in your browser.

## 🌐 Deployment

1. Push your project to [GitHub](https://github.com/).
2. Use a cloud provider ([Render](https://render.com/), [Railway](https://railway.app/), [Heroku](https://heroku.com/), etc.) and connect your repo.
3. Add environment variables required for Django, DB, and SMTP.
4. Deploy and visit your live site!

## 📁 Project Structure

```
BlogNest/
  ├── blog/                 # Django app (models, views, urls, templates)
  ├── BlogNest/             # Project settings
  ├── static/               # Static files (CSS, JS, images)
  ├── templates/            # Global HTML templates
  ├── manage.py
  ├── requirements.txt
  ├── .gitignore
  └── README.md
```

## 💌 Contact & Support

- For issues or feature requests, open a GitHub issue.
- Email: divi44246@gmail.com
- Connect: [LinkedIn](https://www.linkedin.com/in/divya-pal22/) | [X (Twitter)](https://x.com/_divi_xoxo)

## 🙏 Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Bootstrap 5](https://getbootstrap.com/)
- [Font Awesome](https://fontawesome.com/)
