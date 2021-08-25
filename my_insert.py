import sqlalchemy

db = 'postgresql://postgres:123456@localhost:5432/music'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

# genres_list = ['hard rock','heavy metal','power metal','folk rock','pagan metal']
# for i in genres_list:
#    my_string = f"""INSERT INTO genre(name)
#           VALUES('{i}');
#    """
#    connection.execute(my_string)
#
# sel = connection.execute("""SELECT name FROM genre;
# """).fetchall()
# print(sel)
#
# performers_list = ['Корневище с горы','Rocketeers','Hyaena','Great Minstrel','Elves band','The Swords','Dragon','Destend']
# for i in performers_list:
#     my_string = f"""INSERT INTO performer(name)
#            VALUES('{i}');
#     """
#     connection.execute(my_string)
#
# albums_list = [['Спускаясь с гор', 2008],['Skyrize', 1989],['Warcry',2011],['Lute`s song',2020],
#                ['Elven arrows',2018],['Great Victory',2002],['My breath',2019],['Destiny',2000]]
# for i in albums_list:
#     my_string = f"""INSERT INTO album(name, year)
#            VALUES('{i[0]}',{i[1]});
#     """
#     connection.execute(my_string)
#
# collections_list = [['Сага', 2018],['Matallized', 2019],['Викинги',2012],['Fantezy',2017],
#                ['Fantezy2',2021],['Metal Hymnes',2017],['2015',2015],['Plague',2021]]
# for i in collections_list:
#     my_string = f"""INSERT INTO collection(name, year)
#            VALUES('{i[0]}',{i[1]});
#     """
#     connection.execute(my_string)
#
# perf_genrs_list = [[1, 4],[1,5],[2,1],[2,2],[3,3],[3,1],[4,4],[4,5],[5,4],[6,3],[7,1],[7,2],[7,3],[8,3],[8,5],[8,2]]
# for i in perf_genrs_list:
#     my_string = f"""INSERT INTO performer_genre(performer, genre)
#            VALUES({i[0]},{i[1]});
#     """
#     connection.execute(my_string)
#
# track_list = [['Спускаясь с гор', 1, 3.54],
#                 ['Корневище', 1, 4.11],
#                 ['Skyrize', 2, 3.55],
#                 ['Metal roket', 2, 7.12],
#                 ['War song', 3, 3.05],
#                 ['Metal hymn', 3, 3.27],
#                 ['My lute', 4, 4.44],
#                 ['Blessed strings', 4, 4.51],
#                 ['Green arrows fly', 5, 5.01],
#                 ['Orc`s death', 5, 5.21],
#                 ['Paladines', 6, 4.00],
#                 ['Codex', 6, 5.35],
#                 ['Scales mirror', 7, 3.54],
#                 ['My breath', 7, 4.01],
#                 ['Warrior', 8, 3.51],
#                 ['Norske', 8, 5.22],
#                 ['Roket rock', 2, 6.02],
#                 ['Great Minstrel', 4, 4.02],
#                 ['Fly of Dragons', 7, 5.22]
#                ]
#
# for i in track_list:
#     my_string = f"""INSERT INTO Track(name, album, lasting)
#            VALUES('{i[0]}',{i[1]},{i[2]});
#     """
#     #print(my_string)
#     connection.execute(my_string)

# track_collection_list = [[1,1],
#                         [1,5],
#                         [1,6],
#                         [2,3],
#                         [2,4],
#                         [2,11],
#                         [2,14],
#                         [3,5],
#                         [3,6],
#                         [3,15],
#                         [3,16],
#                         [4,11],
#                         [4,12],
#                         [4,1],
#                         [5,8],
#                         [5,9],
#                         [5,13],
#                         [5,14],
#                         [6,4],
#                         [6,11],
#                         [6,6],
#                         [8,3],
#                         [8,14],
#                         [8,10]
#                         ]
# for i in track_collection_list:
#     my_string = f"""INSERT INTO track_collection(track, collection)
#            VALUES({i[1]},{i[0]});
#     """
#     connection.execute(my_string)



