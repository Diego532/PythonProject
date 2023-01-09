from fastapi import APIRouter, Depends
from repositories import song_repo
from sqlalchemy.orm import Session
from dependencies import get_db
from schemas.schemas import SongDetailResponse
router = APIRouter()


#Tengu un problema para devolver el precio por la parte dle numeric
@router.get("/v1/song/{id}/", response_model=SongDetailResponse)
async def get_song_detail(id: int,db: Session = Depends(get_db) ):
    response = song_repo.get_song(db,id)
    return response