#!/bin/bash

# FastAPI Vue Boilerplate Startup Script

echo "🚀 Starting FastAPI Vue Boilerplate..."

# Backend setup
echo "📦 Setting up backend..."
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m app.database.init_db

# Run backend in background
echo "🔧 Starting FastAPI server..."
python main.py &
BACKEND_PID=$!

# Frontend setup
echo "📦 Setting up frontend..."
cd ../frontend
npm install
npm run dev &
FRONTEND_PID=$!

echo "✅ Application started!"
echo "Backend: http://localhost:8000"
echo "Frontend: http://localhost:5173"
echo ""
echo "Demo Credentials:"
echo "  Admin: admin / admin123"
echo "  User: user / user123"

# Keep script running
wait
