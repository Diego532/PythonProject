from sqlalchemy.orm import Session
from schemas import models


def get_song(db: Session,  songId: int):
    return db.query(models.Songs).filter(models.Songs.TrackId == songId).first()