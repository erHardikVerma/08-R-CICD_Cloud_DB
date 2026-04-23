@echo off
echo =========================================
echo 🚀 Pushing Code to GitHub...
echo =========================================

git init
git remote remove origin 2>nul
git remote add origin https://github.com/erHardikVerma/08-R-CICD_Cloud_DB.git
git add .
git commit -m "Auto-commit: Saved project memory and backend logic"
git branch -M main
git push -u origin main

echo =========================================
echo ✅ Push Complete!
echo =========================================
