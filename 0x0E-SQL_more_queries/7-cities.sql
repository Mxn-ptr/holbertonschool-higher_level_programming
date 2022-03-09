-- Create the database hbtn_0d_usa and the table cities
-- Where id auto generated, can't be null and is a primary key
-- state_id can't be null and is a FOREIGN KEY references to id of the states tables
-- name can't be null
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
USE `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `cities` (
	`id` INT	NOT NULL AUTO_INCREMENT,
	`state_id` INT	 NOT NULL,
	`name` VARCHAR(256) 	NOT NULL,
	PRIMARY KEY(`id`),
	FOREIGN KEY(`state_id`) REFERENCES `states`(`id`)
);
