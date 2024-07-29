from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from ..controllers import account as controller
from ..schemas import account as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Account'],
    prefix="/account"
)

@router.post("/", response_model=schema.Account, status_code=status.HTTP_201_CREATED)
def create(request: schema.AccountCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.Account])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{item_id}", response_model=schema.Account)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)

@router.put("/{item_id}", response_model=schema.Account)
def update(item_id: int, request: schema.AccountUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)