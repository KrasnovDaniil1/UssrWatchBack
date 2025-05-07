from fastapi import APIRouter
from watch.api import router as watch_router
from seed.api import router as seed_router

router = APIRouter()

router.include_router(watch_router, tags=['watch'])
router.include_router(seed_router, tags=['seed_data'])


