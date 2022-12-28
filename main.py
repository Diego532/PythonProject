from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controllers.artist_api import router as artist_router
from controllers.song_api import router as song_router
from controllers.album_api import router as album_router
from database import engine
from schemas import models, schemas

models.Base.metadata.create_all(bind=engine)

def get_aplication():


    app = FastAPI(
        title="Proyecto Pracial 2",
        description="Actividad practica para Python",
        version="0.1.0"
    )   

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    app.include_router(artist_router, prefix="/music-store/api", tags=["Artistas"])
    app.include_router(song_router, prefix="/music-store/api", tags=["Cancion"])
    app.include_router(album_router, prefix="/music-store/api", tags=["Album"])
    return app




app: FastAPI = get_aplication()


