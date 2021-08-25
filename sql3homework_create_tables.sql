CREATE TABLE IF NOT EXISTS Genre (
	Id serial PRIMARY KEY NOT NULL,
	Name varchar(40) NOT NULL
);

CREATE TABLE IF NOT EXISTS Performer (
	Performer_Id serial PRIMARY KEY NOT NULL,
	Name varchar(256) NOT NULL
);

CREATE TABLE IF NOT EXISTS Album (
	Album_Id serial PRIMARY KEY NOT NULL,
	Name varchar(256) NOT NULL,
	Year integer NOT NULL
);

CREATE TABLE IF NOT EXISTS Collection (
	Collection_Id serial PRIMARY KEY NOT NULL,
	Name varchar(256) NOT NULL,
	Year integer NOT NULL
);

CREATE TABLE IF NOT EXISTS Performer_Genre (
	PG_Id serial PRIMARY KEY NOT NULL,
	Performer integer REFERENCES Performer(Performer_Id),
	Genre integer REFERENCES Genre(Id)
);

CREATE TABLE IF NOT EXISTS Performer_Album (
	Performer integer REFERENCES Performer(Performer_Id),
	Album integer REFERENCES Album(Album_Id),
	CONSTRAINT pa_key PRIMARY KEY (Performer, Album)
);

CREATE TABLE IF NOT EXISTS Track (
	Track_Id serial PRIMARY KEY NOT NULL,
	Album serial REFERENCES Album(Album_Id),
	Name varchar(256) NOT NULL,
	Lasting FLOAT(8) NOT NULL
);

CREATE TABLE IF NOT EXISTS Track_Collection (
	Track integer REFERENCES Track(Track_Id),
	Collection integer REFERENCES Collection(Collection_Id),
	CONSTRAINT tc_key PRIMARY KEY (Track, Collection)
);