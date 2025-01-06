from fastapi import FastAPI
from app.routes.search import router as search_router

app = FastAPI()

# Incluir rutas
app.include_router(search_router, prefix="/api/v1", tags=["Search"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
