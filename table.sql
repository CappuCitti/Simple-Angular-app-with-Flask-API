CREATE TABLE users (
	id int IDENTITY(0,1) PRIMARY KEY,
	email varchar(255) NOT NULL,
	password varchar(255) NOT NULL,
	first_name varchar(255) NOT NULL,
	last_name varchar(255) NOT NULL,
	born_date DATE NOT NULL,
	info TEXT NOT NULL,
	gender varchar(32) NOT NULL
);