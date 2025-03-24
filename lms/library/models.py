from django.contrib.auth.models import AbstractUser, Group, Permission, BaseUserManager
from django.db import models
from library.auth_backends import User


# Extend AbstractUser to use email as the primary identifier
class AdminUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        extra_fields.setdefault('username', email)
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class AdminUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, unique=False, blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AdminUserManager()

    groups = models.ManyToManyField(Group, related_name="admin_users", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="admin_users", blank=True)


# Book Genre Model
class BookGenre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


# Book Model
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.ForeignKey(BookGenre, on_delete=models.CASCADE, related_name="books")
    edition = models.CharField(max_length=50, null=True, blank=True)
    published_date = models.DateField()

    def __str__(self):
        return self.title


# Book Review Model
class BookReview(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.student.email} for {self.book.title}"


# Student Feedback Model
class StudentFeedback(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback by {self.student.email}"