CREATE DATABASE zamg;
use zamg;

CREATE TABLE thesis (
  urn VARCHAR(250) NOT NULL,
  title VARCHAR(250) NOT NULL,
  subtitle VARCHAR(250),
  author VARCHAR(250) NOT NULL,
  language VARCHAR(250) NOT NULL,
  supervisor VARCHAR(250) NOT NULL,
  sec_supervisor VARCHAR(250),
  genre VARCHAR(250) NOT NULL,
  university VARCHAR(250) NOT NULL,
  production int NOT NULL,
  abstract LONGTEXT(250),
);


