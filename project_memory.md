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
   - Successfully imported the connection from `db.py` into `app.py`.
   - Renamed variables for better mental mapping: `table` (connection), `waiter` (cursor), and `food` (fetched data).
   - Executed our first SQL query (`SELECT * from users`) and used `.fetchall()` to retrieve the data.
5. **Version Control Setup:**
   - Overhauled `.gitignore` to prevent pushing OS/IDE junk and secrets.
   - Created a reusable `push.bat` script to automate commits and pushing to GitHub.
6. **Server Activation:**
   - Added `if __name__ == '__main__': app.run(debug=True)` to `app.py`.
   - Successfully started the development server and verified the Flask debugger is active.

7. **Build Endpoints:**
   - Imported `jsonify` to convert database tuples into JSON format.
   - Successfully created a raw API endpoint that returns data to the browser.

8. **Docker Containerization:**
   - Authored a `Dockerfile` using `python:3.10-slim`.
   - Updated `app.run(host="0.0.0.0")` in `app.py` so the container allows external traffic.
   - Cleaned up `requirements.txt` to only include `Flask` and `psycopg2-binary`.
   - Successfully built image `ebg-backend` and test-ran it — confirmed Supabase connection works from inside the container.

9. **Jenkins Pipeline:**
   - Created a `Jenkinsfile` with 3 stages: Clone Repo → Build Docker Image → Smoke Test Container.
   - Uses `bat` commands (Windows-native Jenkins).
   - Pushed to GitHub so Jenkins can read it directly from the repo.
   - *Bug Fixed:* `timeout /t 5` doesn't work in Jenkins (no stdin). Replaced with `ping -n 6 127.0.0.1 > nul`.
   - ✅ **All 3 stages passed GREEN on Jenkins!** Pipeline is fully operational.

## 🗺️ Future Roadmap (The Game Plan)
1. **AWS Deployment:** Deploy the Docker container to an AWS EC2 instance so the world can access it.
2. **GitHub Webhook:** Auto-trigger Jenkins pipeline on every `git push` (true CI/CD).
3. **Frontend:** Build a web UI that consumes our Flask JSON API.
