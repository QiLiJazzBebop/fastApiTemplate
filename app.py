from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

from route.crudTest import crudTestRoute


def create_app():
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=['*'],
            allow_credentials=True,
            allow_methods=['*'],
            allow_headers=['*']
        )
    ]
    # Reference Website: https://www.gormanalysis.com/blog/building-a-simple-crud-application-with-fastapi/
    # SQL CRUD Operation: https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_quick_guide.htm

    tags_metadata = [
        {"name": "CRUD Template", "description": "Test Function",
         "name": "Entry Point", "description": "Welcome"}
    ]

    app = FastAPI(middleware=middleware, openapi_tags=tags_metadata)

    app.include_router(crudTestRoute)

    return app


