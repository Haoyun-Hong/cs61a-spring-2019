.read sp19data.sql

-- Q2
CREATE TABLE obedience AS
  SELECT seven, animal FROM students;

-- Q3
CREATE TABLE smallest_int AS
  SELECT time, smallest FROM students WHERE smallest > 2   ORDER BY smallest LIMIT 20;

-- Q4
CREATE TABLE matchmaker AS
  SELECT tabel1.pet, tabel1.song, tabel1.color, tabel2.color FROM students as tabel1 , students as tabel2 
  WHERE tabel1.pet=tabel2.pet AND tabel1.song = tabel2.song AND (tabel1.time !=tabel2.time);
