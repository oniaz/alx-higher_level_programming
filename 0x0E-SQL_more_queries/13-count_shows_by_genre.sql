-- task 13
-- Listing all the genres in the database.
-- Each record displays the genre and the number of shows linked to it.

SELECT tv_genres.NAME                AS genre,
       Count(tv_show_genres.show_id) AS number_of_shows
FROM   tv_show_genres
       JOIN tv_genres
         ON tv_show_genres.genre_id = tv_genres.id
GROUP  BY tv_show_genres.genre_id
ORDER  BY number_of_shows DESC; 