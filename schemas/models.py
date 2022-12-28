from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.types import Numeric
from sqlalchemy.orm import relationship
from database import Base

class Artists(Base):
    __tablename__ = "artists"

    ArtistId = Column(Integer, primary_key=True)
    Name =  Column(String)
    albums = relationship("Albums", back_populates="artist")

class Albums(Base):
    __tablename__ = "albums"

    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("artists.ArtistId"))
    artist = relationship("Artists", back_populates="albums")
    song = relationship("Songs", back_populates="album")

class Songs(Base):
    __tablename__ = "tracks"

    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("albums.AlbumId"))
    MediaTypeId = Column(Integer,nullable=False)
    GenreId = Column(Integer)
    Composer = Column(String)
    Milliseconds = Column(Integer, nullable=False)
    Bytes = Column(Integer)
    UnitPrice = (Numeric)

    album = relationship("Albums", back_populates='song')

#Nota: Todos los campos son necesarios o solo los que utilizo.