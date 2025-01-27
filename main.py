from fastapi import FastAPI
from server.routes import router

app = FastAPI()


app.include_router(router, prefix='/api')
