from fastapi import APIRouter
from .watch import router as watch_router
from .mechanism import router as mechanism_router
from .user import router as user_router

router = APIRouter()

router.include_router(watch_router, tags=['watch'])
router.include_router(mechanism_router, tags=['mechanism'])
router.include_router(user_router, tags=['user'])

