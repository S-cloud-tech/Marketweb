# Marketweb

**Marketweb** is a full-stack **e-commerce web application** built using **Python (Django)**. It provides core shopping functionality including product listings, user accounts, dashboard, media handling, and blog features. :contentReference[oaicite:0]{index=0}

## 🧱 Project Structure

The repository includes the following major components: :contentReference[oaicite:1]{index=1}
- `blog/` — Blog posts & CMS-style content  
- `core/` — Core configuration, settings, and utilities  
- `dashboard/` — Admin or seller dashboard features  
- `item/` — Product & catalog management  
- `media/` — Media uploads and storage support  
- `puddle/` — cart, orders or miscellaneous features  
- `users/` — Authentication, profiles, user data  
- `static/` & `templates/` — Frontend assets and HTML templates  
- Dev & deployment config: `Dockerfile`, `docker-compose.yml`, `nginx.conf`, etc. :contentReference[oaicite:2]{index=2}

---

## 🚀 Features

✔ E-commerce product catalog  
✔ User authentication and user accounts  
✔ Admin dashboard for content & product management  
✔ Media upload support  
✔ Docker-ready deployment setup  
✔ NGINX + Docker configuration for production use :contentReference[oaicite:3]{index=3}

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python, Django |
| Frontend | HTML, CSS (templates) |
| Deployment | Docker, NGINX |
| Dependencies | Listed in `requirements.txt` | :contentReference[oaicite:4]{index=4}

---

## 📦 Requirements

Before running the project locally, make sure you have:  
✔ Python 3.x  
✔ Docker & Docker Compose (optional but recommended)  
✔ Git

---

## ⚙️ Setup & Installation

### Clone the repo
```sh
git clone https://github.com/S-cloud-tech/Marketweb.git
cd Marketweb

### Using Docker
```sh
docker compose up --build

### Local development (without Docker)
1. Create & activate a virtual environment:
```sh
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

2. Install dependencies
```sh
pip install -r requirements.txt

3. Create .env config from example:
```sh
cp .env.example .env

4. Apply database migration
```sh
python manage.py migrate

5. Run development server
```sh
python manage.py runserver


## 📁 Environment Variables
See .env.example for configuration. Typical settings include database credentials secret keys, and debug flags.

## 📫 Get in Touch
If you want to contribute or report issues:
https://github.com/S-cloud-tech/Marketweb

## ❤️ Support
If you found this project useful or want more features, please ⭐ the repo!

