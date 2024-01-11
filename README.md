# phase-3-project
Author:Bravin Onsase
License:MIT

E.R.M Diagram

+------------------+    +------------------+
|      Author      |    |       Book       |
+------------------+    +------------------+
| id (PK)          |    | id (PK)          |
| name             |    | title            |
+------------------+    | author_id (FK)   |
                        +------------------+
                             |
                             |
                             V
+------------------+    +------------------+
|       User       |    |  BorrowedBooks   |
+------------------+    +------------------+
| id (PK)          |    | id (PK)          |
| name             |    | user_id (FK)     |
+------------------+    | book_id (FK)     |
                        +------------------+

Explanation:

-Each box represents an entity, and the lines connecting them represent relationships.
-PK denotes a primary key, and FK denotes a foreign key.
-An Author can have multiple Books (one-to-many relationship).
-A Book belongs to one Author.
-A User can borrow multiple Books, and a Book can be borrowed by multiple Users (many-to-many relationship).
-BorrowedBooks is a junction table representing the many-to-many relationship between User and Book.

Booksphere is a python application that helps the user store books,borrow books,user names,authors.

Use the command python booksphere.py to see it in action.

Use other commands like: pipenv install, pipenv shell, pip install sqlalchemy, pip install click when necessary.
