from pydantic_settings import BaseSettings
from typing import List, Optional


class Settings(BaseSettings):
    """Application Settings"""
    
    # Database
    database_url: str = "postgresql://user:password@localhost:5432/fastapi_db"
    
    # Security
    secret_key: str = "your-secret-key-here-change-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 7
    
    # App
    app_name: str = "FastAPI Vue Boilerplate"
    app_version: str = "1.0.0"
    debug: bool = True
    
    # CORS - will parse comma-separated string into list automatically
    cors_origins: str = "http://localhost:3000,http://localhost:5173"
    
    # Email
    smtp_host: Optional[str] = None
    smtp_port: Optional[int] = None
    smtp_user: Optional[str] = None
    smtp_password: Optional[str] = None
    
    @property
    def cors_origins_list(self) -> List[str]:
        """Parse cors_origins string into list"""
        return [origin.strip() for origin in self.cors_origins.split(",")]
    
    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
