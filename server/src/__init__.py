import functools as ft

from fastapi import HTTPException
from fastapi.exceptions import RequestValidationError

from src import exception_handlers, utils
from src.application import Application
from src.exceptions import HandlerException
from src.file_cache import StaticFilesCache
from src.repositories.motorclient import MotorClient


async def _on_app_start(app: Application):
    app.state.mongo = MotorClient(app.config.mongo_con_str)
    app.state.static_files_cache = StaticFilesCache()


def create_app():
    app = Application(
        redoc_url=None,
        docs_url=None,
        openapi_url=None,
        swagger_ui_oauth2_redirect_url=None,
    )

    app.add_exception_handler(HTTPException, exception_handlers.handle_http_exception)
    app.add_exception_handler(RequestValidationError, exception_handlers.handle_validation_exception)
    app.add_exception_handler(HandlerException, exception_handlers.handle_handler_exception)

    app.add_event_handler("startup", ft.partial(_on_app_start, app))

    return app
