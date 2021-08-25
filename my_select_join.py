import sqlalchemy

db = 'postgresql://postgres:123456@localhost:5432/music'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()


#количество исполнителей в каждом жанре;
sel = connection.execute("""SELECT g.name, SUM(performer) FROM Performer_Genre AS pg
    LEFT JOIN genre AS g ON pg.genre = g.id
    GROUP BY g.name
    """).fetchall()
print(sel)
print()

#количество треков, вошедших в альбомы 2019-2020 годов
sel = connection.execute("""SELECT COUNT(t.name) FROM album AS a
    LEFT JOIN track AS t ON t.album = a.album_id
    WHERE a.year BETWEEN 2019 and 2020
    """).fetchall()
print(sel)
print()

#средняя продолжительность треков по каждому альбому
# не уверен, что в данном случае делать, так как он неправильно считает указанное время. в треках после запятой секунды, а не сотые минуты
sel = connection.execute("""SELECT a.name, AVG(t.lasting) FROM album AS a
    LEFT JOIN track AS t ON t.album = a.album_id
    GROUP BY a.name
    """).fetchall()
print(sel)
print()

#все исполнители, которые не выпустили альбомы в 2020 году
sel = connection.execute("""SELECT p.name FROM performer AS p
    JOIN Performer_Album AS pa ON pa.performer = p.performer_id
    JOIN Album AS a ON a.album_id = pa.album
    WHERE a.year != 2020
    GROUP BY p.name
    """).fetchall()
print(sel)
print()

#названия сборников, в которых присутствует конкретный исполнитель (выберите сами)(id 1)
sel = connection.execute("""SELECT c.name FROM collection AS c
    JOIN Track_Collection AS tc ON tc.collection = c.collection_id
    JOIN Track AS t ON t.track_id = tc.track
    JOIN Album AS a ON a.album_id = t.album
    JOIN Performer_Album AS pa ON pa.album = a.album_id
    JOIN Performer AS p ON p.performer_id = pa.performer
    WHERE p.performer_id = 1
    GROUP BY c.name
    """).fetchall()
print(sel)
print()

# название альбомов, в которых присутствуют исполнители более 1 жанра
sel = connection.execute("""SELECT a.name FROM Album AS a
    JOIN Performer_Album AS pa ON pa.album = a.album_id
    JOIN Performer AS p ON p.performer_id = pa.performer
    JOIN Performer_Genre AS pg ON pg.performer = p.performer_id
    JOIN Genre AS g ON g.id = pg.genre
    WHERE p.performer_id IN (
                            SELECT Performer FROM Performer_Genre
                            GROUP BY Performer
                            HAVING COUNT(Performer) > 1
                            )
    GROUP BY a.name
    """).fetchall()
print(sel)
print()

#наименование треков, которые не входят в сборники
sel = connection.execute("""SELECT t.name FROM Track AS t
    FULL OUTER JOIN Track_Collection AS tc ON tc.track = t.track_id
	WHERE tc.track IS NULL
    """).fetchall()
print(sel)
print()

# исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько);
sel = connection.execute("""SELECT p.name, t.lasting FROM Performer AS p
    JOIN Performer_Album AS pa ON pa.performer = p.performer_id
	JOIN Album AS a ON a.album_id = pa.performer
 	JOIN Track AS t ON t.album = a.album_id
	WHERE t.lasting = (SELECT MIN(lasting) FROM Track)
    """).fetchall()
print(sel)
print()

#название альбомов, содержащих наименьшее количество треков
sel = connection.execute("""SELECT a.name FROM Album AS a
    JOIN track AS t ON a.album_id = t.album 
    GROUP BY a.name
    HAVING COUNT(a.album_id) = (SELECT COUNT(album_id) AS count_a FROM album AS a
	                            JOIN track AS t ON a.album_id = t.album 
	                            GROUP BY a.album_id
	                            ORDER BY count_a
	                            LIMIT 1)                            
    """).fetchall()
print(sel)
print()