# 1. Choose the base computer (A tiny Linux machine with Python pre-installed)
FROM python:3.10-slim

# 2. Create a folder inside this new computer called /app
WORKDIR /app

# 3. Copy our requirements file into the folder
COPY requirements.txt .

# 4. Install all the plugins (Flask, psycopg2) inside the container
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy all the rest of our files (app.py, db.py) into the container
COPY . .

# 6. Expose the port so traffic can come in
EXPOSE 5000

# 7. The command to turn the server on when the box starts
CMD ["python", "app.py"]
