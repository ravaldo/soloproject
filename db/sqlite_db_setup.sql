DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS membertypes;
DROP TABLE IF EXISTS classes;

CREATE TABLE membertypes(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name VARCHAR(255) NOT NULL
);
CREATE TABLE members(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name VARCHAR(255) NOT NULL,
	date_of_birth DATE NOT NULL,
	membertype_id INTEGER REFERENCES membertypes(id) ON DELETE CASCADE
);
CREATE TABLE classes(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name VARCHAR(255) NOT NULL,
	event_time TIMESTAMP NOT NULL,
	capacity INTEGER NOT NULL
);
CREATE TABLE bookings(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	member_id INTEGER REFERENCES members(id) ON DELETE CASCADE,
	class_id INTEGER REFERENCES classes(id) ON DELETE CASCADE
);