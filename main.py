import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from db.database import fetch_random_recipe, fetch_recipe_by_id


class Recipe(BaseModel):
    id: int
    name: str
    total_duration: int
    ingredients: list
    directions: str

    class Config:
        schema_extra = {
            "example": {
                "id": 5490,
                "name": "Tongue and Mustard Sandwiches Recipe",
                "total_duration": 150,
                "ingredients": ["salt", "onion", "mustard", "bread", "beef"],
                "directions": "Rinse beef tongue and place in a large pot. Cover with water and add the salt and chopped onion...",
            }
        }


app = FastAPI()


@app.get("/", status_code=200, response_model=Recipe)
def get_recipes() -> dict:
    recipe: Recipe = fetch_random_recipe()
    return recipe


@app.get("/{id}", status_code=200, response_model=Recipe)
def get_recipe_by_id(id) -> dict:
    recipe: Recipe = fetch_recipe_by_id(id)
    if recipe is not None:
        return {"status": 200, "recipe": recipe}
    return {"status": 404, "message": "recipe not found"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
