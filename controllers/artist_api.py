from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from repositories import artist_repo as artistRepo
from schemas.schemas import ArtistResponse, AlbumResponse, SongResponse, SongDetailResponse
from sqlalchemy.orm import Session
from dependencies import get_db



router = APIRouter()

@router.get("/v1/singers/", response_model=List[ArtistResponse], status_code=status.HTTP_200_OK)
async def get_artist(db: Session = Depends(get_db)):
    response = artistRepo.get_artists(db)
    return response

@router.get("/v1/singers/{id}/", response_model=List[AlbumResponse], status_code=status.HTTP_200_OK)
async def get_album_by_artist(artistId: int,db: Session = Depends(get_db)):
    response = artistRepo.get_album_by_artist(db, artistId)
    return response

#Falta el response model vamos a ver primero si funciona
@router.get("/v1/singer/{id}/", response_model=list[SongResponse], status_code=status.HTTP_200_OK)
async def get_song_by_artist(artistId: int,db: Session = Depends(get_db)):
    response = artistRepo.get_song_by_artist(db, artistId)
    return response

