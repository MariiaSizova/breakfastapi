import uvicorn
from fastapi import FastAPI

from db.database import fetch_random_recipe

app = FastAPI()


@app.get("/", status_code=200)
def get_recipes() -> dict:
    return {"status": 200, "recipe": fetch_random_recipe()}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
