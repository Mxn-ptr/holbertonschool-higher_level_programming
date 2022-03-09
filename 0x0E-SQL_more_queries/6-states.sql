-- Create the database hbtn_0d_usa and the table states
-- Where id is unique,  auto generated, can't be null and is a primary key
-- name can't be null
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`states` (
	`id` INT	NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(256) 	NOT NULL,

	PRIMARY KEY(`id`)
);
