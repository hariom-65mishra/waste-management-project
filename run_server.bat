@echo off
title CleanCity - Waste Management System Server
cd /d "%~dp0"
echo ========================================================
echo   Starting CleanCity Waste Management System
echo   Designed & Developed by Hariom Mishra
echo ========================================================
echo.
echo Opening server at http://127.0.0.1:8000/
echo Admin Login: http://127.0.0.1:8000/admin/
echo Username: hariomtnr@gmail.com
echo Password: hari@123
echo.
echo Press Ctrl+C in this window anytime to stop the server.
echo.

python manage.py runserver 127.0.0.1:8000
pause
