from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Search for Disney Lorcana Cards!"}
