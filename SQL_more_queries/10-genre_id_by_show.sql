-- Task 10
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_show_genre INNER JOIN tv_shows ON tv_show_genre.show_id = tv_shows.id ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
