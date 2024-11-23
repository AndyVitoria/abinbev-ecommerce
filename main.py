from fastapi import FastAPI
import uvicorn

from src.routes.health import health_router
from src.routes.v1.clients import client_router


app = FastAPI()

app.include_router(health_router)
app.include_router(client_router, prefix="/v1")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)