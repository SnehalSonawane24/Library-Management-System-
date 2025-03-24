from django.urls import path
from .views import AdminSignupView, AdminLoginView, BookGenreListCreateView, BookListCreateView, BookDetailView, BookReviewListCreateView, StudentBookListView, StudentFeedbackListCreateView

urlpatterns = [
    path('admin/signup/', AdminSignupView.as_view(), name='admin-signup'),

    path('admin/login/', AdminLoginView.as_view(), name='admin-login'),
    # Book Management
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # Book Genre Management
    path('book-genres/', BookGenreListCreateView.as_view(), name='book-genre-list-create'),

    # Book Reviews
    path('book-reviews/', BookReviewListCreateView.as_view(), name='book-review-list-create'),

    # Student Feedback
    path('student-feedback/', StudentFeedbackListCreateView.as_view(), name='student-feedback-list-create'),

    # Public Student Book View
    path('student/books/', StudentBookListView.as_view(), name='student-book-list'),
]
