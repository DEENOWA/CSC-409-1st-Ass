CREATE TABLE Students(
    Matric_no INT(11) PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    department VARCHAR(50) NOT NULL,
    CGPA DECIMAL(2,1) NOT NULL
)

INSERT INTO Students (Matric_no, name, department, CGPA) VALUES
(011,'Tolu Fabiyi','Software Engineering',3.8),
(012,'Ruth Oluwa','IT',4.5),
(013,'David Chuks','Computer Science',3.5),
(014,'Hanna Abiodun','Software Engineering',3.9);

SELECT * FROM Students;

SELECT * FROM Students WHERE Matric_no = '012';

SELECT Name, CGPA FROM Students WHERE CGPA > 3.5;


