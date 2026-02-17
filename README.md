# FastAPI Vue Boilerplate

A professional, full-stack boilerplate with **FastAPI backend**, **Vue 3 frontend**, **PostgreSQL database**, and **RBAC authentication**.

## Features

### ✨ Core Features
- ✅ **JWT-based Authentication** - Secure token-based auth with refresh tokens
- ✅ **RBAC System** - Role-Based Access Control with granular permissions
- ✅ **Admin Dashboard** - Modern admin interface with SakaiVue inspired design
- ✅ **User Dashboard** - Real-time monitoring screen for regular users
- ✅ **User Management** - Admin can create, update, and manage users
- ✅ **Role Management** - Define roles and assign permissions
- ✅ **Responsive UI** - Mobile-first design with PrimeVue components

### 🎨 Professional Features
- 📊 **Real-time Dashboards** - Live statistics and monitoring
- 🔐 **Password Security** - Bcrypt hashing with salt
- 🛡️ **CORS Protection** - Configurable CORS middleware
- 📝 **Input Validation** - Pydantic schemas for data validation
- 🚀 **Docker Support** - Complete Docker & Docker Compose setup
- 📦 **Database Migrations** - SQLAlchemy ORM with proper models
- 🎬 **Professional Layout** - Reusable admin and auth layouts

### 🔧 Technical Stack

**Backend:**
- FastAPI 0.104+
- SQLAlchemy 2.0
- PostgreSQL 15
- JWT Authentication
- Pydantic

**Frontend:**
- Vue 3 (Composition API)
- Vue Router 4
- Pinia (State Management)
- PrimeVue v4 (UI Components)
- Axios (HTTP Client)
- Vite (Build Tool)

## Quick Start

### Prerequisites
- Python 3.11+
- Node.js 20+
- PostgreSQL 15+
- Docker & Docker Compose (optional)

### 1. Clone & Setup Backend

```bash
cd backend
cp .env.example .env
pip install -r requirements.txt
python -m app.database.init_db  # Initialize database
python main.py
```

Backend will run at `http://localhost:8000`

### 2. Setup Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend will run at `http://localhost:5173`

### 3. Demo Login Credentials

After initialization, use:
- **Admin**: `admin` / `admin123`
- **User**: `user` / `user123`

## Docker Setup

```bash
docker-compose up --build
```

All services will start:
- Backend: http://localhost:8000
- Frontend: http://localhost:5173
- PostgreSQL: localhost:5432

## Project Structure

```
fastapi-vue-boilerplate/
├── backend/
│   ├── app/
│   │   ├── api/              # API routes
│   │   ├── models/           # SQLAlchemy models
│   │   ├── schemas/          # Pydantic schemas
│   │   ├── services/         # Business logic
│   │   ├── security/         # Auth & JWT
│   │   ├── middleware/       # CORS, etc
│   │   ├── database/         # DB setup
│   │   └── config/           # Configuration
│   ├── main.py              # Entry point
│   ├── requirements.txt
│   ├── .env.example
│   └── Dockerfile
│
├── frontend/
│   ├── src/
│   │   ├── components/       # Reusable components
│   │   ├── views/            # Page views
│   │   ├── layouts/          # Layout templates
│   │   ├── stores/           # Pinia stores
│   │   ├── services/         # API services
│   │   ├── router/           # Vue Router
│   │   └── utils/            # Utilities
│   ├── public/
│   ├── package.json
│   ├── vite.config.js
│   └── index.html
│
└── docker-compose.yml
```

## API Endpoints

### Authentication
- `POST /auth/login` - User login
- `POST /auth/refresh` - Refresh token

### Users
- `GET /users/me` - Get current user
- `PUT /users/me` - Update profile
- `POST /users/change-password` - Change password

### Admin
- `GET /admin/users` - List users
- `POST /admin/users` - Create user
- `DELETE /admin/users/{id}` - Deactivate user
- `GET /admin/roles` - List roles
- `GET /admin/permissions` - List permissions

## Security Best Practices

1. **Environment Variables** - Store secrets in `.env` (never commit)
2. **Password Hashing** - Uses bcrypt with salt
3. **JWT Tokens** - Short-lived access tokens (30 min) + refresh tokens
4. **CORS** - Configured for specific origins
5. **Input Validation** - All inputs validated with Pydantic
6. **SQL Injection Prevention** - Using SQLAlchemy ORM

## Database Schema

Key tables:
- `users` - User accounts with role assignment
- `roles` - RBAC roles (admin, user, etc.)
- `permissions` - Fine-grained permissions
- `role_permissions` - Role-permission mapping

## Frontend Routes

- `/login` - Authentication page
- `/dashboard` - User dashboard (realtime monitoring)
- `/admin/dashboard` - Admin overview
- `/admin/users` - User management
- `/admin/roles` - Role management

## Customization Ideas

### Add Email Notifications
- Password reset via email
- User registration confirmation
- Admin alerts

### Enhanced Logging
- Request/response logging
- Audit trail for admin actions
- Error tracking with Sentry

### Advanced Features
- Two-factor authentication (2FA)
- OAuth2 integration (Google, GitHub)
- API rate limiting
- Webhook support

### UI Enhancements
- Dark mode toggle
- Internationalization (i18n)
- Advanced charts and analytics
- File upload management

## Troubleshooting

### Database Connection Error
```bash
# Check PostgreSQL is running
psql -U user -d fastapi_db -c "SELECT 1"

# Reset database
python -m app.database.init_db
```

### CORS Issues
- Update `CORS_ORIGINS` in backend `.env`
- Frontend must match backend configuration

### Frontend Can't Connect to Backend
- Check backend is running at `http://localhost:8000`
- Update `API_BASE_URL` in `frontend/src/services/api.js`

## Performance Optimization

- Database connection pooling
- JWT caching strategies
- Frontend code splitting
- Asset compression
- CDN ready

## License

MIT

## Support

For issues and questions, create an issue in the repository.

---

**Happy coding! 🎉**
