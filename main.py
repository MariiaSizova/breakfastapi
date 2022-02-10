import uvicorn
from fastapi import FastAPI

from db.database import fetch_random_recipe, fetch_recipe_by_id

app = FastAPI()


@app.get("/", status_code=200)
def get_recipes() -> dict:
    return {"status": 200, "recipe": fetch_random_recipe()}


@app.get("/{id}", status_code=200)
def get_recipe_by_id(id) -> dict:
    if fetch_recipe_by_id(id) is not None:
        return {"status": 200, "recipe": fetch_recipe_by_id(id)}
    return {"status": 404, "message": "recipe not found"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
