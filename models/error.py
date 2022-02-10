from pydantic import BaseModel

class ResponseError(BaseModel):
    status: int
    message: str


class NotFoundResponse(ResponseError):
    class Config:
        schema_extra = {"example": {"status": 404, "message": "recipe not found"}}
