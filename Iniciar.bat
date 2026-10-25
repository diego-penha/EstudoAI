@echo off

start powershell -NoExit -Command "cd E:\StudyAI\backend; .\venv\Scripts\Activate.ps1; uvicorn app.main:app --reload"

timeout /t 3 >nul

start powershell -NoExit -Command "cd E:\StudyAI\frontend; npm run dev"