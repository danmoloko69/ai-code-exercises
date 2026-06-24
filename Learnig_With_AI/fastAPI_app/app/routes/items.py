from fastapi import APIRouter, HTTPException, status
from app.models.schemas import ItemCreate, ItemRead

router = APIRouter(prefix="/items", tags=["items"])

fake_db = {}

@router.post("/", response_model=ItemRead, status_code=status.HTTP_201_CREATED)
async def create_item(item: ItemCreate):
    """Create a new item using request body validation."""
    item_id = len(fake_db) + 1
    fake_db[item_id] = item.dict()
    return {"id": item_id, **fake_db[item_id]}


@router.get("/{item_id}", response_model=ItemRead)
async def read_item(item_id: int):
    """Return an existing item or raise a clear error."""
    if item_id not in fake_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item {item_id} not found"
        )
    return {"id": item_id, **fake_db[item_id]}
