import sys

from fastapi import FastAPI
from loguru import logger
from starlette.middleware.cors import CORSMiddleware

from configs.Environment import get_environment_variables
from routing.v1.CFA import router as cfa_router
from routing.v1.User import router as user_router
from routing.v1.Company import router as company_router
from routing.v1.PaymentMethod import router as payment_router
from routing.v1.History import router as history_router

app = FastAPI(openapi_url="/core/openapi.json", docs_url="/core/docs")

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


env = get_environment_variables()

if not env.DEBUG:
    logger.remove()
    logger.add(sys.stdout, level="INFO")

app.include_router(cfa_router)
app.include_router(user_router)
app.include_router(company_router)
app.include_router(payment_router)
app.include_router(history_router)
