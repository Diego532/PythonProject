from fastapi import APIRouter

router = APIRouter()

@router.get("/v1/albums/{id}/")
async def get_song_by_album_of_artist():
    return {"message":"lista de canciones del álbum de un artista"}