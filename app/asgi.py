from fastapi import APIRouter, FastAPI

from app.views import router as common_router

__all__ = [
    'app',
]


def get_router() -> APIRouter:
    router = APIRouter()
    router.include_router(common_router)

    return router


def create_app() -> FastAPI:
    app_instance = FastAPI()
    app_instance.include_router(get_router())

    return app_instance


app = create_app()
