import sys

from fastapi import FastAPI
from loguru import logger

from configs.Environment import get_environment_variables
from routing.v1.CFA import router as cfa_router
from routing.v1.Company import router as company_router
from routing.v1.PaymentMethod import router as payment_router

app = FastAPI(openapi_url="/core/openapi.json", docs_url="/core/docs")

env = get_environment_variables()

if not env.DEBUG:
    logger.remove()
    logger.add(sys.stdout, level="INFO")

app.include_router(cfa_router)
app.include_router(company_router)
app.include_router(payment_router)