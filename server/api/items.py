# from fastapi import APIRouter, HTTPException, Depends
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.future import select

# from database import get_session
# from models import Item
# from schemas import ItemCreate, ItemUpdate, ItemResponse

# router = APIRouter()


# @router.post("/", response_model=ItemResponse)
# async def create_item(item: ItemCreate, session: AsyncSession = Depends(get_session)):
#     db_item = Item(**item.dict())
#     session.add(db_item)
#     await session.commit()
#     await session.refresh(db_item)
#     return db_item


# @router.get("/", response_model=list[ItemResponse])
# async def read_items(
#     skip: int = 0, limit: int = 100, session: AsyncSession = Depends(get_session)
# ):
#     result = await session.execute(select(Item).offset(skip).limit(limit))
#     items = result.scalars().all()
#     return items


# @router.get("/{item_id}", response_model=ItemResponse)
# async def read_item(item_id: int, session: AsyncSession = Depends(get_session)):
#     db_item = await session.get(Item, item_id)
#     if not db_item:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return db_item


# @router.put("/{item_id}", response_model=ItemResponse)
# async def update_item(
#     item_id: int, item: ItemUpdate, session: AsyncSession = Depends(get_session)
# ):
#     db_item = await session.get(Item, item_id)
#     if not db_item:
#         raise HTTPException(status_code=404, detail="Item not found")
#     for key, value in item.dict().items():
#         setattr(db_item, key, value)
#     await session.commit()
#     await session.refresh(db_item)
#     return db_item


# @router.delete("/{item_id}")
# async def delete_item(item_id: int, session: AsyncSession = Depends(get_session)):
#     db_item = await session.get(Item, item_id)
#     if not db_item:
#         raise HTTPException(status_code=404, detail="Item not found")
#     await session.delete(db_item)
#     await session.commit()
#     return {"message": "Item deleted successfully"}
