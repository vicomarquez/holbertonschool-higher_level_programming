-- Task 15
SELECT title FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_shows_genres.show_id
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY title ASC;
