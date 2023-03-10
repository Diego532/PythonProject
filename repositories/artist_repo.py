from schemas import models
from sqlalchemy.orm import Session


async def get_artists(db: Session):
    try:
        return db.query(models.Artists).all()
    except:
        print("Ocurrio un error con get_artist")

async def get_album_by_artist(db: Session, artistId:int = 0):
    try:
        return db.query(models.Albums).filter(models.Albums.ArtistId == artistId).all()
    except:
        print("Ocurrio un error en get_album_by_artist")


async def get_song_by_artist(db: Session, artistID: int = 0):
    try:
        result = db.query(
            models.Songs).join(models.Albums, models.Songs.AlbumId == models.Albums.AlbumId).filter(models.Albums.ArtistId == artistID).all() 
        return result
    except:
        print("Some thing went wrong")
