from schemas import models
from sqlalchemy.orm import Session


def get_artists(db: Session,  skip: int = 0, limit: int = 100):
    return db.query(models.Artists).offset(skip).limit(100).all()

def get_album_by_artist(db: Session, artistId:int = 0):
    return db.query(models.Albums).filter(models.Albums.ArtistId == artistId).all()



def get_song_by_artist(db: Session, artistID: int = 0):
    try:
        result = db.query(
            models.Songs).join(models.Albums, models.Songs.AlbumId == models.Albums.AlbumId).filter(models.Albums.ArtistId == artistID).all() 
        return result
    except:
        print("Some thing went wrong")
