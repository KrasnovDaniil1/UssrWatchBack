from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import SQLAlchemyError
import logging

logger = logging.getLogger(__name__)

class NotFoundError(Exception):
    def __init__(self, detail: str):
        self.detail = detail

async def not_found_handler(request: Request, exc: NotFoundError):
    logger.warning(f"❌ NotFoundError: {exc.detail}")
    return JSONResponse(status_code=404, content={"detail": exc.detail})

async def validation_handler(request: Request, exc: RequestValidationError):
    logger.warning(f"🛑 ValidationError: {exc.errors()}")
    return JSONResponse(status_code=422, content={"detail": exc.errors()})

async def sqlalchemy_handler(request: Request, exc: SQLAlchemyError):
    logger.error(f"DB error: {exc}")
    return JSONResponse(status_code=500, content={"detail": "Ошибка с данной базой"})

async def not_know_handler(request: Request, exc: Exception):
    logger.exception(f"DB error: Не обработанная ошибка")
    return JSONResponse(status_code=500, content={"detail": "Не обработанная ошибка"})

def register_handlers(app):
    app.add_exception_handler(NotFoundError, not_found_handler)
    app.add_exception_handler(RequestValidationError, validation_handler)
    app.add_exception_handler(SQLAlchemyError, sqlalchemy_handler)
    app.add_exception_handler(Exception, not_know_handler)