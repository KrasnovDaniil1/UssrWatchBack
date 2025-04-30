from fastapi import APIRouter
from watch.api import router as watch_router
from mechanism.api import router as mechanism_router
from user.api import router as user_router
from draft.api import router as draft_router
from seed.api import router as seed_router

router = APIRouter()

router.include_router(watch_router, tags=['watch'])
router.include_router(mechanism_router, tags=['mechanism'])
router.include_router(user_router, tags=['user'])
router.include_router(draft_router, tags=['draft'])
router.include_router(seed_router, tags=['seed_data'])


