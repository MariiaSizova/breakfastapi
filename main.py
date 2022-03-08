import uvicorn
from fastapi import FastAPI
from typing import Union

from db.database import fetch_random_recipe, fetch_recipe_by_id, fetch_recipes
from models.recipe import Recipe, RecipeResponse, RecipesResponse, RecipesRequest
from models.error import NotFoundResponse
from starlette.responses import FileResponse


app = FastAPI()
favicon_path = 'images/favicon.ico'


@app.get('/favicon.ico')
async def favicon():
    return FileResponse(favicon_path)


@app.get("/", response_model=RecipeResponse, responses={200: {"model": RecipeResponse}})
@app.get("/recipes", response_model=RecipeResponse, responses={200: {"model": RecipeResponse}})
def get_random_recipe() -> RecipeResponse:
    """
    This function returns a random recipe from the database.
    ---
    Args: None
    Returns:
        dict: A dictionary containing status code and recipe. 
    """
    recipe: Recipe = fetch_random_recipe()
    return {"status": 200, "recipe": recipe}


@app.get("/{id}",
    response_model=Union[RecipeResponse, NotFoundResponse],
    responses={200: {"model": RecipeResponse}, 404: {"model": NotFoundResponse}},
)
def get_recipe_by_id(id: int) -> dict:
    """
    This function returns a recipe from the database by id.
    ---
    Args:
        id (int): id of the recipe passed as a path parameter.
    Returns:
        dict: A dictionary containing status code and a recipe.
    """
    recipe: Recipe = fetch_recipe_by_id(id)
    if recipe is not None:
        return {"status": 200, "recipe": recipe}
    return {"status": 404, "message": "recipe not found"}


@app.get("/recipes/{limit}",
    response_model=Union[RecipesResponse, NotFoundResponse],
    responses={200: {"model": RecipesResponse}, 404: {"model": NotFoundResponse}},
)
def get_recipes(limit: RecipesRequest) -> RecipesResponse:
    """
    This function returns multiple recipes from the database.
    ---
    Args:
        limit (int): numbers of recipes to be returned.
    Returns:
        RecipesResponse: A dictionary containing status code and multiple recipes. 
    """
    recipes = fetch_recipes(limit)
    if len(recipes):
        return {"status": 200, "results": recipes}
    return {"status": 404, "message": "recipe not found"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
