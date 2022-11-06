-- Task 13
SELECT name as 'genre', COUNT(*) AS 'number_of_shows' FROM tv_show_genres, tv_genres WHERE tv_genre.id = tv_show_genres.genre_id
GROUP BY tv_genres.name ORDER BY number_of_shows DESC;
