from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import click
import os

Base = declarative_base()

# file paths
authors_file = 'authors.txt'
books_file = 'books.txt'
users_file = 'users.txt'
borrowed_books_file = 'borrowed_books.txt'

engine = create_engine('sqlite:///booksphere.db', echo=False)