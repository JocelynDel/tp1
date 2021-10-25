create database if not exists tp1;

use tp1;

create table if not exists quotes(
  id int auto_increment primary key,
  quote text(500),
  author varchar(255),
);