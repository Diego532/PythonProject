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
    AlbumId: int

class SongResponse(SongBase):
    class Config:
        orm_mode = True

class SongDetailResponse(SongBase):
    Composer: Optional[str]
    Milliseconds: int
    Bytes: Optional[int]
    #UnitPrice: float  #tengo un error para retornar el precio
    
    class Config:
        orm_mode = True

