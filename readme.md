# R-CICD Cloud Database Project

This project demonstrates a complete, modern web architecture with CI/CD integration, moving from a local desktop architecture to a fully deployed cloud-based web application.

## 🏗️ Architecture Stack
- **Frontend:** Vanilla HTML, CSS, JavaScript (Deployed on Vercel)
- **Backend:** Python Flask + Gunicorn (Containerized with Docker, Deployed on Render)
- **Database:** Supabase (PostgreSQL Cloud DB)
- **CI/CD:** Jenkins (Automated Docker builds and smoke tests triggered by GitHub webhooks)

## 🌍 Important Links
- **GitHub Repository:** [https://github.com/erHardikVerma/08-R-CICD_Cloud_DB](https://github.com/erHardikVerma/08-R-CICD_Cloud_DB)
- **Backend API:** [https://ebg-backend.onrender.com](https://ebg-backend.onrender.com)
- **Frontend App:** [https://cicd-cloud.vercel.app](https://cicd-cloud.vercel.app)

## 🚀 Features
- Complete CRUD API via Flask.
- Responsive, modern frontend UI consuming the backend JSON API.
- Fully dockerized backend for environment consistency.
- Jenkins pipeline with three stages: Clone Repo → Build Docker Image → Smoke Test Container.
- Production-ready `gunicorn` deployment on Render.

## 🛠️ Local Development

### Backend Setup
1. Clone the repository.
2. Install Python dependencies: `pip install -r requirements.txt`
3. Set your Supabase connection strings as environment variables.
4. Run the Flask server: `python app.py`

### Docker Build
```bash
docker build -t ebg-backend .
docker run -p 5000:5000 ebg-backend
```
