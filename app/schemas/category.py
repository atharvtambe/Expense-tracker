from pydantic import BaseModel


class CategoryCreate(BaseModel):
    name: str
    color: str


class CategoryResponse(BaseModel):
    id: int
    name: str
    color: str

    class Config:
        from_attributes = True