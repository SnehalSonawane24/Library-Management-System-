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

## API Endpoints

## 1. Admin Creation
# Method
  POST
# URL
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
## URL
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
## URL
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
## URL
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
## URL
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
## URL
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
## URL
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
## URL
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






