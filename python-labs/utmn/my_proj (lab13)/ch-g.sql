SELECT * FROM ch_g_book;
SELECT * FROM ch_g_book_authors;
SELECT * FROM ch_g_book_languages;
SELECT * FROM ch_g_book_genres;

SELECT * FROM ch_g_author;
SELECT * FROM ch_g_language;
SELECT * FROM ch_g_genre;
SELECT * FROM ch_g_print;

SELECT * FROM ch_g_book;
SELECT * FROM ch_g_book_authors;
SELECT * FROM ch_g_author;

SELECT fsl_name, ch_g_book.id
FROM ch_g_author
JOIN ch_g_book_authors ON ch_g_author.id = ch_g_book_authors.author_id
JOIN ch_g_book ON ch_g_book.id = ch_g_book_authors.book_id
WHERE ch_g_book.id = 1;

SELECT * FROM pg_roles;