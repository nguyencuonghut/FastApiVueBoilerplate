"""Main FastAPI application with full integration"""
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.config.settings import settings
from app.middleware.cors import add_cors_middleware
from app.middleware.exception_handlers import setup_exception_handlers
from app.middleware.openapi import setup_openapi_schema
from app.database.database import engine, Base
from app.api import auth, users, admin, dashboard, health

# Create tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Professional FastAPI + Vue 3 boilerplate with RBAC",
    debug=settings.debug
)

# Setup middleware and handlers
add_cors_middleware(app)
setup_exception_handlers(app)
setup_openapi_schema(app)

# Include routers
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(admin.router)
app.include_router(dashboard.router)
app.include_router(health.router)


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to FastAPI Vue Boilerplate",
        "version": settings.app_version,
        "docs": "/docs"
    }


@app.get("/api/info")
async def api_info():
    """Get API information"""
    return {
        "name": settings.app_name,
        "version": settings.app_version,
        "debug": settings.debug,
        "endpoints": {
            "auth": "/auth",
            "users": "/users",
            "admin": "/admin",
            "dashboard": "/dashboard",
            "health": "/health"
        }
    }
