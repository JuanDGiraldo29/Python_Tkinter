CREATE TABLE students(id serial, name text, degree text, age int);

INSERT INTO students(name, degree, age) VALUES 
    ('RYAN', 'Sistemas', 23);
INSERT INTO students(name, degree, age) VALUES 
    ('JOHN', 'Ambiental', 33);

select* from students;