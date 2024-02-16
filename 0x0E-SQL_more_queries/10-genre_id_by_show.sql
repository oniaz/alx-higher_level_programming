-- task 10
-- Listing all shows in the database that have at least one genre linked.
-- Each record displays the show title, and the its genre id.

SELECT tv_shows.title,
       tv_show_genres.genre_id
FROM   tv_shows
       JOIN tv_show_genres
         ON tv_show_genres.show_id = tv_shows.id
ORDER  BY tv_shows.title ASC,
          tv_show_genres.genre_id ASC; 
