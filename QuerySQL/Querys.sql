select * from albums where ArtistId = 1;
-- Ahora de estos albunes necesito saber cuales son las canciones que tienen.

select AlbumId from albums where ArtistId = 1;



--Esta consulta me trae una tabla con todos los artistas, sus albunes y canciones.
SELECT artists.ArtistId ,albums.AlbumId, tracks.TrackId, tracks.Name
FROM albums
INNER JOIN artists ON artists.ArtistId = albums.ArtistId
INNER JOIN tracks ON albums.AlbumId = tracks.AlbumId;

-- Esta es la consulta qu etengo que realizar con ORM "Investigar"
SELECT TrackId, name, AlbumId from (SELECT artists.ArtistId ,albums.AlbumId, tracks.TrackId, tracks.Name
FROM albums
INNER JOIN artists ON artists.ArtistId = albums.ArtistId
INNER JOIN tracks ON albums.AlbumId = tracks.AlbumId) where ArtistId = 1;