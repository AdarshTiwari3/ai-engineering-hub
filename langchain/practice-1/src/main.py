import logging
from fastapi import FastAPI

from api.routes import router


logging.basicConfig(level=logging.INFO)

app = FastAPI(title="Local LLaMA API", version="1.0.0", docs_url="/docs")
app.include_router(router)
