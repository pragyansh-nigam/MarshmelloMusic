create database mymusic;

	create table mymusic.contact(
		uid int AUTO_INCREMENT,
		name varchar(100) NOT NULL,
		email varchar(100) NOT NULL,
		subject varchar(1000),
		message varchar(5000) NOT NULL,
		PRIMARY KEY(uid);
	); 