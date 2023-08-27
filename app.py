from fastapi import FastAPI
from routing.CFA import router as cfa_router

app = FastAPI(openapi_url="/core/openapi.json", docs_url="/core/docs")

app.include_router(cfa_router)