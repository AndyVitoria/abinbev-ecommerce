from fastapi import FastAPI
import uvicorn

from src.routes.health import health_router


app = FastAPI()

app.include_router(health_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)