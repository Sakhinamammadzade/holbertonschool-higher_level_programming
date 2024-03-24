-- lists all shows without the genre Comedy in the database
SELECT tv_shows.title
FROM tv_shows
WHERE id NOT IN (
	    SELECT 1
	    FROM tv_genres
	    JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
	    JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
	    WHERE tv_genres.name = 'Comedy'
)
ORDER BY tv_shows.title;
