# app/main.py
from fastapi import FastAPI
from .routes import items
from .utils.exceptions import add_exception_handlers

# Create FastAPI application
app = FastAPI(
    title="Enhanced FastAPI Example",
    description="A more structured FastAPI application with proper models and error handling",
    version="0.2.0"
)

# Add routes
app.include_router(items.router)

# Configure exception handlers
add_exception_handlers(app)

# Root endpoint
@app.get("/", tags=["root"])
async def root():
    """API root endpoint"""
    return {
        "message": "Welcome to the enhanced FastAPI example",
        "docs": "/docs",
        "endpoints": {
            "items": "/items"
        }
    }