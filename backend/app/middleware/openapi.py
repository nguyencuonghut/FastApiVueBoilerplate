from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi


def setup_openapi_schema(app: FastAPI):
    """Setup OpenAPI/Swagger documentation"""
    
    def custom_openapi():
        if app.openapi_schema:
            return app.openapi_schema
        
        openapi_schema = get_openapi(
            title="FastAPI Vue Boilerplate API",
            version="1.0.0",
            description="Professional API with RBAC authentication",
            routes=app.routes,
        )
        
        # Add security scheme
        openapi_schema["components"]["securitySchemes"] = {
            "Bearer": {
                "type": "http",
                "scheme": "bearer",
                "bearerFormat": "JWT",
            }
        }
        
        app.openapi_schema = openapi_schema
        return app.openapi_schema
    
    app.openapi = custom_openapi
