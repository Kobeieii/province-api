from fastapi import FastAPI, Request
import router

app = FastAPI()
app.include_router(router.router)