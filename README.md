# Student Records Database (MySQL)

This project sets up a simple MySQL database for storing and retrieving student academic records. It includes a `Students` table and some example data that you can use to test and practice SQL queries.

## Table Structure

The database contains one table named `Students`, with the following fields:

| Column      | Type         | Description |
|-------------|--------------|-------------|
| Matric_no   | INT (PK)     | Unique student ID |
| name        | VARCHAR(50)  | Student's full name |
| department  | VARCHAR(50)  | Student's department |
| CGPA        | DECIMAL(2,1) | Cumulative Grade Point Average |

## How to Use

1. Make sure MySQL is installed on your system.
2. Open your SQL editor or terminal.
3. Run the SQL script provided in `MySQL Local.session.sql`.

This will:
- Create the `Students` table
- Insert sample data
- Run a few example queries

## Sample Queries

**View all students:**
```sql
SELECT * FROM Students;
