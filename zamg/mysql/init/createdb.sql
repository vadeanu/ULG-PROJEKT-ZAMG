create DATABASE zamg;
use zamg;

CREATE TABLE thesis
  (
     urn            VARCHAR(250) NOT NULL,
     title          VARCHAR(250) NOT NULL,
     subtitle       VARCHAR(250),
     author         VARCHAR(60) NOT NULL,
     language       VARCHAR(25) NOT NULL,
     supervisor     VARCHAR(60) NOT NULL,
     sec_supervisor VARCHAR(60),
     genre          VARCHAR(80) NOT NULL,
     university     VARCHAR(150) NOT NULL,
     production     INT(10) NOT NULL,
     abstract       LONGTEXT,
     PRIMARY KEY (urn)
  );