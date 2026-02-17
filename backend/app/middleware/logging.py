import logging
from typing import Callable
from fastapi import Request
from time import time

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


class LoggingMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, request: Request, call_next: Callable):
        start_time = time()
        
        # Log request
        logger.info(
            f"Request: {request.method} {request.url.path}",
            extra={
                "client": request.client,
                "method": request.method,
                "path": request.url.path
            }
        )
        
        response = await call_next(request)
        
        # Log response
        process_time = time() - start_time
        logger.info(
            f"Response: {response.status_code} - {process_time:.2f}s",
            extra={
                "status_code": response.status_code,
                "process_time": process_time
            }
        )
        
        response.headers["X-Process-Time"] = str(process_time)
        return response
