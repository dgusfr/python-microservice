from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager

from app.checkout.router import router as checkout_router
from app.client_manager import client_manager
from app.config import APP_HOST, APP_PORT, PAYMENT_SERVICE_URL
from app.infra.database import create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application lifespan events"""
    # Startup: Create database tables
    await create_tables()
    await client_manager.startup()
    yield
    await client_manager.shutdown()


app = FastAPI(title="Checkout Commerce", version="0.1.0", lifespan=lifespan)

app.include_router(checkout_router)


@app.get("/health")
async def health_check():
    return {"status": PAYMENT_SERVICE_URL}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=APP_HOST, port=APP_PORT)
