-- Convert hbtn_0c_0 database UTF8MB4 to UTF8MB4_UNICODE_CI
USE `hbtn_0c_0`;
ALTER TABLE `first_table` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
