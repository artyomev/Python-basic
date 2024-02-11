from fastapi import FastAPI
from views.pinger import router as pinger_router

app = FastAPI()
app.include_router(pinger_router)


@app.get("/")
def root():
    return {"message": "Root Page"}

