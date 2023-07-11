create table certificates (
id integer not null, 
certificate_id varchar(255), 
created_at timestamp(6), 
created_by varchar(255), 
entitytype varchar(255), 
expired varchar(255), 
fitype varchar(255), 
name varchar(255), 
purposecode integer not null, 
rebitversion varchar(255), 
updated_at timestamp(6), 
updated_by varchar(255), 
primary key (id)
);


CREATE TABLE IF NOT EXISTS Verification (
  id integer PRIMARY KEY,
  name TEXT NOT NULL,
  entitytype TEXT NOT NULL,
  rebitversion TEXT NOT NULL,
  purposecode integer NOT NULL,
  fitype TEXT NOT NULL, 
  expired DATE,
  createdAt DATE,
  updatedAt DATE,
  updatedBy TEXT,
  createdBy TEXT,
  certificate_id integer,
  CONSTRAINT fk_Certificates FOREIGN KEY (certificate_id) REFERENCES certificates (id)
);


