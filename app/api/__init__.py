from fastapi import APIRouter
from api.watch import router as watch_router
from api.mechanism import router as mechanism_router
from api.user import router as user_router
from api.draft import router as draft_router

from api.seed_data import router as other_router

router = APIRouter()

router.include_router(watch_router, tags=['watch'])
router.include_router(mechanism_router, tags=['mechanism'])
router.include_router(user_router, tags=['user'])
router.include_router(draft_router, tags=['draft'])
router.include_router(other_router, tags=['seed_data'])



