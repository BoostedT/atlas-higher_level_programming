-- Use the tv_shows, tv_show_genres, and genres tables to find the genres of the TV show Dexter. Your query should return the genre names in alphabetical order.
SELECT name FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
JOIN genres ON tv_shows.id=tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter'
ORDER BY genres.name ASC;
