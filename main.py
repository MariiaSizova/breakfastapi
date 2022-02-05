import uvicorn
from fastapi import FastAPI

from db.database import Database
from helpers.data_formating import jsonify_data

app = FastAPI()
db = Database()


@app.get("/", status_code=200)
def get_recipes() -> list:
    return jsonify_data(db)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
