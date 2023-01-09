from sqlalchemy.orm import Session
from schemas import models, schemas

async def get_song_by_album(db : Session, albumId: int):
    try:
        result = db.query(models.Songs).filter(models.Songs.AlbumId == albumId).all()
    except ValueError as e:
        print(e)
    return result