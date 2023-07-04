CREATE TABLE IF NOT EXISTS Certificates (
    id uuid NOT NULL,
    certificate_id uuid,
    name text NOT NULL,
    entitytype text NOT NULL,
    rebitversion text NOT NULL,
    purposecode int NOT NULL,
    expired date,
    createdAt date,
    updatedAt date,
    updatedBy text, 
    createdBy text,
    PRIMARY KEY (certificate_id)
);


CREATE TABLE IF NOT EXISTS Verification (
  id UUID NOT NULL PRIMARY KEY,
  name TEXT NOT NULL,
  entitytype TEXT NOT NULL,
  rebitversion TEXT NOT NULL,
  purposecode INT NOT NULL,
  expired DATE,
  createdAt DATE,
  updatedAt DATE,
  updatedBy TEXT,
  createdBy TEXT,
  certificate_id UUID,
  CONSTRAINT fk_Certificates FOREIGN KEY (certificate_id) REFERENCES Certificates (certificate_id)
);

