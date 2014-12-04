CREATE DATABASE tourism;
use tourism;

CREATE TABLE city(
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY ,
name VARCHAR(50),
state VARCHAR(50),
country VARCHAR(50)
);

CREATE TABLE activity(
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY ,
activity VARCHAR(50),
parent_activity VARCHAR(50)
);

create table activity_mapping(
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
activity_id INT,
city_id INT,
rating INT,
FOREIGN KEY (activity_id) REFERENCES activity(id) ON DELETE CASCADE,
FOREIGN KEY (city_id) REFERENCES city(id) ON DELETE CASCADE
);

create table group_mapping(
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
city_id INT,
solo INT,
couple INT,
family INT,
friend INT,
FOREIGN KEY (city_id) REFERENCES city(id) ON DELETE CASCADE
);
