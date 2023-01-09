from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from dependencies import get_db
from repositories import album_repo
from schemas.schemas import SongResponse

router = APIRouter()

@router.get("/v1/albums/{id}/", response_model=List[SongResponse])
async def get_song_by_album_of_artist(id: int, db :Session = Depends(get_db)):
    response = album_repo.get_song_by_album(db, id)
    return response