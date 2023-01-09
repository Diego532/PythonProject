from sqlalchemy.orm import Session
from schemas import models


async def get_song(db: Session,  songId: int):
    return db.query(models.Songs).filter(models.Songs.TrackId == songId).first()