from fastapi import FastAPI
from routing.v1.CFA import router as cfa_router
from routing.v1.Company import router as company_router

app = FastAPI(openapi_url="/core/openapi.json", docs_url="/core/docs")

app.include_router(cfa_router)
app.include_router(company_router)