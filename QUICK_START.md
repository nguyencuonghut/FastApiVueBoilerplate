# Quick Start Guide

## 5-Minute Setup

### Option 1: Using Docker (Recommended)

```bash
# Clone/extract to your project directory
cd /run/media/cuong/DATA/02_Project/200_FastApiVueBoilerplate

# Start everything
docker-compose up --build

# Open in browser
# Frontend: http://localhost:5173
# Backend API: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

**Demo Credentials:**
- Admin: `admin` / `admin123`
- User: `user` / `user123`

---

### Option 2: Manual Setup

#### Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Initialize database (requires PostgreSQL running)
python -m app.database.init_db

# Start server
python main.py
```
Server runs at: `http://localhost:8000`

#### Frontend Setup (in new terminal)

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```
Application runs at: `http://localhost:5173`

---

## Project Overview

### What's Included?

✅ **Authentication**
- JWT token-based login
- Refresh token mechanism
- Secure password hashing

✅ **Authorization**
- Role-Based Access Control (RBAC)
- Granular permissions
- Admin vs User roles

✅ **User Management**
- Admin can create/manage users
- User profile editing
- Password change

✅ **Dashboards**
- Admin: System overview & user management
- User: Real-time monitoring screen

✅ **Professional Features**
- Input validation
- Error handling
- CORS protection
- API documentation
- Docker support

---

## First Steps

### 1. Login
Visit `http://localhost:5173` and login with demo credentials

### 2. Explore Admin Panel
If logged in as admin, go to `/admin/dashboard` to see:
- User statistics
- User management interface
- Role management

### 3. Check User Dashboard
If logged in as regular user, see:
- Real-time monitoring
- System status
- Activity log

### 4. Test API
Visit `http://localhost:8000/docs` for interactive API documentation

---

## File Structure Overview

```
📁 backend/
  ├── app/
  │   ├── api/              # API endpoints
  │   ├── models/           # Database models
  │   ├── schemas/          # Data validation
  │   ├── services/         # Business logic
  │   ├── security/         # Auth & JWT
  │   └── middleware/       # CORS, logging, etc
  └── main.py              # Entry point

📁 frontend/
  ├── src/
  │   ├── components/       # Vue components
  │   ├── views/            # Page components
  │   ├── stores/           # Pinia state
  │   ├── router/           # Vue Router config
  │   ├── services/         # API calls
  │   └── layouts/          # Layout templates
  └── package.json
```

---

## Customization Tips

### Add New API Endpoint
1. Create service in `backend/app/services/`
2. Add route in `backend/app/api/`
3. Include in `backend/app/main.py`
4. Call from frontend service

### Add New Page
1. Create component in `frontend/src/views/`
2. Add route in `frontend/src/router/index.js`
3. Link from navigation

### Database Changes
1. Modify model in `backend/app/models/`
2. Run initialization again
3. Or use Alembic migrations

---

## Common Issues

**Port already in use?**
```bash
# Change port in vite.config.js or backend config
```

**Database connection error?**
```bash
# Check PostgreSQL is running
# Update DATABASE_URL in .env
```

**CORS errors?**
```bash
# Update CORS_ORIGINS in backend .env
```

---

## Next Steps

1. ✅ Get it running
2. 📖 Read the README.md for full documentation
3. 🔧 Customize for your needs
4. 🚀 Deploy to production
5. 📚 Add more features

---

Enjoy building! 🎉
