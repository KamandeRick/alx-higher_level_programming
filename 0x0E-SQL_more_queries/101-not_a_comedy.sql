-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- You can use a maximum of two SELECT statement
-- The database name will be passed as an argument of the mysql command

SELECT
    tv_genres.name
FROM
    tv_genres
LEFT JOIN (
    SELECT
        tv_genres.id,
        tv_genres.name
    FROM
        tv_genres
    INNER JOIN
        tv_show_genres
    ON
        tv_genres.id = tv_show_genres.genre_id
    INNER JOIN
        tv_shows
    ON
        tv_show_genres.show_id = tv_shows.id
    WHERE
        tv_shows.title = "Dexter"
    ORDER BY
        tv_genres.id
) AS dexter_genres
ON
    dexter_genres.id = tv_genres.id
WHERE
    dexter_genres.id IS NULL
ORDER BY
    tv_genres.name;
