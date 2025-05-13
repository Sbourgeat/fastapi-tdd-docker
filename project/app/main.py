# project/app/main.py 

import logging
from mimetypes import init

from fastapi import FastAPI  

from app.api import ping 
from app.db import init_db

log = logging.getLogger("uvicorn")

def create_application() -> FastAPI:
    app  = FastAPI()
    app.include_router(ping.router)
    return app

    app.include_router(ping.router)

    return app 


app = create_application()

init_db(app)