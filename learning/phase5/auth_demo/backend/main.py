from fastapi import FastAPI

from routes import router


app = FastAPI(title="Authentication Learning API")

app.include_router(router)
