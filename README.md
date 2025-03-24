# Library-Management-System
# Description
This Django-based Library Management System provides APIs for managing books, book genres, and book reviews. It includes user authentication for admins and CRUD operations for books.

# Features
## Admin Authentication

Admins can sign up and log in to manage the system.

## Book Genre Management

Create book genres to categorize books.

## Book Management

Add, update, retrieve, and delete books in the system.

## Book Retrieval

Fetch all available books in the library.

## Book Reviews

Users can submit reviews and ratings for books.

Modeling Strategy
This project follows a relational database design using Django ORM. Below is an overview of the key models:

1️⃣ AdminUser Model
Extends AbstractUser, making email the primary identifier instead of username.

Uses a custom AdminUserManager for user creation.

Implements groups and user_permissions for role-based access control.

2️⃣ BookGenre Model
Stores different book categories (e.g., "Computer Science", "History").

Has a one-to-many relationship with the Book model.

3️⃣ Book Model
Represents a book with fields like title, author, edition, published_date, and genre.

A foreign key (genre) links each book to its respective genre.

Uses cascade deletion, meaning deleting a genre removes all its associated books.

4️⃣ BookReview Model
Stores student reviews and ratings for books.

A foreign key (book) links reviews to a book.

A foreign key (student) links reviews to students.

Uses created_at to timestamp the review.

5️⃣ StudentFeedback Model
Allows students to provide general feedback about the library system.

A foreign key (student) associates feedback with the user.

Uses created_at for tracking when the feedback was submitted

## API Endpoints

## 1. Admin Creation
# Method
  POST
# Endpoint
  http://127.0.0.1:8000/api/admin/signup/
# Payload
  {
      "email": "snehal@gmail.com",
      "password": "snehal@123"
  }
# Response
  {
      "success": true,
      "message": "Admin registered successfully.",
      "errors": {
          "code": null,
          "message": null,
          "fields": []
      },
      "data": {
          "id": "1",
          "email": "snehal@gmail.com"
      }
  }

## 2. Admin Login
## Method
  POST
## Endpoint
  http://127.0.0.1:8000/api/admin/login/
## Payload
  {
      "email": "snehal@gmail.com",
      "password": "testpassword"
  }
## Response
  {
      "success": true,
      "message": "Login successful.",
      "errors": {
          "code": null,
          "message": null,
          "fields": []
      },
      "data": {
          "token": "1896486a1605ac2a46e233c7c049e95c0bb64dc1"
      }
  }

## 3. Book Genre Creation 
## Method 
  POST
## Endpoint
  http://127.0.0.1:8000/api/book-genres/
## Payload
  {
      "name": "Computer Science"
  }
## Response
  {
      "success": true,
      "message": "Book genre added successfully",
      "errors": {
          "code": null,
          "message": null,
          "fields": []
      },
      "data": {
          "id": 1,
          "name": "Computer Science"
      }
  }

## 4. Book Creation
## Method 
  POST
## Endpoint
  http://127.0.0.1:8000/api/books/
## Payload
  {
      "title": "Python Basics",
      "author": "John Doe",
      "genre": 1,
      "edition": "3rd Edition",
      "published_date": "2023-01-15"
  }
## Response
  {
      "success": true,
      "message": "Book added successfully",
      "errors": {
          "code": null,
          "message": null,
          "fields": []
      },
      "data": {
          "id": 1,
          "genre": 1,
          "title": "Python Basics",
          "author": "John Doe",
          "edition": "3rd Edition",
          "published_date": "2023-01-15"
      }
  }

## 5.Book Retrieve
## Method
  GET
## Endpoint
  http://127.0.0.1:8000/api/books/
## Response
  {
      "success": true,
      "message": "Books retrieved successfully",
      "errors": {
          "code": null,
          "message": null,
          "fields": []
      },
      "data": [
          {
              "id": 1,
              "genre": 1,
              "title": "Python Basics",
              "author": "John Doe",
              "edition": "3rd Edition",
              "published_date": "2023-01-15"
          },
          {
              "id": 2,
              "genre": 1,
              "title": "Fundaentals of Programming",
              "author": "Harish Narula",
              "edition": "1st Edition",
              "published_date": "2025-01-15"
          }
      ]
  }

## 6.Update Book
## Method 
  PUT
## Endpoint
  http://127.0.0.1:8000/api/books/<int:book_id>/
## Payload
  {
      "title": "Advance Programming",
      "author": "Harish Narula",
      "genre": 1,
      "edition": "1st Edition",
      "published_date": "2025-01-15"
  }
## Response
  {
      "success": true,
      "message": "Book updated successfully",
      "errors": {
          "code": null,
          "message": null,
          "fields": []
      },
      "data": {
          "id": 1,
          "genre": 1,
          "title": "Advance Programming",
          "author": "Harish Narula",
          "edition": "1st Edition",
          "published_date": "2025-01-15"
      }
  }

## 7. Delete Book
## Method
  DELETE
## Endpoint
  http://127.0.0.1:8000/api/books/<int:book_id>/
## Response
  {
      "success": true,
      "message": "Book deleted successfully",
      "errors": {
          "code": null,
          "message": null,
          "fields": []
      },
      "data": {}
  }

## 8. Add Book Review
## Method
  POST
## Endpoint
  http://127.0.0.1:8000/api/book-reviews/
## Payload
  {
      "book": 2,
      "review_text": "This book is very helpful!",
      "rating": 5,
      "student": 1
  }
## Response
  {
      "success": true,
      "message": "Review added successfully.",
      "errors": {
          "code": null,
          "message": null,
          "fields": []
      },
      "data": {
          "id": 1,
          "book": 2,
          "student": 1,
          "review_text": "This book is very helpful!",
          "rating": 5,
          "created_at": "2025-03-24T16:52:29.393633Z"
      }
  }
