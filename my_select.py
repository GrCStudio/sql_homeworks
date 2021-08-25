import sqlalchemy

db = 'postgresql://postgres:123456@localhost:5432/music'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

#название и год выхода альбомов, вышедших в 2018 году;
sel = connection.execute("""SELECT name, year FROM album 
	WHERE year = 2018;
    """).fetchall()
print(sel)

# название и продолжительность самого длительного трека;
sel = connection.execute("""SELECT name, lasting FROM track
	ORDER BY lasting DESC;
    """).fetchone()
print(sel)

# название треков, продолжительность которых не менее 3,5 минуты;
sel = connection.execute("""SELECT name FROM track
	WHERE lasting >= 3.30;
    """).fetchall()
print(sel)

#названия сборников, вышедших в период с 2018 по 2020 год включительно
sel = connection.execute("""SELECT name FROM collection
	WHERE year BETWEEN 2018 AND 2020;
    """).fetchall()
print(sel)

#исполнители, чье имя состоит из 1 слова;
sel = connection.execute("""SELECT name FROM performer;
    """).fetchall()
new_list = []
for i in sel:
    if len(i[0].split()) == 1:
         new_list.append(i[0])
print(new_list)

#название треков, которые содержат слово "мой"/"my".
sel = connection.execute("""SELECT name FROM track
    WHERE name LIKE '%%My%%' OR  name LIKE '%%my%%';
    """).fetchall()
print(sel)

