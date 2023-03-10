from typing import List, Any, Optional
from pydantic import BaseModel
from pydantic.schema import Optional

class ArtistBase(BaseModel):
    ArtistId: int
    Name: str


class ArtistResponse(ArtistBase):
    
    class Config:
        orm_mode = True


class AlbumBase(BaseModel):
    AlbumId: int
    Title: str

class AlbumResponse(AlbumBase):
    class Config:
        orm_mode = True

#Este es el schema de respuesta para las canciones
class SongBase(BaseModel):
    TrackId: int
    Name: str
    AlbumId: Optional[int]

class SongResponse(SongBase):
    class Config:
        orm_mode = True

class SongDetailResponse(SongBase):
    Composer: Optional[str]
    MediaTypeId: int
    GenreId: Optional[int]
    Milliseconds: int
    Bytes: Optional[int]
    UnitPrice: float
    
    class Config:
        orm_mode = True

