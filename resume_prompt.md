# 🪄 Resume Prompt — Copy-Paste This Into Any New Chat

> Hey, I'm building a Flask + Supabase backend project with Docker and Jenkins CI/CD.
>
> Please read these 2 files from my project folder to load your persona and full project context:
> 1. `project_memory.md` — Contains the architecture stack, full journey, all achievements, and future roadmap.
> 2. `reference_memory.md` — Contains your persona rules (Senior Backend Mentor), teaching style, and Antigravity execution mode.
>
> **Current Status:** Docker container `ebg-backend` has been successfully built. The Flask API is live and returns JSON data from a Supabase PostgreSQL cloud database.
>
> **What's Next on the Roadmap:**
> 1. *(Optional)* Test the Docker container locally with `docker run`.
> 2. Set up a Jenkins pipeline to automate builds.
> 3. Deploy to AWS EC2.
>
> Let's resume from where we left off!

---

## 📂 Key Files In This Project

| File | Purpose |
|---|---|
| `app.py` | Flask server — connects to Supabase, fetches data, returns JSON via API |
| `db.py` | Database connection logic — uses `psycopg2` to connect to Supabase Session Pooler |
| `Dockerfile` | Docker instruction manual — packages the app into a portable container |
| `requirements.txt` | Only 2 dependencies: `Flask` and `psycopg2-binary` |
| `push.bat` | One-click script to commit and push everything to GitHub |
| `project_memory.md` | Full project history, decisions, and roadmap |
| `reference_memory.md` | Mentor persona rules and teaching methodology |

## 🔑 Important Details To Remember
- **Supabase Table Name:** `EBG` (capital letters — must use double quotes in SQL: `"EBG"`)
- **Supabase Connection:** Uses **Session Pooler** URL (not direct) to bypass IPv4/IPv6 issues
- **Docker Image Name:** `ebg-backend`
- **GitHub Repo:** `https://github.com/erHardikVerma/08-R-CICD_Cloud_DB.git`
- **Branch:** `main`
- **Flask runs on:** `host="0.0.0.0"`, `port=5000`
- **Cursor uses `RealDictCursor`** from `psycopg2.extras` for labeled JSON output
