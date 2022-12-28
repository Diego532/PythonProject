from schemas import models, schemas
from sqlalchemy.orm import Session


def get_artists(db: Session,  skip: int = 0, limit: int = 100):
    return db.query(models.Artists).offset(skip).limit(100).all()

def get_album_by_artist(db: Session, artistId:int = 0):
    return db.query(models.Albums).filter(models.Albums.ArtistId == artistId).all()


#Este endpoint todavia no esta funcionando
def get_song_by_artist(db: Session, artistID: int = 0):
    try:
        result = db.query(models.Albums).join(models.Artists).filter(models.Albums.ArtistId == models.Artists.ArtistId).filter(models.Artists.ArtistId == artistID).all() 
        print(f"Esta es mi respuesta: {result}")
        return result
    except:
        print("Some thing went wrong")

# La consulta no esta funcionando correctamente