# Project Architecture & Progress Memory

## 🏗️ Architecture Stack
- **Backend:** Python Flask
- **Database:** Supabase (PostgreSQL Cloud DB)
- **Deployment (Future):** Docker, AWS EC2
- **CI/CD (Future):** Jenkins triggered by GitHub Webhook

## 📖 The Journey (How We Got Here)
- **Initial Phase:** Started with a Python Tkinter desktop UI connected to a local MySQL database via phpMyAdmin.
- **The Problem:** Tkinter is a desktop-only framework, making web deployment impossible. Furthermore, a local database isn't accessible from the cloud.
- **The Pivot:** Dropped Tkinter/MySQL and migrated to a modern web architecture (Flask backend + Supabase PostgreSQL cloud database) to allow for real web deployment, scalability, and CI/CD integration.
- **Why Supabase over Firebase?** Firebase is NoSQL and has poor joins, making it bad for structured systems. Supabase is structured PostgreSQL, which is much better for future dashboards and complex reporting.
- **Why Flask over FastAPI?** Not because Flask is "better", but because it provides a lower cognitive load and easier debugging for a beginner. This is crucial when simultaneously learning complex CI/CD, Docker, AWS, and Cloud databases.

## ✅ What We Have Achieved So Far
1. **Database Setup:** 
   - Created a Supabase project and a PostgreSQL database.
   - Created the `users` table.
2. **Environment Setup:** 
   - Installed `Flask` and `psycopg2-binary` (the Postgres adapter for Python).
   - Saved dependencies in `requirements.txt`.
3. **Database Connection (`db.py`):**
   - Wrote the connection logic.
   - *Challenge Overcome:* Ran into an IPv4/IPv6 networking error where the local machine couldn't see Supabase's direct URL.
   - *Solution:* Switched to Supabase's **Session Pooler** URL, successfully bypassing the issue and establishing a stable connection.
4. **Server Integration (`app.py`):**
   - Successfully imported the `conn` variable from `db.py` into `app.py`.
   - Created our first **Cursor** (the "waiter" that carries SQL queries).
   - Executed our first SQL query (`SELECT * from users`).

## 🗺️ Future Roadmap (The Game Plan)
1. **Level Up Python:** Learn to fetch and print the database data.
2. **Build Endpoints:** Convert that data into JSON so it acts as a real API.
3. **Containerization:** Wrap the Flask app in Docker so it can run anywhere.
4. **Automation:** Set up a Jenkins pipeline to automatically test and build our code.
5. **Deployment:** Deploy the Docker container to an AWS EC2 instance so the world can access it.
